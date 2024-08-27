estatura1 = float(input("Digite a estatura da primeira pessoa (em metros): "))
estatura2 = float(input("Digite a estatura da segunda pessoa (em metros): "))
estatura3 = float(input("Digite a estatura da terceira pessoa (em metros): "))

if estatura1 >= estatura2 and estatura1 >= estatura3:
    maior1 = estatura1
    if estatura2 >= estatura3:
        meio = estatura2
        menor = estatura3
    else:
        meio = estatura3
        menor = estatura2
elif estatura2 >= estatura1 and estatura2 >= estatura3:
    maior1 = estatura2
    if estatura1 >= estatura3:
        meio = estatura1
        menor = estatura3
    else:
        meio = estatura3
        menor = estatura1
else:
    maior1 = estatura3
    if estatura1 >= estatura2:
        meio = estatura1
        menor = estatura2
    else:
        meio = estatura2
        menor = estatura1

print(f"As estaturas em ordem decrescente são:")
print(f"{maior1:.2f} metros")
print(f"{meio:.2f} metros")
print(f"{menor:.2f} metros")
