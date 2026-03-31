# Estrutura de Controle Repetição - exercício 01

# Alocação de Memória
a = []
resultado = 0.0

# Entrada de Dados
n = int(input("Qual o grau do polinômio? "))
x = float(input("Qual o valor de x? "))

for i in range(n + 1):
    coef = float(input(f"Qual o coeficiente a{i}? "))
    a.append(coef)

# Processamento de Dados
for i in range(n + 1):
    resultado += a[i] * (x**i)

# Saída de Dados
print(f"\nO resultado do polinômio de grau {n}, é [{resultado:.3f}]")
