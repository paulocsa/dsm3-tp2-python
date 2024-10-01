from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox

tela = Tk()

tela.title("Exemplo combo box")

tela.geometry("250x250")

combo = Combobox(tela)



def mostra_msg():
    messagebox.showinfo("Titulo da caixa", combo.get())

combo["values"] = ("Iguape", "Ilha", "Registro", "juquiá")

# define o valor padrao do combom box
combo.current(0)
combo.pack()

Button(tela, text="Mostra Cidade", command=mostra_msg)

tela.mainloop()
