"""
Projeto: Calculadora Modular com suporte a Números Complexos
Autor: André Pinheiro Falcão
Disciplina: Economia Computacional
Descrição: Programa de linha de comando que implementa uma calculadora modular com suporte às quatro operações fundamentais e a números complexos.
Versão: 1.0.0

Módulo responsável pela leitura e validação das entradas do usuário.
"""

def ler_numero(mensagem):
    """
    Lê um número real ou complexo digitado pelo usuário.

    Exemplos aceitos:
    2
    3.5
    2+3j
    -1-4j
    """

    while True:
        valor = input(mensagem).strip()

        if valor.upper() == "FIM":
            return "FIM"

        try:
            return complex(valor)
        except ValueError:
            print("Entrada inválida. Digite um número real ou complexo.")
            print("Exemplos: 2, 3.5, 2+3j, -1-4j")


def ler_operacao():
    """
    Lê a operação desejada pelo usuário.
    """

    operacoes_validas = ["+", "-", "*", "/"]

    while True:
        operacao = input("Digite a operação (+, -, *, /) ou FIM para encerrar: ").strip()

        if operacao.upper() == "FIM":
            return "FIM"

        if operacao in operacoes_validas:
            return operacao

        print("Operação inválida. Use +, -, * ou /.")
