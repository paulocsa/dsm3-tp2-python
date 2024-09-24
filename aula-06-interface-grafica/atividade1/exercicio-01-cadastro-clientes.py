from tkinter import *  # Importa todas as funcionalidades da biblioteca Tkinter para criar interfaces gráficas.
import os  # Importa a biblioteca 'os' para realizar operações no sistema operacional.

# Limpa a tela do terminal no Windows. Em sistemas Linux ou macOS, use 'clear'.
os.system("cls")

# Cria uma instância de uma janela principal chamada 'tela'
tela = Tk()

# Define o título da janela
tela.title("Calculadora de Soma")

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

# Labels e caixas de entrada
lbl_num1 = Label(tela, text="Número 1: ", font="Arial 15 bold", bg="#1e3743", fg="white")
lbl_num1.place(x=50, y=45)

txt_num1 = Entry(tela, width=20, borderwidth=10, fg="blue", bg="white")
txt_num1.place(x=280, y=45)

lbl_num2 = Label(tela, text="Número 2: ", font="Arial 15 bold", bg="#1e3743", fg="white")
lbl_num2.place(x=50, y=85)

txt_num2 = Entry(tela, width=20, borderwidth=10, fg="blue", bg="white")
txt_num2.place(x=280, y=85)

lbl_resul = Label(tela, text="Resultado: ", font="Arial 15 bold", bg="#1e3743", fg="white")
lbl_resul.place(x=50, y=125)

txt_resul = Entry(tela, width=20, borderwidth=10, fg="blue", bg="white")
txt_resul.place(x=280, y=125)

def calcularSoma():
    try:
        # Obtém os números a partir das caixas de entrada
        num1 = float(txt_num1.get())
        num2 = float(txt_num2.get())
        soma = num1 + num2
        txt_resul.delete(0, END)  # Limpa a caixa de resultado
        txt_resul.insert(0, str(soma))  # Insere o resultado na caixa de texto
    except ValueError:
        txt_resul.delete(0, END)
        txt_resul.insert(0, "Erro!")  # Exibe um erro se a conversão falhar

# Botão para calcular a soma
btn_resultado = Button(tela, text="> Calcular <", command=calcularSoma, bg="#3b6b7f", fg="white", font="Arial 12 bold")
btn_resultado.place(x=50, y=165)

# Mantém a janela aberta e interativa até ser fechada manualmente
tela.mainloop()
