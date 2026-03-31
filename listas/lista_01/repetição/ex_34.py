# Estrutura de Controle Repetição - exercício 09

# Alocação de Memória
nums = []
cubos = []
raizes = []
i = 0

# Entrada de Dados
while i < 6:
    nums.append(float(input(f"Qual o valor do {i+1}º número? ")))
    i += 1

# Processamento de Dados
for i in nums:
    cubos.append(float(i**3))
    raizes.append(float(i**(1/3)))


# Saída de Dados
print("-" * 50)
print(f"{'Número':>10} {'Cubo':>15} {'Raiz Cúbica':>15}")
print("-" * 50)

for i in range(len(nums)):
    print(f"{nums[i]:>10.2f} {raizes[i]:>15.2f} {cubos[i]:>15.2f}")

print("-" * 50)
