base = float(input("Digite o valor da base: "))  # Solicita ao usuário que digite o valor da base e o converte para float
altura = float(input("Digite o valor da altura: "))  # Solicita ao usuário que digite o valor da altura e o converte para float
area = (base * altura) / 2  # Calcula a área do triângulo usando a fórmula (base * altura) / 2

# Para arredondar o valor para duas casas decimais, utilizamos :.2f
print(f"O valor da área é de: {area:.2f} cm²")  # Exibe o valor da área arredondado para duas casas decimais
