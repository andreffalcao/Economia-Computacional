# Estrutura de Controle Sequência - exercício 05
# Alocação de Memória
wh = 40.00
wt = 0.30

# Entrada de Dados
h = int(input("Quantas horas você trabalha? "))

# Processamento de Dados
wb = h * wh
t = wb * wt
wl = wb - t

# Saída de Dados
print(f"Resposta 5: Salário bruto R${wb:.2f};" 
      f" Líquido R${wl:.2f}; Descontos R${t:.2f}!")
