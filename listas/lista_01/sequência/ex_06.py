# Estrutura de Controle Sequência - exercício 06
# Entrada de Dados
n = int(input("Quantos termos terá a PA? "))
a1_pa = int(input("Qual é o primeiro termo? "))
r = int(input("Qual é a razão? "))

# Processamento de Dados
# n-ésimo termo
an = a1_pa + (n - 1) * r

# soma dos n termos
sn = n * (a1_pa + an) // 2

# Saída de Dados
print(f"Resposta 6: o n-ésimo termo é [{an}]; enquanto a soma dos termos será [{sn}].")
