# pip install yfinance pandas numpy

from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Any, Dict, Optional

import numpy as np
import pandas as pd
import yfinance as yf


@dataclass
class ValuationResult:
    ticker: str
    price: Optional[float]
    fair_value_per_share: Optional[float]
    upside_pct: Optional[float]
    verdict: str
    notes: list[str]
    metrics: Dict[str, Any]


def _safe_float(x: Any) -> Optional[float]:
    try:
        if x is None or (isinstance(x, float) and math.isnan(x)):
            return None
        return float(x)
    except Exception:
        return None


def _pick_first_available(d: Dict[str, Any], keys: list[str]) -> Optional[float]:
    for k in keys:
        v = _safe_float(d.get(k))
        if v is not None:
            return v
    return None


def _latest_column(df: Optional[pd.DataFrame]) -> Optional[pd.Series]:
    if df is None or df.empty:
        return None
    cols = list(df.columns)
    if not cols:
        return None
    try:
        cols = sorted(cols, reverse=True)
    except Exception:
        pass
    return df[cols[0]]


def _get_statement_value(df: Optional[pd.DataFrame], row_names: list[str]) -> Optional[float]:
    col = _latest_column(df)
    if col is None:
        return None
    for row in row_names:
        if row in col.index:
            return _safe_float(col.loc[row])
    return None


def analyze_discounted_stock(
    ticker: str,
    years_high_growth: int = 5,
    growth_rate: float = 0.08,
    terminal_growth_rate: float = 0.03,
    discount_rate: float = 0.12,
    required_margin_of_safety: float = 0.15,
) -> ValuationResult:
    """
    Triagem simplificada:
    - Preço atual
    - P/L, P/VP, market cap, dívida líquida
    - DCF simplificado via FCF mais recente
    - Veredito: aparenta descontada / neutra / aparenta cara

    Observação:
    - Para ações brasileiras no Yahoo, use .SA, ex.: PETR4.SA, MRVE3.SA
    """
    notes: list[str] = []
    tk = yf.Ticker(ticker)

    # Histórico/último preço
    hist = tk.history(period="1y", auto_adjust=False)
    price = None
    if hist is not None and not hist.empty and "Close" in hist.columns:
        price = _safe_float(hist["Close"].dropna().iloc[-1])

    # Info geral
    info = {}
    try:
        info = tk.info or {}
    except Exception:
        notes.append("Falha ao ler tk.info; usando só demonstrativos, se disponíveis.")

    shares_out = _pick_first_available(info, ["sharesOutstanding", "impliedSharesOutstanding"])
    market_cap = _pick_first_available(info, ["marketCap"])
    total_debt = _pick_first_available(info, ["totalDebt"])
    cash = _pick_first_available(info, ["totalCash"])
    trailing_pe = _pick_first_available(info, ["trailingPE"])
    pb = _pick_first_available(info, ["priceToBook"])
    current_price_info = _pick_first_available(info, ["currentPrice", "regularMarketPrice"])

    if price is None and current_price_info is not None:
        price = current_price_info

    # Demonstrativos
    cashflow = None
    balance = None
    income = None
    try:
        cashflow = tk.cashflow
    except Exception:
        notes.append("Falha ao ler cashflow.")
    try:
        balance = tk.balance_sheet
    except Exception:
        notes.append("Falha ao ler balance sheet.")
    try:
        income = tk.financials
    except Exception:
        notes.append("Falha ao ler income statement.")

    # FCF = CFO - CapEx (CapEx costuma vir negativo; aqui usamos abs para padronizar)
    cfo = _get_statement_value(
        cashflow,
        [
            "Operating Cash Flow",
            "Total Cash From Operating Activities",
            "Cash Flow From Continuing Operating Activities",
        ],
    )
    capex_raw = _get_statement_value(
        cashflow,
        [
            "Capital Expenditure",
            "Capital Expenditures",
        ],
    )
    capex = abs(capex_raw) if capex_raw is not None else None

    fcf = None
    if cfo is not None and capex is not None:
        fcf = cfo - capex
    elif cfo is not None:
        notes.append("CapEx ausente; usando CFO como aproximação ruim de FCF.")
        fcf = cfo
    else:
        notes.append("Sem CFO; DCF não pôde ser calculado.")

    # Dívida líquida
    net_debt = None
    if total_debt is not None or cash is not None:
        net_debt = (total_debt or 0.0) - (cash or 0.0)

    # DCF simplificado
    enterprise_value = None
    equity_value = None
    fair_value_per_share = None

    if fcf is not None and fcf > 0 and shares_out not in (None, 0):
        projected_fcfs = []
        fcf_t = fcf
        for _ in range(years_high_growth):
            fcf_t *= (1 + growth_rate)
            projected_fcfs.append(fcf_t)

        pv_fcfs = sum(f / ((1 + discount_rate) ** i) for i, f in enumerate(projected_fcfs, start=1))

        terminal_fcf = projected_fcfs[-1] * (1 + terminal_growth_rate)
        if discount_rate <= terminal_growth_rate:
            notes.append("discount_rate <= terminal_growth_rate; DCF inválido.")
        else:
            terminal_value = terminal_fcf / (discount_rate - terminal_growth_rate)
            pv_terminal = terminal_value / ((1 + discount_rate) ** years_high_growth)
            enterprise_value = pv_fcfs + pv_terminal

            equity_value = enterprise_value
            if net_debt is not None:
                equity_value = enterprise_value - net_debt

            fair_value_per_share = equity_value / shares_out
    else:
        if fcf is not None and fcf <= 0:
            notes.append("FCF não positivo; DCF ficou sem base confiável.")

    # Upside / downside
    upside_pct = None
    if fair_value_per_share is not None and price not in (None, 0):
        upside_pct = (fair_value_per_share / price) - 1

    # Veredito
    verdict = "Dados insuficientes"
    if upside_pct is not None:
        if upside_pct >= required_margin_of_safety:
            verdict = "Aparenta descontada"
        elif upside_pct <= -required_margin_of_safety:
            verdict = "Aparenta cara"
        else:
            verdict = "Próxima do valor estimado"

    # Notas qualitativas de múltiplos
    if trailing_pe is not None and trailing_pe < 0:
        notes.append("P/L negativo: empresa teve prejuízo; P/L perde utilidade.")
    if pb is not None and pb < 1:
        notes.append("P/VP abaixo de 1 pode sugerir desconto, mas também pode refletir risco/problemas.")
    if net_debt is not None and enterprise_value is not None and net_debt > enterprise_value * 0.5:
        notes.append("Dívida líquida alta em relação ao EV: atenção.")

    metrics = {
        "market_cap": market_cap,
        "shares_outstanding": shares_out,
        "price": price,
        "trailing_pe": trailing_pe,
        "price_to_book": pb,
        "cash": cash,
        "total_debt": total_debt,
        "net_debt": net_debt,
        "cfo": cfo,
        "capex": capex,
        "fcf": fcf,
        "enterprise_value_dcf": enterprise_value,
        "equity_value_dcf": equity_value,
        "growth_rate": growth_rate,
        "terminal_growth_rate": terminal_growth_rate,
        "discount_rate": discount_rate,
    }

    return ValuationResult(
        ticker=ticker,
        price=price,
        fair_value_per_share=fair_value_per_share,
        upside_pct=upside_pct,
        verdict=verdict,
        notes=notes,
        metrics=metrics,
    )


def print_result(res: ValuationResult) -> None:
    print("=" * 70)
    print(f"Ticker: {res.ticker}")
    print(f"Preço atual: {res.price if res.price is not None else 'N/D'}")
    print(
        "Valor justo estimado por ação: "
        f"{round(res.fair_value_per_share, 4) if res.fair_value_per_share is not None else 'N/D'}"
    )
    print(
        "Upside estimado: "
        f"{round(res.upside_pct * 100, 2)}%" if res.upside_pct is not None else "Upside estimado: N/D"
    )
    print(f"Veredito: {res.verdict}")
    print("-" * 70)
    print("Métricas:")
    for k, v in res.metrics.items():
        print(f"  {k}: {v}")
    if res.notes:
        print("-" * 70)
        print("Notas:")
        for n in res.notes:
            print(f"  - {n}")
    print("=" * 70)


if __name__ == "__main__":
    # Exemplos:
    # res = analyze_discounted_stock("AAPL")
    # res = analyze_discounted_stock("MRVE3.SA")
    # res = analyze_discounted_stock("PETR4.SA", growth_rate=0.06, discount_rate=0.13)

    ticker = input("Ticker (ex.: AAPL, PETR4.SA, MRVE3.SA): ").strip().upper()
    res = analyze_discounted_stock(ticker)
    print_result(res)