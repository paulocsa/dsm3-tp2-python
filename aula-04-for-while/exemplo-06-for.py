import os
os.system('cls')  # Limpa a tela do terminal no Windows. No Linux ou macOS, você usaria 'clear'.

print('*' * 40)  

# Armazenar valores em uma lista utilizando um loop for

listanumeros = []  # Inicializa uma lista vazia para armazenar os números

for i in range(1, 6):  # Loop de 1 a 5 (inclusive)
    numero = int(input(f"Digite o {i}° número:"))  # Solicita ao usuário que digite um número
    listanumeros.append(numero)  # Adiciona o número digitado à lista
    print("Números armazenados")
    
    # Exibe todos os números armazenados na lista até o momento
    for i in listanumeros:
        print(i)

print('*' * 40)  
