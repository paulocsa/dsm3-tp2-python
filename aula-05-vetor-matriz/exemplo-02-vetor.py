import os
os.system('cls')  # Limpa a tela do terminal no Windows. No Linux ou macOS, você usaria 'clear'.

print('*' * 40)  

# Exemplo de vetor para definir o tamanho do vetor
tamanho = int(input("Digite o tamanho do vetor: "))  # Solicita ao usuário o tamanho do vetor e converte a entrada para um número inteiro.

vetor = []  # Inicializa uma lista vazia para armazenar os elementos do vetor.

# Loop para preencher o vetor com a quantidade de elementos definida pelo usuário
for i in range(tamanho):
    elemento = int(input(f"Digite o elemento {i+1}° do vetor "))  # Solicita ao usuário que insira os elementos um por um, com base no índice.
    vetor.append(elemento)  # Adiciona cada elemento digitado pelo usuário à lista 'vetor'.
    
print(f"Vetor {vetor} ")  # Exibe o vetor completo após a inserção dos elementos.

print('*' * 40)  
