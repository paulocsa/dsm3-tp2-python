import os
os.system('cls')  

valores = []

qtd_valores = int(input("Digite a quantidade de valores que deseja inserir:"))

for i in range(qtd_valores):
    valor = int(input(f"Digite o {i+1}° valor:"))
    valores.append(valor)

print("\n Valores armazenados:\n")

for valor in valores:
    print(valor)1-

print("\n Valores armazenados porem pares:")

for valor in valores:
    if valor % 2 == 0:  
        print(valor) 



