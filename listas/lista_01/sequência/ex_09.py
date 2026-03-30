# Estrutura de Controle Sequência - exercício 09
# Entrada de Dados
a1_eq = float(input("Digite o valor de 'a': "))
b1 = float(input("Digite o valor de 'b': "))
c1 = float(input("Digite o valor de 'c': "))

# Processamento e Saída de Dados
delta = b1**2 - 4*a1_eq*c1 
if a1_eq == 0:
    print("Resposta 9: Não é equação do segundo grau.")
elif delta > 0:
    x1 = (-b1 + delta**0.5) / (2*a1_eq)
    x2 = (-b1 - delta**0.5) / (2*a1_eq)
    print(f"Resposta 9: Raízes: {x1} e {x2}")

elif delta == 0:
    x = -b1 / (2*a1_eq)
    print(f"Resposta 9: Raiz: {x}")
    
else:
    print("Resposta 9: Não possui raízes reais.")
