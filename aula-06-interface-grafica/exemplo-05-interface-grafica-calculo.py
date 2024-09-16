from tkinter import *  # Importa todas as funcionalidades da biblioteca Tkinter para criar interfaces gráficas.

import os  # Importa a biblioteca 'os' para realizar operações no sistema operacional.

# Limpa a tela do terminal no Windows. Em sistemas Linux ou macOS, use 'clear'.
os.system("cls")


# Cria uma instância de uma janela principal chamada 'tela'
tela = Tk()

# Define o título da janela
tela.title("Exemplo 5 interface")

# Configura o fundo da janela com a cor especificada em hexadecimal
tela.configure(background="#1e3743")

# Define a largura e altura da janela
largura = 800
altura = 300

# Obtém a largura da tela
largura_screen = tela.winfo_screenwidth()

# Obtém a altura da tela
altura_screen = tela.winfo_screenheight()

# Calcula a posição horizontal (x) para centralizar a janela
posx = largura_screen / 2 - largura / 2

# Calcula a posição vertical (y) para centralizar a janela
posy = altura_screen / 2 - altura / 2

# Define a geometria da janela, com dimensões e posição centralizadas
tela.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))


lbl_num1 = Label(tela, text="Número 1: ", font="Arial 15 bold")
lbl_num1.place(x=50, y=45)

txt_num1 = Entry(tela, width=20, borderwidth=10, fg="blue", bg="white")
txt_num1.place(x=280, y=45)
txt_num1.insert(0, "Digite um número: ")


lbl_num2 = Label(tela, text="Número 2: ", font="Arial 15 bold")
lbl_num2.place(x=50, y=85)

txt_num2 = Entry(tela, width=20, borderwidth=10, fg="blue", bg="white")
txt_num2.place(x=350, y=85)
txt_num2.insert(0, "Digite outro número: ")


lbl_resyl = Label(tela, text="Resultado: ", font="Arial 15 bold")
lbl_resyl.place(x=50, y=150)

txt_resul = Entry(tela, width=20, borderwidth=10, fg="blue", bg="white")
txt_resul.place(x=350, y=185)


def calcularSoma():
    soma = float(txt_num1.get()) + float(txt_num2.get())
    txt_resul.insert(0, soma)

    lbl_soma = Label(tela, text="Resultado: " + str(soma))
    lbl_soma.place(x=205, y=335)


btn_resultado = Button(tela, text=">Calcular<", command =calcularSoma)


btn_resultado.place(x=50,y=200)


# Mantém a janela aberta e interativa até ser fechada manualmente
tela.mainloop()
