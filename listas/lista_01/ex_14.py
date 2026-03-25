# Estrutura de Controle Sequência - exercício 14
# Entrada de Dados
valores1 = input("Digite os valores de x1 e y1 separados por espaço: ").replace(",", " ").split()
valores2 = input("Digite os valores de x2 e y2 separados por espaço: ").replace(",", " ").split()

# Processamento de Dados
x1, y1 = map(float, valores1)
x2, y2 = map(float, valores2)

soma_qd = (x2 - x1)**2 + (y2 - y1)**2
distancia = soma_qd ** 0.5

print(f"Resposta 14: A distância entre os pontos é [{distancia:.2f}]")
