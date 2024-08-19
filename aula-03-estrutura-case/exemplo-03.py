import os 
os.system('cls')

cat = input("\n Digite 'A' para calcular 10% \n Digite 'B' para calcular 15% \n Escolha uma das duas opções:")

valor = float(input("Digite o valor:"))

# variavel.lower para deixar tudo minusculo, variavel.upper para deixar tudo maiusculo

match (cat.lower()):
    case "a":
        nv = (valor * 10)/100
        print(f"O cáculo de 10% de {valor} é: {nv:.2}")
    
    case "b":
        nv = (valor * 15)/100
        print(f"O cálculo de 15% de {valor} é {nv:.2}")
        
    case _:
        print("Esta opção não tem cáculos")
        exit