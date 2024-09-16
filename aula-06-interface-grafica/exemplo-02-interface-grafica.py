from tkinter import *  # Importa todas as funcionalidades da biblioteca Tkinter para criar interfaces gráficas.

import os  # Importa a biblioteca 'os' para realizar operações no sistema operacional.

# Limpa a tela do terminal no Windows. Em sistemas Linux ou macOS, use 'clear'.
os.system("cls")

# Cria uma instância de uma janela principal chamada 'tela'
tela = Tk()

# Define o título da janela
tela.title("Exemplo 2 interface")

# Configura o fundo da janela com a cor especificada em hexadecimal
tela.configure(background="#1e3743")

# Define o tamanho da janela como 700x300 pixels
tela.geometry("700x300")

# Define que a janela não pode ser redimensionada nem horizontal nem verticalmente
tela.resizable(False, False)

# Cria um widget de rótulo (label) com o texto "Nome: ", cor de fundo e cor de texto
lbl_nome = Label(tela, text="Nome: ", bg="#1e3743", fg="#ffffff")

# Posiciona o label na janela usando coordenadas absolutas (x=10, y=20)
lbl_nome.place(x=10, y=20)

# Cria um segundo label para "Telefone: ", com as mesmas cores de fundo e texto
lbl_tel = Label(tela, text="Telefone: ", bg="#1e3743", fg="#ffffff")

# Posiciona o label do telefone em coordenadas (x=10, y=50)
lbl_tel.place(x=10, y=40)

# Mantém a janela aberta e interativa até ser fechada manualmente
tela.mainloop()
