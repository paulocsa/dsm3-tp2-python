import os 
os.system('cls')  # Limpa a tela do terminal no Windows. No Linux ou macOS, você usaria 'clear'.

# Solicita ao usuário que escolha entre calcular 10% ou 15% e insira o valor
cat = input("\n Digite 'A' para calcular 10% \n Digite 'B' para calcular 15% \n Escolha uma das duas opções:")

valor = float(input("Digite o valor:"))  # Solicita ao usuário que digite o valor para o cálculo

# Converte a escolha do usuário para minúsculas para facilitar a comparação
match (cat.lower()):
    case "a":  # Se a escolha for 'a' (ou 'A')
        nv = (valor * 10) / 100  # Calcula 10% do valor
        print(f"O cálculo de 10% de {valor} é: {nv:.2f}")  # Exibe o resultado formatado com duas casas decimais
    
    case "b":  # Se a escolha for 'b' (ou 'B')
        nv = (valor * 15) / 100  # Calcula 15% do valor
        print(f"O cálculo de 15% de {valor} é {nv:.2f}")  # Exibe o resultado formatado com duas casas decimais
        
    case _:  # Se a escolha não for 'a' nem 'b'
        print("Esta opção não tem cálculos")  # Exibe uma mensagem de erro
        exit()  # Encerra o programa
