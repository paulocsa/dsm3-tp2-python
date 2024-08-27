num = float(input("Digite um número: "))  # Solicita ao usuário que digite um número e o converte para float

potencia = pow(num, 2)  # Calcula a potência do número elevado ao quadrado usando a função `pow`
potencia2 = num ** num  # Calcula a potência do número elevado a ele mesmo usando o operador `**`

print(f"O valor da potência é {potencia}")  # Exibe o valor da potência elevada ao quadrado
print(f"O valor da potência é {potencia2}")  # Exibe o valor da potência elevada a ele mesmo
