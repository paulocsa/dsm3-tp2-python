from tkinter import *

tela = Tk()

tela.title("Exemplo check box")

tela.geometry("500x400")

# define o tipo da varivel do radio
var = StringVar()


chk_button = Checkbutton(
    tela, text="check Box", variable=var, onvalue="On", offvalue="Off"
)


def mostrar():
    Label(tela, text=var.get()).pack()
    tela.mainloop()


# para começar sem estar selecionado
chk_button.deselect()

chk_button.pack()

Button(tela, text="Mostrar", command=mostrar).pack()


tela.mainloop()
