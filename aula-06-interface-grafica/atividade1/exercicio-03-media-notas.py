from tkinter import *
import os

os.system("cls")

tela = Tk()
tela.title("Cálculo de Média")
tela.configure(background="#1e3743")

largura = 500
altura = 400

largura_screen = tela.winfo_screenwidth()
altura_screen = tela.winfo_screenheight()
posx = largura_screen / 2 - largura / 2
posy = altura_screen / 2 - altura / 2

tela.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))

lbl_nota1 = Label(tela, text="Nota 1: ", font="Arial 15 bold", bg="#1e3743", fg="white")
lbl_nota1.place(x=50, y=45)

txt_nota1 = Entry(tela, width=10, borderwidth=5, fg="blue", bg="white")
txt_nota1.place(x=200, y=45)

lbl_nota2 = Label(tela, text="Nota 2: ", font="Arial 15 bold", bg="#1e3743", fg="white")
lbl_nota2.place(x=50, y=85)

txt_nota2 = Entry(tela, width=10, borderwidth=5, fg="blue", bg="white")
txt_nota2.place(x=200, y=85)

lbl_nota3 = Label(tela, text="Nota 3: ", font="Arial 15 bold", bg="#1e3743", fg="white")
lbl_nota3.place(x=50, y=125)

txt_nota3 = Entry(tela, width=10, borderwidth=5, fg="blue", bg="white")
txt_nota3.place(x=200, y=125)

lbl_resultado = Label(tela, text="Média: ", font="Arial 15 bold", bg="#1e3743", fg="white")
lbl_resultado.place(x=50, y=250)

txt_media = Entry(tela, width=10, borderwidth=5, fg="blue", bg="white")
txt_media.place(x=200, y=250)

lbl_situacao = Label(tela, text="Situação: ", font="Arial 15 bold", bg="#1e3743", fg="white")
lbl_situacao.place(x=50, y=290)

txt_situacao = Entry(tela, width=30, borderwidth=5, fg="blue", bg="white")
txt_situacao.place(x=200, y=290)

def calcularMedia():
    try:
        nota1 = float(txt_nota1.get())
        nota2 = float(txt_nota2.get())
        nota3 = float(txt_nota3.get())
        media = (nota1 + nota2 + nota3) / 3

        txt_media.delete(0, END)
        txt_media.insert(0, str(round(media, 2)))

        if media >= 7:
            situacao = "Aprovado"
        elif media >= 3:
            situacao = "Exame"
        else:
            situacao = "Reprovado"

        txt_situacao.delete(0, END)
        txt_situacao.insert(0, situacao)

    except ValueError:
        txt_media.delete(0, END)
        txt_media.insert(0, "Erro!")
        txt_situacao.delete(0, END)
        txt_situacao.insert(0, "Erro!")

btn_calcular = Button(tela, text="Calcular Média", command=calcularMedia, bg="#3b6b7f", fg="white", font="Arial 12 bold")
btn_calcular.place(x=150, y=210)

tela.mainloop()
