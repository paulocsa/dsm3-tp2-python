import os
os.system('cls')  

qtdcores = 5

cores = []

for i in range(qtdcores):
    cor = input(f"Digite a {i+1}° cor:")
    cores.append(cor)
print(cores)

