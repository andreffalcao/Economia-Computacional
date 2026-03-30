# Estrutura de Controle Seleção - exercício 05

# Entrada de Dados
num = float(input("Digite um número: "))

# Processamento e Saída de Dados
if num < 0:
    info = f"Este número é negativo [{num}]"
elif num == 0:
    info = f"Este número é nulo [{num}]"
else:
    info = f"Este número é positivo [{num}]"

print(info)
