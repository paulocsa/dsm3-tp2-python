salario_atual = float(input("Digite o salário atual: "))
percentual_reajuste = float(input("Digite o percentual de reajuste em porcentagem:  "))

reajuste = salario_atual * (percentual_reajuste / 100)


novo_salario = salario_atual + reajuste

print(f"O novo salario com reajuste é: {novo_salario}")