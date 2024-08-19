
opcao = int(input("\n 1 - Sacar \n 2 - Extrato \n 3 - Sair \n Escolhar a opção:"))

# estrutura case

match opcao:
    case 1:
        print("Escolheu a opção sacar")
        valor = float(input("DIgite o valor do saque R$:"))
        print(f"Sacando da sua conta o valor de: R$ {valor}...")
    
    case 2:
        print("Escolheu a opção extrato")
        dias = int(input("Digite a quantidade de dias:"))
        print(f"Retirando o extrato de {dias} dias...")
    
    case 3:
        exit
    
    case _:
        print("Opção inválida, digite a opção correta")