import os
os.system('cls')  # Limpa a tela do terminal no Windows. No Linux ou macOS, você usaria 'clear'.

print('*' * 40)  

# Mostrar somente os números ímpares

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # Lista de números de 1 a 10

for i in numbers:
    if i % 2 == 0:  # Verifica se o número é par (divisível por 2)
        continue  # Se o número for par, pula para a próxima iteração do loop
    print(f"Número ímpar: {i}")  # Imprime o número ímpar

print('*' * 40)  
