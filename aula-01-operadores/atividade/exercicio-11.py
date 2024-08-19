descricao = input("Digite o nome do produto: ")

quantidade = int(input(f"Digite a quantidade de {descricao} comprado(a):"))

precoUn = float(input("Digite o preço unitario do produto:"))

valor_total = precoUn * quantidade

print(f"O valor total da compra de {descricao} é {valor_total}")