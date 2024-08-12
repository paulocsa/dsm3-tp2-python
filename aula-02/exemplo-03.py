num1 = int(input("Digite o numero 1:"))
num2 = int(input("Digite o numero 2:"))
num3 = int(input("Digite o numero 3:"))

if num1 == num2 or num2 == num3 or num1 == num3:
    exit()
elif num1 > num2 and num1 > num3:
    print("O primerio numero é maior")
elif num2 > num1 and num2 > num3:
    print("O segundo numero é maior")
elif num3 > num1 and num3 > num2:
    print("O terceiro numero é maior")