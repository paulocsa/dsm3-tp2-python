altura_parede = float(input("Digite a altura da parede:"))
largura_parede = float(input("Digite a largura da parede:"))
altura_azulejo= float(input("Digite a altura do azulejo:"))
largura_azulejo = float(input("Digite a largura do azulejo:"))

area_parede = (largura_parede * altura_parede)
area_azulejo = (largura_azulejo*altura_azulejo)


total_azulejos = (area_parede * area_azulejo)/2


print(f"Você precisará de {total_azulejos:.0f} azulejos para cobrir a parede.")

