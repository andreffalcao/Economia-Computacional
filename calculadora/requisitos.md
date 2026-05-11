# Requisitos do Projeto

## Identificação

**Nome do projeto:** Calculadora Modular com suporte a Números Complexos

**Disciplina:** Economia Computacional

**Linguagem:** Python

**Interface:** Linha de comando

**Autor:** André Pinheiro Falcão

**Professor:** Nelson Seixas dos Santos

**Instituição:** Universidade Federal do Rio Grande do Sul - UFRGS

**Semestre:** 2026/1

---

## Enunciado

Faça um programa plenamente modularizado que seja uma calculadora com as quatro operações fundamentais.

A calculadora deve ser capaz de operar com números complexos, ler dois números dados pelo usuário, seguida da operação desejada pelo usuário e colocar na tela a resposta.

A calculadora deve executar em interface de linha de comando e ficar disponível para novo cálculo ao fim da execução de uma operação, a menos que o usuário digite a palavra `FIM`.

O programa deve conter, no máximo, 20 módulos e não possuir mais de 16 MB.

---

## Requisitos funcionais

### RF01 — Realizar as quatro operações fundamentais

O programa deve realizar:

- soma;
- subtração;
- multiplicação;
- divisão.

---

### RF02 — Operar com números complexos

O programa deve aceitar números complexos como entrada.

Em Python, números complexos devem ser escritos usando `j`.

Exemplo:

```text
2+3j
```
---

### RF03 — Ler dois números informados pelo usuário

O programa deve solicitar ao usuário dois números para realizar a operação escolhida.

---

### RF04 — Ler a operação desejada pelo usuário

Após a leitura dos dois números, o programa deve solicitar a operação matemática desejada.

```text
+
-
*
/
```

---

### RF05 — Exibir a resposta na tela

Após realizar o cálculo, o programa deve exibir o resultado da operação na tela.

---

### RF06 — Executar em interface de linha de comando

O programa deve ser executado pelo terminal, usando entrada e saída de dados em linha de comando.

---

### RF07 — Permanecer disponível para novo cálculo

Após executar uma operação, o programa deve continuar disponível para que o usuário realize novos cálculos.

---

### RF08 — Encerrar com a palavra FIM

O programa deve ser encerrado quando o usuário digitar a palavra FIM.

---

## Requisitos não-funcionais

### RNF01 — Modularização

O programa deve ser plenamente modularizado, com separação clara das responsabilidades em diferentes módulos.

---

### RNF02 — Limite de módulos

O programa deve conter, no máximo, 20 módulos.

---

### RNF03 — Limite de tamanho

O programa não deve possuir mais de 16 MB.

---

## Estrutura proposta do projeto

```text
calculadora_complexos/
│
├── main.py
├── entrada.py
├── operacoes.py
├── calculadora.py
└── requisitos.md
```

### Descrição dos módulos

```text
main.py
```
Arquivo principal do programa.
Responsável por iniciar a execução da calculadora.

```text
entrada.py
```
Módulo responsável pela leitura dos números e da operação digitada pelo usuário.

```text
operacoes.py
```
Módulo responsável pelas quatro operações fundamentais.

```text
calculadora.py
```
Módulo responsável pelo controle principal da calculadora, mantendo o programa em execução até o usuário digitar FIM.

---

### Forma de execução

Para executar o programa, abrir o terminal na pasta do projeto e digitar:

```text
python main.py
```
ou:

```text
python3 main.py
```
