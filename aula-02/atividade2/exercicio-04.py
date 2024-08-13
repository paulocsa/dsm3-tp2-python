numero = int(input("Digite um numero inteiro:"))

if numero %2 == 0:
    resultado = pow(numero,2)
    t = "par"
else:
    resultado = pow(numero,3)
    t = "impar"

print(f"O número {numero} é {t}")
    