import os 
os.system('cls')

print('*' * 40)

categoria = input("Digite a categoria do empregado (A, B ou C): ").upper()

salario_atual = float(input("Digite o salário atual do empregado: R$ "))

if categoria == 'A':
    aumento = 0.10
    salario_com_aumento = salario_atual * (1 + aumento)
    print(f"Categoria: {categoria}")
    print(f"Salário atual: R$ {salario_atual:.2f}")
    print(f"Salário com aumento: R$ {salario_com_aumento:.2f}")

elif categoria == 'B':
    aumento = 0.15
    salario_com_aumento = salario_atual * (1 + aumento)
    print(f"Categoria: {categoria}")
    print(f"Salário atual: R$ {salario_atual:.2f}")
    print(f"Salário com aumento: R$ {salario_com_aumento:.2f}")

elif categoria == 'C':
    aumento = 0.25
    salario_com_aumento = salario_atual * (1 + aumento)
    print(f"Categoria: {categoria}")
    print(f"Salário atual: R$ {salario_atual:.2f}")
    print(f"Salário com aumento: R$ {salario_com_aumento:.2f}")

else:
    print("Categoria inválida! Por favor, insira uma categoria válida (A, B ou C).")

print('*' * 40)
