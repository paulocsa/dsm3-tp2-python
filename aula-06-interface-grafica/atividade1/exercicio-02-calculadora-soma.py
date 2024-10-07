from tkinter import *
import os

os.system("cls")

tela = Tk()
tela.title("Calculadora de Soma")
tela.configure(background="#2e3b4e")

largura = 400
altura = 250
largura_screen = tela.winfo_screenwidth()
altura_screen = tela.winfo_screenheight()
posx = largura_screen / 2 - largura / 2
posy = altura_screen / 2 - altura / 2
tela.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))

lbl_num1 = Label(tela, text="Número 1: ", font="Arial 12 bold", bg="#2e3b4e", fg="white")
lbl_num1.place(x=50, y=30)

txt_num1 = Entry(tela, width=15, borderwidth=5, fg="black", bg="#f0f0f0")
txt_num1.place(x=150, y=30)

lbl_num2 = Label(tela, text="Número 2: ", font="Arial 12 bold", bg="#2e3b4e", fg="white")
lbl_num2.place(x=50, y=70)

txt_num2 = Entry(tela, width=15, borderwidth=5, fg="black", bg="#f0f0f0")
txt_num2.place(x=150, y=70)

lbl_resul = Label(tela, text="Resultado: ", font="Arial 12 bold", bg="#2e3b4e", fg="white")
lbl_resul.place(x=50, y=110)

txt_resul = Entry(tela, width=15, borderwidth=5, fg="black", bg="#f0f0f0")
txt_resul.place(x=150, y=110)

def calcularSoma():
    try:
        num1 = float(txt_num1.get())
        num2 = float(txt_num2.get())
        soma = num1 + num2
        txt_resul.delete(0, END)
        txt_resul.insert(0, str(soma))
    except ValueError:
        txt_resul.delete(0, END)
        txt_resul.insert(0, "Erro!")

btn_resultado = Button(tela, text="Calcular", command=calcularSoma, bg="#3b6b7f", fg="white", font="Arial 12 bold")
btn_resultado.place(x=150, y=150)

tela.mainloop()
