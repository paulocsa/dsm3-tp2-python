from math import pi  # Importa a constante pi do módulo math

# Exemplo de uso da constante pi
raio = float(input("Digite o valor do raio: "))  # Solicita ao usuário que digite o valor do raio e o converte para float
area = pi * (raio ** 2)  # Calcula a área do círculo usando a fórmula pi * raio^2

print(f"A área do círculo é: {area:.2f}")  # Exibe a área do círculo arredondada para duas casas decimais
