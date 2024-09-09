import os
os.system('cls')  # Limpa a tela do terminal no Windows. Em sistemas Linux ou macOS, use 'clear'.

print('*' * 40)  

# Solicita ao usuário o número de linhas e colunas da matriz
linhas = int(input("Digite o número de linhas da matriz:"))  # Lê o número de linhas da matriz.
colunas = int(input("Digite o número de colunas da matriz:"))  # Lê o número de colunas da matriz.

# Inicializa uma lista vazia para armazenar a matriz
matriz_numeros = []

# Preenche a matriz com os números fornecidos pelo usuário
for i in range(linhas):  # Itera sobre cada linha da matriz
    linha = []  # Cria uma nova lista para armazenar os números da linha atual
    matriz_numeros.append(linha)  # Adiciona a nova linha à matriz
    for j in range(colunas):  # Itera sobre cada coluna da linha atual
        numero = int(input(f"Digite o número da posição ({i},{j}):"))  # Solicita o número para a posição (i, j)
        linha.append(numero)  # Adiciona o número à linha

# Imprime a matriz completa
for i in matriz_numeros:  # Itera sobre cada linha da matriz
    print(i)  # Imprime a linha atual

print('*' * 40)  
