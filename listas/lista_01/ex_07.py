# Estrutura de Controle Sequência - exercício 07
# Entrada de Dados
npg = int(input("Quantos termos terá a PG? "))
a1pg = int(input("Qual é o primeiro termo? "))
q = int(input("Qual é a razão? "))

# Processamento de Dados
# n-ésimo termo
anpg = a1pg * (q ** ( npg - 1))

# soma dos n termos
if q == 1:
    snpg = a1pg * npg
else:
    snpg = (a1pg * (q ** npg - 1)) / (q - 1)

# Saída de Dados    
print(f"Resposta 7: o n-ésimo termo é [{anpg}]; enquanto a soma dos termos será [{snpg}].")
