from tkinter import *  # Importa todas as funcionalidades da biblioteca Tkinter para criar interfaces gráficas.

import os  # Importa a biblioteca 'os' para realizar operações no sistema operacional.

# Limpa a tela do terminal no Windows. Em sistemas Linux ou macOS, use 'clear'.
os.system("cls")

# Cria uma instância de uma janela principal chamada 'tela'
tela = Tk()

# Define o título da janela
tela.title("Exemplo 1 interface")

# Configura o fundo da janela com a cor especificada em hexadecimal
tela.configure(background="#1e3743")

# Define o tamanho da janela como 700x300 pixels
tela.geometry("700x300")

# Define que a janela não pode ser redimensionada nem horizontal nem verticalmente
tela.resizable(False, False)

# Define o tamanho máximo da janela (largura = 800 pixels, altura = 600 pixels)
tela.maxsize(width=800, height=600)

# Define o tamanho mínimo da janela (largura = 300 pixels, altura = 300 pixels)
tela.minsize(width=300, height=300)

# Mantém a janela aberta e interativa até ser fechada manualmente
tela.mainloop()
