# Estrutura de Controle Seleção - exercício 08

# Alcocação de Memória
imcs = [(18.49, "Excessivamente Magro"), (25, "Peso Normal"), (30, "Sobrepeso"), (100, "Obeso")]

# Entrada de Dados

nome = input("Qual o seu nome? ")
peso = float(input("Qual o seu peso? "))
altura = float(input("Qual a sua altura? "))

# Processamento de Dados
if altura > 3:
    altura = altura/100

IMC = peso / (altura * altura)

for limite, imc in imcs:
    if IMC <= limite:
        print(f"{nome.title()} você possui um IMC de {IMC:.2f}; "
              f"Condição é {imc}")
        break

