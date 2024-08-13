
sexo = int(input("Digite o seu sexo (1 - Homem, 2 - Mulher): "))
altura = float(input("Digite sua altura: "))

if sexo == 1:
    peso_ideal = (72.7 * altura) - 58
elif sexo == 2:
    peso_ideal = (62.1 * altura) - 44.7
else:
    print("Erro: Opção de sexo inválida.")
    exit() 

print(f"O seu peso ideal seria: {peso_ideal:.2f}")
