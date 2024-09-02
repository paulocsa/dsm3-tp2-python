import os 
os.system('cls')

print('*' * 40)

peso_na_terra = float(input("Digite o seu peso na Terra (em kg): "))

print("Escolha um planeta pelo número correspondente:")
print("1 - Mercúrio")
print("2 - Vênus")
print("3 - Marte")
print("4 - Júpiter")
print("5 - Saturno")

planeta_numero = int(input("Digite o número do planeta: "))

if planeta_numero == 1:
    gravidade_relativa = 0.37
    planeta = "Mercúrio"
elif planeta_numero == 2:
    gravidade_relativa = 0.88
    planeta = "Vênus"
elif planeta_numero == 3:
    gravidade_relativa = 0.38
    planeta = "Marte"
elif planeta_numero == 4:
    gravidade_relativa = 2.64
    planeta = "Júpiter"
elif planeta_numero == 5:
    gravidade_relativa = 1.15
    planeta = "Saturno"
else:
    print("Número do planeta inválido!")
    exit()

peso_no_planeta = peso_na_terra * gravidade_relativa

print(f"Seu peso em {planeta} seria: {peso_no_planeta:.2f} kg")

print('*' * 40)