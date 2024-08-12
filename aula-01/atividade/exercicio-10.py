from math import pi

raio = float(input("Digite o raio do cilindro:"))
altura = float(input("Digite a altura do cilindro:"))

volume = pi * pow(raio,2) * altura

print(f"O volume do cilindro é:{volume:.2f}")
