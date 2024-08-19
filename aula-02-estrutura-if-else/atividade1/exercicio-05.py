custo_fabrica = float(input("Digite o custo da fabricação do carro:"))

perc_distribuidor = 28
perc_imposto = 45

custo_distribuidor = custo_fabrica * (perc_distribuidor / 100)
custo_impostos = custo_fabrica * (perc_imposto / 100)

custo_total = custo_fabrica + custo_distribuidor + custo_impostos

print(f"O custo total da fabricação do carro é de {custo_total}")