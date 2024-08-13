n1 = float(input("Digite o número 1: "))
n2 = float(input("Digite o número 2: "))

if n1 == 0 or n2 == 0:
    print("Não é possível dividir por zero.")
    exit()

if n1 > n2:
    menor = n2
    maior = n1
else:
    menor = n1
    maior = n2

divisao = maior / menor

print(f"A divisão do maior número ({maior}) pelo menor número ({menor}) é {divisao:.2f}")
