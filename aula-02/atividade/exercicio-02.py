valor_prestacao = float(input("Qual o valor da prestação:"))
taxa_juros = float(input("Qual é a taxa de juros:"))
meses_atraso = float(input("Quantos meses estão em atraso:"))

valor_atraso = valor_prestacao +(valor_prestacao*(taxa_juros/100)* meses_atraso)


print(f"O calculo das prestações em atraso é de {valor_atraso}")