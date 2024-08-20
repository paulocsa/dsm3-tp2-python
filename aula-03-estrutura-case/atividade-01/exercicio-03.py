import os 
os.system('cls')

print('*' * 40)

print("1. Tensão (em Volt) ------------ U = R * i")
print("2. Resistência (em Ohm) ------------ R = U / i")
print("3. Corrente (em Ampére) ------------ i = U / R")

calculo = int(input("Escolha qual grandeza elétrica deseja você deseja calcular:"))

match calculo:
    case 1:
        r = float(input("Digite a resistência (em Ohm)  para calcular a tensão(em Volt):"))
        i = float(input("Digite a Corrente (em Ampére)  para calcular a tensão(em Volt):"))
        u = r * i
        print(f"O cálculo da tensão é: {u}")
        
    case 2:
        u = float(input("Digite a Tensão (em Volt)  para calcular a Resistência (em Ohm):"))
        i = float(input("Digite a Corrente (em Ampére)  para calcular a Resistência (em Ohm):"))
        r = u / i
        print(f"O cálculo da resistencia é: {r}")
        
    case 3:
        u = float(input("Digite a Tensão (em Volt)  para calcular a Corrente (em Ampére):"))
        r = float(input("Digite a Resistência (em Ohm)   para calcular a Corrente (em Ampére):"))
        i = u / r
        print(f"O cálculo da resistencia é: {i}")
        
    case _:
        print("Escolha invalida!")
        exit
        
        
        

print('*' * 40)