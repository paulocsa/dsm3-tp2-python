from tkinter import *
from tkinter import messagebox

tela = Tk()
tela.title("Controle de estoque")

tela.configure(background='#edfe9e')
tela.geometry("500x400")

lbl1= Label(tela, text="Quantidade (1ª quinzena):",bg="#edfe9e",fg="#000000")
lbl1.place(x=20, y=30)
lbl2= Label(tela, text="Quantidade (2ª quinzena):",bg="#edfe9e",fg="#000000")
lbl2.place(x=20, y=60)

txt1= Entry(tela, width=50, borderwidth=3, fg="#000000")
txt1.place(x=160, y=30)

txt2= Entry(tela, width=50, borderwidth=3, fg="#000000")
txt2.place(x=160, y=60)

def calcular_media():
    valor1 = txt1.get()
    valor2 =txt2.get()
    media = ((float(valor1)+float(valor2))/2)
    txt3.insert(0, f"O resultado da média do estoque é: {media:.2f}")
    label3 = Label(tela, text=f"O resultado da média do estoque é: {media:.2f}")
    label3.place(x=160, y=150)
    
        
btn_botao = Button(tela,text = "Calcular Média", font="Arial", bg="#0015ff", fg="#ffffff", command=calcular_media, width="20")
btn_botao.place(x=160, y=100)





txt3= Entry(tela, width=50, borderwidth=3, fg="#000000")
txt3.place(x=160, y=180)


tela.mainloop()