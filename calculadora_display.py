
# importando a biblioteca
from tkinter import *
from tkinter import ttk

# varáveis de cores
cor1 = '#000000'
cor2 = '#76ABAE'
cor3 = '#E2E2B6'
cor4 = '#FF9D3D'
cor5 = '#feffff'

                                                                                                                  
janela = Tk()
janela.title('Calculadora')
janela.geometry('350x451') # comando para definir o tamanho da janela principal. Primeiro atributo é a largura(350px) e o segundo é a altura(452).

#janela.config(background=cor2)

# criando frames #
frame_display = Frame(janela, width=350, height=100, background=cor2) 
#  comando para criar um frame dentro da janela. Definindo largura(width), altura(height) e cor de fundo(background ou bg) respectivamente. Parte da calculadora onde ficará a os números da calculadora. Para melhor posicionamento a largura deve ser a mesma da variável que foi criada nessa caso(janela.geometry). frame_display é aonde irá sair o resultado das operações.
frame_display.grid(row=0, column=0) 
#  comando para posicionar o frame na janela.
frame_corpo = Frame(janela, width=350, height=350,)
frame_corpo.grid(row=1, column=0) 
# como o frame_display ja foi definido na linha 0, o frame_corpo irá aparecer na linha 1.

# criando função #
def calcular():
    resultado = eval('2')
    # O eval() é uma função interna do Python que avalia uma string como código Python e executa essa expressão.
    
    # passando o valor para tela #
    valor_texto.set(resultado)
    #StringVar é uma classe no Tkinter que permite associar uma variável de string a um widget de interface gráfica, como um Label, Entry, ou Text.
    
valor_texto = StringVar()
# Essa variável é usada para armazenar e controlar valores do tipo string de maneira que seja possível vincular a uma interface gráfica, permitindo que a atualização da variável também atualize automaticamente o conteúdo do widget associado.
    
   
# criando label #    
app_label = Label(frame_display, textvariable=valor_texto, anchor='e', padx=40, font=('Arial 45'), bg=cor2, fg=cor5) 
# comando para criar um label. Label: É um widget (elemento da interface gráfica) do Tkinter usado para exibir texto ou imagens. 
# parâmetro anchor=E no Tkinter é usado para ajustar o alinhamento do conteúdo dentro do widget, como um Label. A letra E representa East, ou seja, o lado direito do widget.
# parâmetro padx=5 no Tkinter é usado para adicionar espaço horizontal extra (em pixels) entre o conteúdo de um widget e as suas bordas.
app_label.place(x=15, y=5, width=350, height=100)

# criando botões #
# A largura (width) do botão é medida em número de caracteres que ele pode conter, enquanto a altura (height) é o número de linhas de texto que o botão pode ter.#
# parâmetro width do Button não aceita valores em pixels, no TKINTER mas você pode contornar isso ao usar o método place() para especificar as dimensões desejadas.
b1 = Button(frame_corpo, text='C', background = cor4, foreground= cor5, font=('Ivy 30 bold'), relief=RAISED) 
# parâmetro relief=RAISED é utilizado em widgets do Tkinter para definir a aparência da borda do widget,
#você está especificando que deseja que a borda do widget tenha uma aparência elevada, como se o widget estivesse "levantado" em relação à superfície da janela.
b1.place(x=0, y=0,  width=175, height=70,) 
# eixo x é  a largura(horizontal) e eixo y é a altura(vertical). Usando o método place() para substuir os valores para pixels.
b2 = Button(frame_corpo, text='%', overrelief=RIDGE, font=('Ivy 15 bold')) 
# Quando o cursor do mouse passa sobre o botão, a borda muda para RIDGE, dando um efeito visual que indica ao usuário que o botão pode ser clicado. Quando o mouse sai, a borda retorna ao estilo original (RAISED).
b2.place(x=175, y=0,  width=87.5, height=70) 
# o eixo x está com 175px pq o b1 tem 175px de largura.
b3 = Button(frame_corpo, text='/', font=('Ivy 15 bold'))
b3.place(x=262.5, y=0,  width=87.5, height=70)
# posição do botão está em x = 262.5 pq b1 vai até 175px, b2 vai até 262.5 e o b3 vai até 262.5 diferença  de 87.5px entre b2 e b3, já que a largura máxima é de 350px.

# Segunda linha de botões
b4 = Button(frame_corpo, text= '7')
b4.place(x=0, y=70,  width=87.5, height=70)
# o eixo Y está  com 70px pq o b1 tem 70px de altura.
b5 = Button(frame_corpo, text= '8')
b5.place(x=87.5, y=70,  width=87.5, height=70)
b6 = Button(frame_corpo, text= '9')
b6.place(x=175, y=70,  width=87.5, height=70)
b7 = Button(frame_corpo, text= 'X', font=('Ivy 15 bold') )
b7.place(x=262.5, y=70,  width=87.5, height=70)

# Terceira linha de botões
b8 = Button(frame_corpo, text= '4')
b8.place(x=0, y=140,  width=87.5, height=70)
b9 = Button(frame_corpo, text= '5')
b9.place(x=87.5, y=140,  width=87.5, height=70)
b10 = Button(frame_corpo, text= '6')
b10.place(x=175, y=140,  width=87.5, height=70)
b11 = Button(frame_corpo, text= '-', font=('Ivy 15 bold'))
b11.place(x=262.5, y=140,  width=87.5, height=70)

# Quarta linha de botões
b12 = Button(frame_corpo, text= '1')
b12.place(x=0, y=210,  width=87.5, height=70)
b13 = Button(frame_corpo, text= '2')
b13.place(x=87.5, y=210,  width=87.5, height=70)
b13 = Button(frame_corpo, text= '3')
b13.place(x=175, y=210,  width=87.5, height=70)
b13 = Button(frame_corpo, text= '+',font=('Ivy 15 bold'))
b13.place(x=262.5, y=210,  width=87.5, height=70)


b14 = Button(frame_corpo, text='0', background = cor4, foreground= cor5, font=('Ivy 30 bold'), relief=RAISED) 
b14.place(x=0, y=280,  width=175, height=70,) 
b15 = Button(frame_corpo, text=',', overrelief=RIDGE, font=('Ivy 15 bold')) 
b15.place(x=175, y=280,  width=87.5, height=70) 
b16 = Button(frame_corpo, text='=', font=('Ivy 15 bold'))
b16.place(x=262.5, y=280,  width=87.5, height=70)

calcular()

janela.mainloop() 
