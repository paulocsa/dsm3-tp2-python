import os
os.system('cls' if os.name == 'nt' else 'clear')

print('*' * 40)

print("1. Pagamento à vista - 10% de desconto")
print("2. Pagamento em 2x - 5% de desconto")
print("3. Pagamento em 3x ou mais - Sem desconto")

opcao = int(input("Escolha a forma de pagamento: "))

preco_total = float(input("Digite o preço total da compra: R$ "))

match opcao:
    case 1:
        desconto = 0.10
        valor_final = preco_total * (1 - desconto)
        print(f"Você escolheu pagamento à vista.")
        print(f"Desconto aplicado: 10%")
        
    case 2:
        desconto = 0.05
        valor_final = preco_total * (1 - desconto)
        print(f"Você escolheu pagamento em 2x.")
        print(f"Desconto aplicado: 5%")
        
    case 3:
        desconto = 0.0
        valor_final = preco_total
        print(f"Você escolheu pagamento em 3x ou mais.")
        print(f"Sem desconto aplicado.")
        
    case _:
        print("Escolha inválida!")
        exit()

print(f"\nPreço total da compra: R$ {preco_total:.2f}")
print(f"Valor final a ser pago com desconto: R$ {valor_final:.2f}")

print('*' * 40)
