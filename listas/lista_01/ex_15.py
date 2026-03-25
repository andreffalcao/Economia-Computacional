# Estrutura de Controle Sequência - exercício 15
# Entrada de Dados
valores3 = input("Digite três valores separados por espaço: ").replace(",", " ").split()

# Processamento de Dados
v1, v2, v3 = map(float, valores3)

# Saída de Dados
print(f"Resposta 15: A ordem crescente dos valores é {sorted([v1, v2, v3])}")
