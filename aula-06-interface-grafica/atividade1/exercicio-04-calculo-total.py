from tkinter import *
import os

os.system("cls")

tela = Tk()
tela.title("Cálculo de Total do Produto")
tela.configure(background="#1e3743")

largura = 500
altura = 400

largura_screen = tela.winfo_screenwidth()
altura_screen = tela.winfo_screenheight()
posx = largura_screen / 2 - largura / 2
posy = altura_screen / 2 - altura / 2

tela.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))

lbl_produto = Label(tela, text="Produto: ", font="Arial 15 bold", bg="#1e3743", fg="white")
lbl_produto.place(x=50, y=45)

txt_produto = Entry(tela, width=30, borderwidth=5, fg="blue", bg="white")
txt_produto.place(x=200, y=45)

lbl_quantidade = Label(tela, text="Quantidade: ", font="Arial 15 bold", bg="#1e3743", fg="white")
lbl_quantidade.place(x=50, y=85)

txt_quantidade = Entry(tela, width=10, borderwidth=5, fg="blue", bg="white")
txt_quantidade.place(x=200, y=85)

lbl_preco = Label(tela, text="Preço: ", font="Arial 15 bold", bg="#1e3743", fg="white")
lbl_preco.place(x=50, y=125)

txt_preco = Entry(tela, width=10, borderwidth=5, fg="blue", bg="white")
txt_preco.place(x=200, y=125)

lbl_total = Label(tela, text="Total: ", font="Arial 15 bold", bg="#1e3743", fg="white")
lbl_total.place(x=50, y=250)

txt_total = Entry(tela, width=10, borderwidth=5, fg="blue", bg="white")
txt_total.place(x=200, y=250)

lbl_informacoes = Label(tela, text="Informações do Produto: ", font="Arial 15 bold", bg="#1e3743", fg="white")
lbl_informacoes.place(x=50, y=290)

txt_informacoes = Entry(tela, width=40, borderwidth=5, fg="blue", bg="white")
txt_informacoes.place(x=50, y=320)

def calcularTotal():
    try:
        produto = txt_produto.get()
        quantidade = int(txt_quantidade.get())
        preco = float(txt_preco.get())
        total = quantidade * preco

        txt_total.delete(0, END)
        txt_total.insert(0, str(round(total, 2)))

        informacoes = f"Produto: {produto}, Quantidade: {quantidade}, Preço: {preco}"
        txt_informacoes.delete(0, END)
        txt_informacoes.insert(0, informacoes)

    except ValueError:
        txt_total.delete(0, END)
        txt_total.insert(0, "Erro!")
        txt_informacoes.delete(0, END)
        txt_informacoes.insert(0, "Erro!")

btn_calcular = Button(tela, text="Calcular Total", command=calcularTotal, bg="#3b6b7f", fg="white", font="Arial 12 bold")
btn_calcular.place(x=150, y=210)

tela.mainloop()
