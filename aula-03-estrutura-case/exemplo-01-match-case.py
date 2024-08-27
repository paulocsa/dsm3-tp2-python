# Solicita ao usuário que escolha uma opção entre sacar, extrato e sair
opcao = int(input("\n 1 - Sacar \n 2 - Extrato \n 3 - Sair \n Escolha a opção:"))

# Estrutura condicional match (similar ao switch-case) para tratar a opção escolhida
match opcao:
    case 1:  # Caso o usuário escolha a opção 1 (Sacar)
        print("Escolheu a opção sacar")
        valor = float(input("Digite o valor do saque R$:"))  # Solicita o valor do saque
        print(f"Sacando da sua conta o valor de: R$ {valor}...")  # Exibe a mensagem de saque
    
    case 2:  # Caso o usuário escolha a opção 2 (Extrato)
        print("Escolheu a opção extrato")
        dias = int(input("Digite a quantidade de dias:"))  # Solicita a quantidade de dias para o extrato
        print(f"Retirando o extrato de {dias} dias...")  # Exibe a mensagem de extração do extrato
    
    case 3:  # Caso o usuário escolha a opção 3 (Sair)
        exit()  # Encerra o programa
    
    case _:  # Caso a opção não seja válida
        print("Opção inválida, digite a opção correta")  # Exibe mensagem de erro
