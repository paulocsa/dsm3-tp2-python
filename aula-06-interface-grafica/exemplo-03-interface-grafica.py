from tkinter import *  # Importa todas as funcionalidades da biblioteca Tkinter para criar interfaces gráficas.

import os  # Importa a biblioteca 'os' para realizar operações no sistema operacional.

# Limpa a tela do terminal no Windows. Em sistemas Linux ou macOS, use 'clear'.
os.system("cls")


# Cria uma instância de uma janela principal chamada 'tela'
tela = Tk()

# Define o título da janela
tela.title("Exemplo 3 interface")

# Configura o fundo da janela com a cor especificada em hexadecimal
tela.configure(background="#1e3743")

# Define a largura e altura da janela
largura = 800
altura = 300

# Obtém a largura da tela
largura_screen = tela.winfo_screenwidth()

# Obtém a altura da tela
altura_screen = tela.winfo_screenheight()

# Calcula a posição horizontal (x) para centralizar a janela
posx = largura_screen / 2 - largura / 2

# Calcula a posição vertical (y) para centralizar a janela
posy = altura_screen / 2 - altura / 2

# Define a geometria da janela, com dimensões e posição centralizadas
tela.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))

# Cria um rótulo (label) com o texto "Nome: ", usando a fonte Arial tamanho 25 com estilo negrito e itálico
lbl_nome = Label(tela, text="Nome: ", font="Arial 25 bold italic")

# Posiciona o rótulo "Nome: " nas coordenadas (x=10, y=10)
lbl_nome.place(x=10, y=10)

# Cria um segundo rótulo com o texto "Endereço: ", usando a fonte Comic Sans MS tamanho 20 com estilo negrito
lbl_end = Label(tela, text="Endereço: ", font=("Comic Sans MS", "20", "bold"))

# Posiciona o rótulo "Endereço: " nas coordenadas (x=10, y=60)
lbl_end.place(x=10, y=60)

# Mantém a janela aberta e interativa até ser fechada manualmente
tela.mainloop()
