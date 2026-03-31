# Estrutura de Controle Repetição - exercício 10

# Alocação de Memória
rep = 1

# Entrada de Dados
a = float(input("Digite um valor para a: "))
b = int(input("Digite um valor para b: "))

base = a

# Processamento de Dados
while rep < b:
    base *= a
    rep += 1

# Saída de Dados
print("-" * 40)
print(f"O resultado da potência é [{base}] ")
print("-" * 40)
