"""
Projeto: Calculadora Modular com suporte a Números Complexos
Autor: André Pinheiro Falcão
Disciplina: Economia Computacional
Descrição: Programa de linha de comando que implementa uma calculadora modular com suporte às quatro operações fundamentais e a números complexos.
Versão: 1.0.0

Módulo responsável pelas operações matemáticas da calculadora.
"""

def somar(a, b):
    return a + b


def subtrair(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("Não é possível dividir por zero.")
    return a / b
