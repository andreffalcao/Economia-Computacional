# Estrutura de Controle Seleção - exercício 09

# Alcocação de Memória
IRs = [
    (999.99, 0),
    (2499.99, 0.10),
    (4999.99, 0.20),
    (float("inf"), 0.35)
]

whrs = 20.00 # salário por hora trabalhada

# Entrada de Dados
lhrs = int(input("Quantas horas o empregado trabalha? ")) # número de horas trabalhadas

# Processamento de Dados
wb = whrs * lhrs # salário bruto

for salario, ir in IRs:
    if wb <= salario:
        irpercem = ir
        break

irpago = wb * irpercem
wl = wb - irpago

print(f"Dadas {lhrs} horas trabalhadas, o empregado deve pagar R${irpago:.2f} em imposto de renda;"
      f"\nSua renda líquida é de R${wl:.2f}")

