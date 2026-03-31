# Estrutura de Controle Repetição - exercício 05

# Alocação de Memória
termos = []
n = 10

# Entrada de Dados
r = int(input("Qual é a razão? "))
a1_pa = float(input("Qual é o primeiro termo da PA? "))

# Processamento de Dados
for i in range(n):
    termos.append(a1_pa + i * r)

# Saída de Dados
print(f"–" * 60)
print(f"Os dez primeiros termos da PA estão listados abaixo\n{termos}")
print(f"–" * 60)

