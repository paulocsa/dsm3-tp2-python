import os 
os.system('cls')  # Limpa a tela do terminal no Windows. No Linux ou macOS, você usaria 'clear'.

print('*' * 40)  

# Usando for com listas pré-definidas

lista = ["Mauricio", "Luiz", "Max", "Ruth", "Augusto"]  # Lista de nomes

for i in lista:  # Loop que itera sobre cada nome na lista
    if len(i) != 4:  # Verifica se o comprimento do nome não é 4
        continue  # Se o nome não tem 4 letras, pula para a próxima iteração do loop
    print(f"Você encontrou nome com 4 letras {i}")  # Imprime o nome com 4 letras
    
    if i == "Ruth":  # Verifica se o nome é "Ruth"
        break  # Se for "Ruth", sai do loop
    print("Tchau")  # Imprime "Tchau" se o nome não for "Ruth"

print('*' * 40)  
