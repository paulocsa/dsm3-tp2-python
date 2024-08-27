nome1 = input("Digite o nome da primeira pessoa:")
nome2 = input("Digite o nome da segunda pessoa:")
peso1 = float(input(f"Digite o peso do(a) {nome1}:"))
peso2 = float(input(f"Digite o peso do(a) {nome2}:"))


if peso1 > peso2:
    menor = peso2
    maior = peso1
elif peso1 == peso2:
    print("O dois pesos são iguais")
    exit()
else:
    menor = peso1
    maior = peso2
    


if maior == peso1:
    print(f"O mais pesado é o {nome1}")
elif maior == peso2:
    print(f"O mais pesado é o {nome2}")
    

    
