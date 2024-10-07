from tkinter import *
import os

os.system("cls")

tela = Tk()
tela.title("Calculadora de Velocidade")
tela.configure(background="#FF0000")

largura = 500
altura = 400

largura_screen = tela.winfo_screenwidth()
altura_screen = tela.winfo_screenheight()

posx = largura_screen / 2 - largura / 2
posy = altura_screen / 2 - altura / 2

tela.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))

lbl_nome = Label(tela, text="Nome Carro: ", font="Arial 15 bold", bg="#FF0000", fg="white")
lbl_nome.place(x=50, y=30)

txt_nome = Entry(tela, width=30, borderwidth=5, fg="blue", bg="white")
txt_nome.place(x=180, y=30)

lbl_distancia = Label(tela, text="Distância Percorrida em metros: ", font="Arial 15 bold", bg="#FF0000", fg="white")
lbl_distancia.place(x=50, y=70)

txt_distancia = Entry(tela, width=10, borderwidth=5, fg="blue", bg="white")
txt_distancia.place(x=360, y=70)

lbl_tempo = Label(tela, text="Tempo em s: ", font="Arial 15 bold", bg="#FF0000", fg="white")
lbl_tempo.place(x=50, y=110)

txt_tempo = Entry(tela, width=10, borderwidth=5, fg="blue", bg="white")
txt_tempo.place(x=180, y=110)

lbl_resultado = Label(tela, text="Velocidade do Carro: ", font="Arial 15 bold", bg="#FF0000", fg="white")
lbl_resultado.place(x=50, y=160)

txt_resultado = Entry(tela, width=20, borderwidth=5, fg="blue", bg="white")
txt_resultado.place(x=230, y=160)

def calcular_velocidade():
    nome = txt_nome.get()
    distancia = float(txt_distancia.get())
    tempo = float(txt_tempo.get())
    velocidade = distancia / tempo
    resultado = f"O carro: {nome}\nPercorreu: {distancia} metros\nem um tempo de: {tempo} segundos\nem uma velocidade de: {velocidade:.2f} m/s"
    txt_resultado.delete(0, END)
    txt_resultado.insert(0, f"{velocidade:.2f} m/s")
    lbl_resultado_final.config(text=resultado)

btn_calcular = Button(tela, text="CALCULAR VELOCIDADE", command=calcular_velocidade, bg="#0000FF", fg="white", font="Arial 12 bold")
btn_calcular.place(x=150, y=210)

lbl_resultado_final = Label(tela, text="", font="Arial 12", bg="#FF0000", fg="white")
lbl_resultado_final.place(x=50, y=250)

tela.mainloop()
