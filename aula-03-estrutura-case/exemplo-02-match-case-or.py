import os 
os.system('cls')  # Limpa a tela do terminal no Windows. No Linux ou macOS, você usaria 'clear'.

# Solicita ao usuário que escolha uma categoria baseada no número fornecido
numero = int(input("\n 1,2,3 - Categoria A \n 4,5,6 - Categoria B \n Escolha uma categoria:"))

# Estrutura condicional match para verificar a categoria selecionada
match numero:
    case 1 | 2 | 3:  # Se o número for 1, 2 ou 3
        print("Você escolheu a Categoria A")
    
    case 4 | 5 | 6:  # Se o número for 4, 5 ou 6
        print("Você escolheu a Categoria B")
        
    case _:  # Se o número não corresponder a nenhuma das opções anteriores
        print("Não existe esta categoria")
