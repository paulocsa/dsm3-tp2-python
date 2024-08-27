import os
os.system('cls')  # Limpa a tela do terminal no Windows. No Linux ou macOS, você usaria 'clear'.

print('*' * 40)  

# Exemplo de loop que imprime números de 1 a 100 (comentado)
# for i in range(1, 101):
#     print(i)

total = 0  # Inicializa a variável `total` com 0, que será usada para armazenar a soma dos números

for i in range(1, 101):  # Loop que itera de 1 a 100 (inclusive)
    total += i  # Adiciona o valor de `i` à variável `total` em cada iteração

print(total)  # Imprime o valor final de `total`, que é a soma de todos os números de 1 a 100

print('*' * 40)  
