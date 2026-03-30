# Estrutura de Controle Seleção - exercício 06

# Alocação de Memória

capitais = []

capitais.append("Porto Alegre")
capitais.append("Florianópolis")
capitais.append("Curitiba")

# Entrada de Dados

cidade = input("Informe o nome da cidade: ").title()

# Processamento e Saída de Dados
if cidade in capitais:
    print(f"{cidade.title()}, é uma capital da região sul do Brasil.")
else:
    print(f"{cidade.title()}, não é uma capital da região sul do Brasil.")
