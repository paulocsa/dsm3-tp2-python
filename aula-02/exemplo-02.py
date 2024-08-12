print("REsponda 1-sim 0-não \n Empréstimo")

negativo = int(input("Possui o nome negativo:"))

if negativo == 1:
    print("Nao pode fazer emprestimo")
else:
    carteira_assinada = int(input("Possui carteira assinada:"))
    if carteira_assinada == 0:
        print("Nao pode fazer emprestimo")
    else:
        casa_propria = int(input("Possui casa propria:"))
        if casa_propria == 0:
            print("Não pode fazer emprestimo")
        else:
            print("Conceder emprestimo")
            