from tkinter import *

tela = Tk()

tela.title("Exemplo radio button")

tela.geometry("500x400")

# define o tipo da varivel do radio
var = StringVar()

# define o valor selecionado
var.set("m")

rdb_buttonM = Radiobutton(tela, text="MASC", variable=var, value="m")
rdb_buttonM.place(x=20, y=40)

rdb_buttonF = Radiobutton(tela, text="FEM", variable=var, value="f")
rdb_buttonF.place(x=20, y=80)  # Alterando a posição Y

tela.mainloop()
