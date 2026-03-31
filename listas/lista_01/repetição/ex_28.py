# Estrutura de Controle Repetição - exercício 03

# Alocação de Memória
n = 5
num = []
roots = []
i = 0
# Entrada de Dados
while i < n:
    num.append(float(input(f"Qual o {i+1}º número? ")))
    i += 1

# Processamento de Dados
for i in range(n):
    roots.append(num[i]**2)

# Saída de Dados
print(f"–" * 60)
print(f"As raízes dos números: {num};"
      f"\nSão respectivamente: {roots}.")
print(f"–" * 60)
