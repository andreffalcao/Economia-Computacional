# Estrutura de Controle Seleção - exercício 07

# Alocação de Memória
test: int = 0
NF: float = 0
conceitos = [(5.99, "D"), (7.49, "C"), (8.99, "B"), (10, "A")]

notas_test = []

# Entrada de Dados
while test < 2:
    nt_test = float(input(f"Qual foi a sua nota no Teste {test+1}? "))
    test += 1
    notas_test.append(nt_test)

t1 = notas_test[0]
t2 = notas_test[1]

prova = float(input(f"Qual foi a nota da sua prova? "))

# Processamento e Saída de Dados

NF = t1 * 0.15 + t2 * 0.15 + 0.7 * prova

for limite, conceito in conceitos:
    if NF <= limite:
        c_final = conceito
        break

if c_final == "D":
    PR = float(input("Qual foi a sua nota na recuperação? "))
    NF = (3 * PR + 2 * NF) / 5

    # Recalcula conceito após recuperação
    for limite, conceito in conceitos:
        if NF <= limite:
            c_final = conceito
            if c_final in ["A", "B"]:
                c_final = "C"
            break



print(f"\nNota Final [{NF:.2f}]; Conceito [{c_final}].")

