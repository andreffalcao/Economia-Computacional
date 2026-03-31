# Estrutura de Controle Repetição - exercício 02

# Alocação de Memória
x = 1.0

# Entrada de Dados
a = float(input("Qual o número para cálculo da raiz quadrada? "))

# Processamento de Dados
for i in range(10):
    x = (x + a / x) * 0.5

# Saída de Dados
print(f"A raiz quadrada do número {a}, é [{x}].")
