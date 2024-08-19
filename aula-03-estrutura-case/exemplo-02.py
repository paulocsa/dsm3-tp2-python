import os 
os.system('cls')

numero = int(input("\n 1,2,3 - Categoria A \n 4,5,6 - Categoria B \n Escolha uma categoria:"))

# USANDO A ESTRUTURA CONDICIONAL CASE

match numero:
    case 1 | 2 | 3:
        print("Você escolheu a Categoria A")
    
    case 4 | 5 | 6:
        print("Você escolheu a Categoria B")
        
    case _:
        print("Não existe esta categoria")
    
    