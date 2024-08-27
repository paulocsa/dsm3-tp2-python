# Solicita ao usuário que digite a primeira nota e a converte para float
nota1 = float(input("Digite a nota 1:"))

# Solicita ao usuário que digite a segunda nota e a converte para float
nota2 = float(input("Digite a nota 2:"))

# Calcula a média das duas notas
media = (nota1 + nota2) / 2

# Estrutura condicional if para determinar a situação do aluno
if media > 5:  # Se a média for maior que 5
    print("Aprovado")  # Exibe "Aprovado"
elif media >= 2 and media < 5:  # Se a média estiver entre 2 (inclusive) e 5 (exclusivo)
    print("Aluno de exame")  # Exibe "Aluno de exame"
else:  # Caso contrário (média menor que 2)
    print("Aluno reprovado")  # Exibe "Aluno reprovado"
