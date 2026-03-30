# Estrutura de Controle Seleção - exercício 01

# Entrada de Dados
num = float(input("\nDigite um número: "))

# Processamento e Saída de Dados
if num < 10:
    print(num * 2)
elif 10 <= num <= 20:
    print(num / 2)
else:
    print(f"Este número não é válido.")
