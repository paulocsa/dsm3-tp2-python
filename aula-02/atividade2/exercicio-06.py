num1 = float(input("Digite o primeiro número positivo: "))
num2 = float(input("Digite o segundo número positivo: "))

if num1 <= 0 or num2 <= 0:
    print("Os números devem ser positivos.")
    exit()

print("Escolha uma opção:")
print("1. Média ponderada, com pesos 2 e 3, respectivamente")
print("2. Quadrado da soma dos 2 números")
print("3. Cubo do menor número")

opcao = int(input("Digite a opção escolhida: "))

if opcao == 1:
    media_ponderada = (num1 * 2 + num2 * 3) / (2 + 3)
    print(f"A média ponderada é: {media_ponderada:.2f}")
elif opcao == 2:
    quadrado_soma = (num1 + num2) ** 2
    print(f"O quadrado da soma dos números é: {quadrado_soma:.2f}")
elif opcao == 3:
    menor_numero = min(num1, num2)
    cubo_menor = menor_numero ** 3
    print(f"O cubo do menor número é: {cubo_menor:.2f}")
else:
    print("Opção inválida.")
