from entrada import ler_numero, ler_operacao
from operacoes import somar, subtrair, multiplicar, dividir


def calcular(a, b, operacao):
    """
    Recebe dois números e uma operação.
    Retorna o resultado correspondente.
    """

    if operacao == "+":
        return somar(a, b)

    if operacao == "-":
        return subtrair(a, b)

    if operacao == "*":
        return multiplicar(a, b)

    if operacao == "/":
        return dividir(a, b)


def executar_calculadora():
    """
    Executa a calculadora em linha de comando.
    O programa continua disponível até o usuário digitar FIM.
    """

    print("Calculadora com números reais e complexos")
    print("Digite FIM a qualquer momento para encerrar.")
    print("Para números complexos, use j. Exemplo: 2+3j")
    print()

    while True:
        numero1 = ler_numero("Digite o primeiro número: ")

        if numero1 == "FIM":
            print("Programa encerrado.")
            break

        numero2 = ler_numero("Digite o segundo número: ")

        if numero2 == "FIM":
            print("Programa encerrado.")
            break

        operacao = ler_operacao()

        if operacao == "FIM":
            print("Programa encerrado.")
            break

        try:
            resultado = calcular(numero1, numero2, operacao)
            print(f"Resultado: {resultado}")
            print()

        except ZeroDivisionError as erro:
            print(f"Erro: {erro}")
            print()