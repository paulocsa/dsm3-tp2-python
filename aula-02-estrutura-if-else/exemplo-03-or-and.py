# Solicita ao usuário que digite três números e os converte para inteiros
num1 = int(input("Digite o numero 1:"))
num2 = int(input("Digite o numero 2:"))
num3 = int(input("Digite o numero 3:"))

# Se algum dos números for igual a outro, o programa encerra
if num1 == num2 or num2 == num3 or num1 == num3:
    exit()

# Se o primeiro número for maior que os outros dois, exibe uma mensagem
elif num1 > num2 and num1 > num3:
    print("O primeiro numero é maior")

# Se o segundo número for maior que os outros dois, exibe uma mensagem
elif num2 > num1 and num2 > num3:
    print("O segundo numero é maior")

# Se o terceiro número for maior que os outros dois, exibe uma mensagem
elif num3 > num1 and num3 > num2:
    print("O terceiro numero é maior")
