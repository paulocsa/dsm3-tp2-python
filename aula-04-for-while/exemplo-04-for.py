import os 
os.system('cls')  # Limpa a tela do terminal no Windows. No Linux ou macOS, você usaria 'clear'.

print('*' * 40)  

# Usando for com listas pré-definidas

frutas = ["Maçã", "Banana", "Mamão", "Laranja"]  # Lista de frutas
localizar = "Laranja"  # Fruta que queremos localizar na lista

for i in frutas:  # Loop que itera sobre cada fruta na lista
    if i == localizar:  # Verifica se a fruta atual é a que estamos procurando
        print(f"Encontrou a fruta {localizar}")  # Imprime mensagem indicando que a fruta foi encontrada
        break  # Sai do loop se a fruta for encontrada
    else:
        print(f"{localizar}, fruta não encontrada")  # Imprime mensagem indicando que a fruta não foi encontrada

print('*' * 40)  
