# Estrutura de Controle Repetição - exercício 04

# Alocação de Memória
nums = list(range(21))
pars = []
resto = 0

# Processamento de Dados
for i in nums:
    if i % 2 == 0:
        pars.append(i)

# Saída de Dados
print(f"–" * 50)
print(f"Para os números de [0 a 20], os números pares são: \n{pars}.")
print(f"–" * 50)
