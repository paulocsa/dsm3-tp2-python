import os
os.system('cls')  # Limpa a tela do terminal no Windows. Em sistemas Linux ou macOS, use 'clear'.

print('*' * 40)  

# Solicita ao usuário que digite uma sequência de números separados por espaço
dados = input("Digite os números separados por espaço: ")  # Recebe uma string de números separados por espaço do usuário.

# Converte a string de números em uma lista de inteiros
vetor = [int(x) for x in dados.split()]  # Usa uma list comprehension para dividir a string em uma lista de strings e converter cada string em um número inteiro.

print(f"Vetor: {vetor}")  # Exibe a lista de números inteiros resultante da conversão.

print('*' * 40)  
