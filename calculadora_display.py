from tkinter import *

# Cores
cor1 = '#000000'
cor2 = '#76ABAE'
cor3 = '#E2E2B6'
cor4 = '#FF9D3D'
cor5 = '#feffff'

# Janela
janela = Tk()
janela.title('Calculadora')
janela.geometry('350x451')

# Frames
frame_display = Frame(janela, width=350, height=100, background=cor2)
frame_display.grid(row=0, column=0)

frame_corpo = Frame(janela, width=350, height=350)
frame_corpo.grid(row=1, column=0)

# Variáveis
valor_texto = StringVar()
expressao = ""  # aqui vamos armazenar o que o usuário digita

# Funções

def adicionar_valor(valor):
    global expressao # Diz para o Python que a função vai usar e modificar a variável expressao que está fora da função (global), e não criar uma nova só dentro dela.
    expressao += str(valor) # Pega o que já está armazenado em expressao e concatena com o novo valor recebido.
    valor_texto.set(expressao) # Atualiza o display da calculadora (o Label que está vinculado ao valor_texto) com a nova expressão. Isso faz a tela mostrar exatamente o que você está digitando.

def calcular():
    global expressao # Diz que a função vai usar a variável global expressao (onde estão armazenados os números e operações que o usuário digitou).
    try: # Bloco para tentar executar o cálculo. Se algo der errado (ex.: usuário digitou 5/0), cai no except.
        resultado = eval(expressao) # Usa a função eval() para interpretar a string expressao como código Python e calcular.Exemplo:expressao = "5+3*2"eval("5+3*2") → retorna 11.        
        valor_texto.set(str(resultado)) # Atualiza o display da calculadora com o resultado.
        expressao = str(resultado)  # Atualiza a variável expressao para o resultado.
    except: # Se der erro (ex.: divisão por zero, ou expressão inválida), mostra "Erro" no display e limpa a variável expressao.
        valor_texto.set("Erro")
        expressao = ""

def limpar(): # Define a função que será chamada quando o usuário clicar no botão C (Clear).
    global expressao 
    expressao = "" # Limpa a variável expressao, ou seja, apaga tudo o que o usuário digitou até agora. 
    valor_texto.set("") # Atualiza o display da calculadora para ficar vazio (sem mostrar nada).

# Display
app_label = Label(frame_display, textvariable=valor_texto, anchor='e', padx=40, font=('Arial 30'), bg=cor2, fg=cor5)
app_label.place(x=15, y=5, width=320, height=90)

# Botões
Button(frame_corpo, text='C', bg=cor4, fg=cor5, font=('Ivy 20 bold'), relief=RAISED, command=limpar).place(x=0, y=0, width=175, height=70)
Button(frame_corpo, text='%', font=('Ivy 15 bold'), command=lambda: adicionar_valor('%')).place(x=175, y=0, width=87.5, height=70)
Button(frame_corpo, text='/', font=('Ivy 15 bold'), command=lambda: adicionar_valor('/')).place(x=262.5, y=0, width=87.5, height=70)

Button(frame_corpo, text='7', command=lambda: adicionar_valor(7)).place(x=0, y=70, width=87.5, height=70)
Button(frame_corpo, text='8', command=lambda: adicionar_valor(8)).place(x=87.5, y=70, width=87.5, height=70)
Button(frame_corpo, text='9', command=lambda: adicionar_valor(9)).place(x=175, y=70, width=87.5, height=70)
Button(frame_corpo, text='*', font=('Ivy 15 bold'), command=lambda: adicionar_valor('*')).place(x=262.5, y=70, width=87.5, height=70)

Button(frame_corpo, text='4', command=lambda: adicionar_valor(4)).place(x=0, y=140, width=87.5, height=70)
Button(frame_corpo, text='5', command=lambda: adicionar_valor(5)).place(x=87.5, y=140, width=87.5, height=70)
Button(frame_corpo, text='6', command=lambda: adicionar_valor(6)).place(x=175, y=140, width=87.5, height=70)
Button(frame_corpo, text='-', font=('Ivy 15 bold'), command=lambda: adicionar_valor('-')).place(x=262.5, y=140, width=87.5, height=70)

Button(frame_corpo, text='1', command=lambda: adicionar_valor(1)).place(x=0, y=210, width=87.5, height=70)
Button(frame_corpo, text='2', command=lambda: adicionar_valor(2)).place(x=87.5, y=210, width=87.5, height=70)
Button(frame_corpo, text='3', command=lambda: adicionar_valor(3)).place(x=175, y=210, width=87.5, height=70)
Button(frame_corpo, text='+', font=('Ivy 15 bold'), command=lambda: adicionar_valor('+')).place(x=262.5, y=210, width=87.5, height=70)

Button(frame_corpo, text='0', bg=cor4, fg=cor5, font=('Ivy 20 bold'), command=lambda: adicionar_valor(0)).place(x=0, y=280, width=175, height=70)
Button(frame_corpo, text='.', font=('Ivy 15 bold'), command=lambda: adicionar_valor('.')).place(x=175, y=280, width=87.5, height=70)
Button(frame_corpo, text='=', font=('Ivy 15 bold'), command=calcular).place(x=262.5, y=280, width=87.5, height=70)

janela.mainloop()
