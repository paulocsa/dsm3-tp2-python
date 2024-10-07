from tkinter import *
from tkinter import ttk, messagebox, filedialog
from PIL import Image, ImageTk

dados_pessoas = {}

def salvar_dados():
    codigo = entry_codigo.get()
    nome = entry_nome.get()
    idade = entry_idade.get()
    sexo = "M" if radio_sexo_m.select() else "F"
    altura = entry_altura.get()
    peso = entry_peso.get()
    cidade = combo_cidade.get()
    data_nasc = entry_data_nasc.get()
    data_cadastro = entry_data_cadastro.get()
    data_atualizacao = entry_data_atualizacao.get()
    descricao = entry_descricao.get()

    if not codigo or not nome:
        messagebox.showwarning("Aviso", "Código e Nome são campos obrigatórios.")
        return

    dados_pessoas[codigo] = {
        "nome": nome,
        "idade": idade,
        "sexo": sexo,
        "altura": altura,
        "peso": peso,
        "cidade": cidade,
        "data_nasc": data_nasc,
        "data_cadastro": data_cadastro,
        "data_atualizacao": data_atualizacao,
        "descricao": descricao
    }

    messagebox.showinfo("Sucesso", f"Dados salvos para a pessoa com código {codigo}!")

def limpar_campos():
    entry_codigo.delete(0, END)
    entry_nome.delete(0, END)
    entry_idade.delete(0, END)
    radio_sexo_m.deselect()
    radio_sexo_f.deselect()
    entry_altura.delete(0, END)
    entry_peso.delete(0, END)
    combo_cidade.set('')
    entry_data_nasc.delete(0, END)
    entry_data_cadastro.delete(0, END)
    entry_data_atualizacao.delete(0, END)
    entry_descricao.delete(0, END)
    label_imagem.config(image='')
    text_consulta.delete(1.0, END)  

def excluir_dados():
    codigo = entry_codigo.get()
    if codigo in dados_pessoas:
        del dados_pessoas[codigo]  
        messagebox.showinfo("Sucesso", f"Dados excluídos para a pessoa com código {codigo}!")
        limpar_campos()  
    else:
        messagebox.showwarning("Aviso", "Código não encontrado.")

def carregar_imagem():
    caminho_imagem = filedialog.askopenfilename(title="Escolha uma imagem", filetypes=[("Arquivos de imagem", "*.png;*.jpg;*.jpeg")])
    if caminho_imagem:
        img = Image.open(caminho_imagem)
        img = img.resize((120, 120))  
        foto = ImageTk.PhotoImage(img)
        label_imagem.config(image=foto)
        label_imagem.image = foto  


def consultar_dados():
    codigo = entry_codigo.get()
    if codigo in dados_pessoas:
        pessoa = dados_pessoas[codigo]
        
        text_consulta.delete(1.0, END)  
        texto = f"Código: {codigo}\nNome: {pessoa['nome']}\nIdade: {pessoa['idade']}\nSexo: {pessoa['sexo']}\n"
        texto += f"Altura: {pessoa['altura']}\nPeso: {pessoa['peso']}\nCidade: {pessoa['cidade']}\n"
        texto += f"Data de Nascimento: {pessoa['data_nasc']}\nData de Cadastro: {pessoa['data_cadastro']}\n"
        texto += f"Data de Atualização: {pessoa['data_atualizacao']}\nDescrição: {pessoa['descricao']}"
        text_consulta.insert(END, texto)
    else:
        messagebox.showwarning("Aviso", "Código não encontrado.")

def alterar_dados():
    codigo = entry_codigo.get()
    if codigo in dados_pessoas:
        dados_pessoas[codigo]["nome"] = entry_nome.get()
        dados_pessoas[codigo]["idade"] = entry_idade.get()
        dados_pessoas[codigo]["sexo"] = "M" if radio_sexo_m.select() else "F"
        dados_pessoas[codigo]["altura"] = entry_altura.get()
        dados_pessoas[codigo]["peso"] = entry_peso.get()
        dados_pessoas[codigo]["cidade"] = combo_cidade.get()
        dados_pessoas[codigo]["data_nasc"] = entry_data_nasc.get()
        dados_pessoas[codigo]["data_cadastro"] = entry_data_cadastro.get()
        dados_pessoas[codigo]["data_atualizacao"] = entry_data_atualizacao.get()
        dados_pessoas[codigo]["descricao"] = entry_descricao.get()
        
        messagebox.showinfo("Sucesso", f"Dados alterados para a pessoa com código {codigo}!")
    else:
        messagebox.showwarning("Aviso", "Código não encontrado.")

def criar_janela():
    tela = Tk()
    tela.title("Controle de Pessoas")
    tela.geometry("900x600")  

    tela.iconbitmap('C:\\Users\\emers\\OneDrive\\Área de Trabalho\\dsm3-tp2-python\\aula-07-interface-grafica-02\\atividade1\\icones\\icone.ico')

    global entry_codigo, entry_nome, entry_idade, radio_sexo_m, radio_sexo_f
    global entry_altura, entry_peso, combo_cidade, entry_data_nasc
    global entry_data_cadastro, entry_data_atualizacao, entry_descricao, label_imagem, text_consulta

    # Colunas de entrada de dados
    Label(tela, text="Código:", font=("Arial", 10)).grid(row=0, column=0, padx=10, pady=5, sticky=W)
    entry_codigo = Entry(tela, width=10)
    entry_codigo.grid(row=0, column=1, padx=5, pady=5)

    Label(tela, text="Nome:", font=("Arial", 10)).grid(row=0, column=2, padx=10, pady=5, sticky=W)
    entry_nome = Entry(tela, width=30)
    entry_nome.grid(row=0, column=3, padx=5, pady=5)

    Label(tela, text="Idade:", font=("Arial", 10)).grid(row=0, column=4, padx=10, pady=5, sticky=W)
    entry_idade = Entry(tela, width=5)
    entry_idade.grid(row=0, column=5, padx=5, pady=5)

    Label(tela, text="Sexo:", font=("Arial", 10)).grid(row=1, column=0, padx=10, pady=5, sticky=W)
    radio_sexo_m = Radiobutton(tela, text="M", value="M")
    radio_sexo_m.grid(row=1, column=1, padx=5, pady=5, sticky=W)
    radio_sexo_f = Radiobutton(tela, text="F", value="F")
    radio_sexo_f.grid(row=1, column=2, padx=5, pady=5, sticky=W)

    Label(tela, text="Altura", font=("Arial", 10)).grid(row=1, column=3, padx=10, pady=5, sticky=W)
    entry_altura = Entry(tela, width=10)
    entry_altura.grid(row=1, column=4, padx=5, pady=5)

    Label(tela, text="Peso", font=("Arial", 10)).grid(row=1, column=5, padx=10, pady=5, sticky=W)
    entry_peso = Entry(tela, width=10)
    entry_peso.grid(row=1, column=6, padx=5, pady=5)

    Label(tela, text="Cidade", font=("Arial", 10)).grid(row=2, column=0, padx=10, pady=5, sticky=W)
    combo_cidade = ttk.Combobox(tela, values=["Registro", "Outra Cidade"], width=20)
    combo_cidade.grid(row=2, column=1, padx=5, pady=5)

    Label(tela, text="Data Nascimento", font=("Arial", 10)).grid(row=2, column=3, padx=10, pady=5, sticky=W)
    entry_data_nasc = Entry(tela, width=15)
    entry_data_nasc.grid(row=2, column=4, padx=5, pady=5)

    Label(tela, text="Data Cadastro", font=("Arial", 10)).grid(row=3, column=0, padx=10, pady=5, sticky=W)
    entry_data_cadastro = Entry(tela, width=15)
    entry_data_cadastro.grid(row=3, column=1, padx=5, pady=5)

    Label(tela, text="Data Atualização", font=("Arial", 10)).grid(row=3, column=3, padx=10, pady=5, sticky=W)
    entry_data_atualizacao = Entry(tela, width=15)
    entry_data_atualizacao.grid(row=3, column=4, padx=5, pady=5)

    Label(tela, text="Descrição", font=("Arial", 10)).grid(row=4, column=0, padx=10, pady=5, sticky=W)
    entry_descricao = Entry(tela, width=50)
    entry_descricao.grid(row=4, column=1, columnspan=4, padx=5, pady=5)

    label_imagem = Label(tela, text="Sem imagem", width=15, height=7, bg="gray")
    label_imagem.grid(row=1, column=7, rowspan=3, padx=10, pady=5)

    Button(tela, text="Escolher Imagem", command=carregar_imagem).grid(row=4, column=7, padx=5, pady=5)

    foto_salvar = PhotoImage(file=r"C:\Users\emers\OneDrive\Área de Trabalho\dsm3-tp2-python\aula-07-interface-grafica-02\atividade1\icones\salvar.png")
    foto_excluir = PhotoImage(file=r"C:\Users\emers\OneDrive\Área de Trabalho\dsm3-tp2-python\aula-07-interface-grafica-02\atividade1\icones\excluir.png")
    foto_alterar = PhotoImage(file=r"C:\Users\emers\OneDrive\Área de Trabalho\dsm3-tp2-python\aula-07-interface-grafica-02\atividade1\icones\alterar.png")
    foto_consultar = PhotoImage(file=r"C:\Users\emers\OneDrive\Área de Trabalho\dsm3-tp2-python\aula-07-interface-grafica-02\atividade1\icones\consultar.png")
    foto_sair = PhotoImage(file=r"C:\Users\emers\OneDrive\Área de Trabalho\dsm3-tp2-python\aula-07-interface-grafica-02\atividade1\icones\sair.png")

    Button(tela, text="Salvar", image=foto_salvar, compound=TOP, command=salvar_dados).grid(row=5, column=1, padx=5, pady=10)
    Button(tela, text="Excluir", image=foto_excluir, compound=TOP, command=excluir_dados).grid(row=5, column=2, padx=5, pady=10)
    Button(tela, text="Alterar", image=foto_alterar, compound=TOP, command=alterar_dados).grid(row=5, column=3, padx=5, pady=10)
    Button(tela, text="Consultar", image=foto_consultar, compound=TOP, command=consultar_dados).grid(row=5, column=4, padx=5, pady=10)
    Button(tela, text="Sair", image=foto_sair, compound=TOP, command=tela.quit).grid(row=5, column=5, padx=5, pady=10)

    text_consulta = Text(tela, height=10, width=80)
    text_consulta.grid(row=6, column=0, columnspan=6, padx=10, pady=10)

    tela.mainloop()

criar_janela()
