# Estrutura de Controle Repetição - exercício 07

# Saída de Dados

print("–" * 25)
print("Números Pares de 1 a 100")
print("–" * 25)

for i in range(1, 101):
    if i % 2 == 0:
        print(f"{i:4}|", end="")
        if i % 5 == 0:
            print()

print("–" * 25)
