import os
os.system('cls')  # Limpa a tela do terminal no Windows. No Linux ou macOS, você usaria 'clear'.

print('*' * 40)  

# Comando de repetição while crescente

count = 1  # Inicializa a variável `count` com 1

while count <= 100:  # Loop que continua enquanto `count` for menor ou igual a 100
    if count == 51:  # Verifica se `count` é igual a 51
        break  # Sai do loop se `count` for 51
    count += 1  # Incrementa `count` em 1 a cada iteração
    
print('*' * 40)  
