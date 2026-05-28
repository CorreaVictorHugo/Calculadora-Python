# Calculadora em Python

Calculadora desktop desenvolvida em Python com interface grafica em Tkinter.
O projeto foi criado para praticar fundamentos de programacao, organizacao de interface e separacao entre regra de negocio e camada visual.

## Funcionalidades

- Operacoes de adicao, subtracao, multiplicacao e divisao
- Operacao de modulo/resto com `%`
- Suporte a numeros decimais
- Botao para limpar a expressao
- Botao para apagar o ultimo caractere
- Entrada tambem pelo teclado
- Tratamento de expressoes invalidas
- Calculo feito sem `eval()`

## Tecnologias

- Python 3
- Tkinter
- Unittest

## Como executar

Clone o repositorio:

```bash
git clone https://github.com/CorreaVictorHugo/Calculadora-Python.git
cd Calculadora-Python
```

Execute a aplicacao:

```bash
python calculadora_display.py
```

## Como testar

```bash
python -m unittest
```

## Estrutura

```text
Calculadora-Python/
├── calculator_engine.py
├── calculadora_display.py
├── test_calculator_engine.py
├── README.md
└── .gitignore
```

## Aprendizados

Durante o desenvolvimento e refatoracao deste projeto, foram praticados:

- Criacao de interfaces graficas com Tkinter
- Organizacao de codigo em modulos
- Tratamento de erros
- Testes automatizados com Unittest
- Avaliacao segura de expressoes matematicas simples usando AST
