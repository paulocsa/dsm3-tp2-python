import os
os.system('cls')  # Limpa a tela do terminal no Windows. No Linux ou macOS, você usaria 'clear'.

print('*' * 40)  

# Comando while de forma decrescente

count = 300  # Inicializa a variável `count` com 300

while count >= 0:  # Loop que continua enquanto `count` for maior ou igual a 0
    print(count)  # Imprime o valor atual de `count`
    count -= 1  # Decrementa `count` em 1 a cada iteração
    
print('*' * 40)  
