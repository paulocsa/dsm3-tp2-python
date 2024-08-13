rg = input("Digite o RG do empregado: ")
ano_nascimento = int(input("Digite o ano de nascimento: "))
ano_ingresso = int(input("Digite o ano de ingresso na empresa: "))
ano_atual = int(input("Digite o ano atual: "))

idade = ano_atual - ano_nascimento
tempo_trabalho = ano_atual - ano_ingresso

if idade >= 65 or tempo_trabalho >= 30 or (idade >= 60 and tempo_trabalho >= 25):
    print("Requerer Aposentadoria")
else:
    print("Não requerer Aposentadoria")
