import os
os.system('cls')  # Limpa a tela do terminal no Windows. Em sistemas Linux ou macOS, use 'clear'.

print('*' * 40)  

# Define uma matriz 3x3 usando listas
matriz = [
    [1, 2, 3],  # Linha 1 da matriz
    [4, 5, 6],  # Linha 2 da matriz
    [7, 8, 9]   # Linha 3 da matriz
]

# Acessa e imprime o elemento da primeira linha e primeira coluna
print(f"Elemento da primeira linha e primeira coluna {matriz[0][0]}")  # Imprime o elemento na primeira linha e primeira coluna, que é 1.

# Acessa e imprime o elemento da segunda linha e terceira coluna
print(f"Elemento da segunda linha e terceira coluna {matriz[1][2]}")  # Imprime o elemento na segunda linha e terceira coluna, que é 6.

# Mostra a matriz inteira
for i in matriz:
    print(i)  # Imprime cada linha da matriz, onde 'i' representa cada linha da matriz.

print('*' * 40)  
