# Solicita ao usuário que responda às perguntas para determinar a elegibilidade para o empréstimo
print("Responda 1-sim 0-não \n Empréstimo")  

# Pergunta se o usuário possui nome negativo e converte a resposta para inteiro
negativo = int(input("Possui o nome negativo:"))

# Se a resposta for 1 (sim, possui nome negativo), não pode fazer empréstimo
if negativo == 1:  
    print("Não pode fazer empréstimo")  
else:
    # Pergunta se o usuário possui carteira assinada e converte a resposta para inteiro
    carteira_assinada = int(input("Possui carteira assinada:"))
    
    # Se a resposta for 0 (não possui carteira assinada), não pode fazer empréstimo
    if carteira_assinada == 0:  
        print("Não pode fazer empréstimo")  
    else:
        # Pergunta se o usuário possui casa própria e converte a resposta para inteiro
        casa_propria = int(input("Possui casa própria:"))
        
        # Se a resposta for 0 (não possui casa própria), não pode fazer empréstimo
        if casa_propria == 0:  
            print("Não pode fazer empréstimo")  
        else:
            # Se todas as condições foram satisfeitas, exibe que o empréstimo pode ser concedido
            print("Conceder empréstimo")  
