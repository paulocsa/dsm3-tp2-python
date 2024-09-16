from tkinter import *  # Importa todas as funcionalidades da biblioteca Tkinter para criar interfaces gráficas.

import os  # Importa a biblioteca 'os' para realizar operações no sistema operacional.

# Limpa a tela do terminal no Windows. Em sistemas Linux ou macOS, use 'clear'.
os.system("cls")


# Cria uma instância de uma janela principal chamada 'tela'
tela = Tk()

# Define o título da janela
tela.title("Exemplo 4 interface")

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

# Cria um campo de entrada de texto (Entry) com largura de 40 caracteres, borda com espessura 5, cor do texto azul, e fundo branco
txt_nome = Entry(tela, width=40, borderwidth=5, fg="blue", bg="white")

# Exibe o campo de entrada na janela, centralizando-o verticalmente no layout da janela
txt_nome.pack()

# Insere um texto padrão no campo de entrada, que aparece como dica para o usuário
txt_nome.insert(0, "Digite seu nome...")

# Função chamada quando o botão é clicado
def mostrarMsg():
    # Cria um rótulo (label) com uma mensagem que inclui o texto do campo de entrada
    tbl_msg = Label(tela, text="Bem vindo " + txt_nome.get())
    # Posiciona o rótulo nas coordenadas (x=80, y=100)
    tbl_msg.place(x=80, y=100)

# Cria um botão que, ao ser clicado, chama a função 'mostrarMsg'
btn_botao = Button(tela, text=">Aperte aqui<", command=mostrarMsg)
# Exibe o botão na janela, centralizando-o verticalmente no layout da janela
btn_botao.pack()

# Mantém a janela aberta e interativa até ser fechada manualmente
tela.mainloop()
