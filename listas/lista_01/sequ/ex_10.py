# Estrutura de Controle Sequência - exercício 10
# Entrada de Dados
n = int(input("Qual o prazo do investimento (em anos): "))
k = float(input("Qual o capital investido: "))
i = input("Qual a taxa de juros anual (%): ")
if "%" in i:
    i = float(i.replace("%", "")) /100
else:
    i = float(i)
    if i > 1:
        i = i / 100

# Processamento de Dados
vk = k * (1 + i) ** n

# Saída de Dados
print(f"Resposta 10: O valor capitalizado é R${vk:.2f}")
