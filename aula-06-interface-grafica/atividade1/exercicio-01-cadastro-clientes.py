from tkinter import *
import os

os.system("cls")

tela = Tk()
tela.title("Cadastro de Clientes")
tela.configure(background="#1e3743")

largura = 500
altura = 400
largura_screen = tela.winfo_screenwidth()
altura_screen = tela.winfo_screenheight()
posx = largura_screen / 2 - largura / 2
posy = altura_screen / 2 - altura / 2
tela.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))

lbl_nome = Label(tela, text="Nome: ", font="Arial 15 bold", bg="#1e3743", fg="white")
lbl_nome.place(x=50, y=45)

txt_nome = Entry(tela, width=30, borderwidth=5, fg="blue", bg="white")
txt_nome.place(x=200, y=45)

lbl_email = Label(tela, text="E-mail: ", font="Arial 15 bold", bg="#1e3743", fg="white")
lbl_email.place(x=50, y=85)

txt_email = Entry(tela, width=30, borderwidth=5, fg="blue", bg="white")
txt_email.place(x=200, y=85)

lbl_telefone = Label(tela, text="Telefone: ", font="Arial 15 bold", bg="#1e3743", fg="white")
lbl_telefone.place(x=50, y=125)

txt_telefone = Entry(tela, width=30, borderwidth=5, fg="blue", bg="white")
txt_telefone.place(x=200, y=125)

lbl_endereco = Label(tela, text="Endereço: ", font="Arial 15 bold", bg="#1e3743", fg="white")
lbl_endereco.place(x=50, y=165)

txt_endereco = Entry(tela, width=30, borderwidth=5, fg="blue", bg="white")
txt_endereco.place(x=200, y=165)

lbl_resultado = Label(tela, text="Dados cadastrados: ", font="Arial 15 bold", bg="#1e3743", fg="white")
lbl_resultado.place(x=50, y=250)

txt_resul = Entry(tela, width=40, borderwidth=5, fg="blue", bg="white")
txt_resul.place(x=50, y=290)

def cadastrarCliente():
    try:
        nome = txt_nome.get()
        email = txt_email.get()
        telefone = txt_telefone.get()
        endereco = txt_endereco.get()

        resultado = f"Nome: {nome}, E-mail: {email}, Telefone: {telefone}, Endereço: {endereco}"
        txt_resul.delete(0, END)
        txt_resul.insert(0, resultado)
    except ValueError:
        txt_resul.delete(0, END)
        txt_resul.insert(0, "Erro!")

btn_cadastrar = Button(tela, text="Cadastrar", command=cadastrarCliente, bg="#3b6b7f", fg="white", font="Arial 12 bold")
btn_cadastrar.place(x=200, y=210)

tela.mainloop()
