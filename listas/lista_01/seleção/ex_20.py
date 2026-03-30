# Estrutura de Controle Seleção - exercício 04

# Entrada de Dados
name = input(f"Qual o seu nome? ")
age = int(input(f"Qual a sua idade? "))

# Processamento e Saída de Dados
if age < 18:
    aviso = f"{name} não pode assistir a este filme."
else:
    aviso = f"{name} pode assistir a este filme."

print(aviso)
