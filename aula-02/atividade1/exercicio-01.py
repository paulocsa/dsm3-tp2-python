salario_fixo = 1500
bonus = 50
softwares_vendidos = int(input("Digite a quantidade de softwares vendidos este mes:"))

salario_total = salario_fixo + (bonus*softwares_vendidos)

print(f"O salario total com {softwares_vendidos} softwares vendidos é de: {salario_total}")