import os 
os.system('cls')

print('*' * 40)

print("1. À vista (em espécie) - 15% de desconto")
print("2. Cartão de débito - 10% de desconto")
print("3. Cartão de crédito (vencimento) - 5% de desconto")

opcao = int(input("Escolha a condição de pagamento (1, 2 ou 3): "))

preco_total = float(input("Digite o preço total da compra: R$ "))

match opcao:
    case 1:
        desconto = 0.15
        valor_final = preco_total * (1 - desconto)
        print(f"Você escolheu pagamento à vista.")
        print(f"Desconto aplicado: 15%")
        
    case 2:
        desconto = 0.10
        valor_final = preco_total * (1 - desconto)
        print(f"Você escolheu pagamento com cartão de débito.")
        print(f"Desconto aplicado: 10%")
        
    case 3:
        desconto = 0.05
        valor_final = preco_total * (1 - desconto)
        print(f"Você escolheu pagamento com cartão de crédito (vencimento).")
        print(f"Desconto aplicado: 5%")
        
    case _:
        print("Escolha inválida!")
        exit()

print(f"\nPreço total da compra: R$ {preco_total:.2f}")
print(f"Valor final a ser pago com desconto: R$ {valor_final:.2f}")

print('*' * 40)
