from tkinter import *
import os

os.system("cls")

tela = Tk()
tela.title("Cadastro de Contatos")
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

lbl_telefone = Label(tela, text="Telefone: ", font="Arial 15 bold", bg="#1e3743", fg="white")
lbl_telefone.place(x=50, y=85)

txt_telefone = Entry(tela, width=30, borderwidth=5, fg="blue", bg="white")
txt_telefone.place(x=200, y=85)

lbl_endereco = Label(tela, text="Endereço: ", font="Arial 15 bold", bg="#1e3743", fg="white")
lbl_endereco.place(x=50, y=125)

txt_endereco = Entry(tela, width=30, borderwidth=5, fg="blue", bg="white")
txt_endereco.place(x=200, y=125)

lbl_cidade = Label(tela, text="Cidade: ", font="Arial 15 bold", bg="#1e3743", fg="white")
lbl_cidade.place(x=50, y=165)

txt_cidade = Entry(tela, width=30, borderwidth=5, fg="blue", bg="white")
txt_cidade.place(x=200, y=165)

lbl_informacoes = Label(tela, text="Informações do Contato: ", font="Arial 15 bold", bg="#1e3743", fg="white")
lbl_informacoes.place(x=50, y=210)

txt_informacoes = Entry(tela, width=50, borderwidth=5, fg="blue", bg="white")
txt_informacoes.place(x=50, y=250)

def cadastrarContato():
    nome = txt_nome.get()
    telefone = txt_telefone.get()
    endereco = txt_endereco.get()
    cidade = txt_cidade.get()

    informacoes = f"Nome: {nome}, Telefone: {telefone}, Endereço: {endereco}, Cidade: {cidade}"
    txt_informacoes.delete(0, END)
    txt_informacoes.insert(0, informacoes)

btn_cadastrar = Button(tela, text="Cadastrar Contato", command=cadastrarContato, bg="#3b6b7f", fg="white", font="Arial 12 bold")
btn_cadastrar.place(x=150, y=300)

tela.mainloop()
