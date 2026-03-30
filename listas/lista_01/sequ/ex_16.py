# Estrutura de Controle Sequência - exercício 16
# Entrada de Dados
retfree = float(input("Digite o valor da taxa de retorno livre de risco: "))
beta = float(input("Digite o valor do beta do ativo: "))
retmerc = float(input("Digite o valor da taxa de retorno do mercado: "))

# Processamento de Dados
capm = retfree + beta * (retmerc - retfree)

print(f"Resposta 16: O retorno esperado do ativo é [{capm:.2f}]")
