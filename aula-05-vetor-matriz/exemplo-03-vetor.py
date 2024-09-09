import os
os.system('cls')  # Limpa a tela do terminal no Windows. Em sistemas Linux ou macOS, use 'clear'.

print('*' * 40)     

# Exemplo de separação de uma string em palavras
# O método 'split()' divide a string em uma lista de palavras com base nos espaços.

frase = "Vetor separado por espaço"  # Define uma string chamada 'frase' com várias palavras separadas por espaços.
palavras = frase.split()  # Usa o método 'split()' para dividir a string 'frase' em uma lista de palavras, separadas por espaços.
print(palavras)  # Exibe a lista de palavras resultante da separação.

# Exemplo de vetor com números sem determinar o tamanho
# A string 'numeros' é separada em uma lista de números usando o método 'split()'.

numeros = "10 20 30 50 70 40"  # Define uma string chamada 'numeros' com vários números separados por espaços.
vetor = numeros.split()  # Usa o método 'split()' para dividir a string 'numeros' em uma lista de strings, cada uma representando um número.
print(vetor)  # Exibe a lista de números resultante da separação. Note que os números ainda estão como strings.

print('*' * 40)  
