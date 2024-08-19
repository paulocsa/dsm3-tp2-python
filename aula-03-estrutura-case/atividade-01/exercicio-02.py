import os 
os.system('cls')

print('*' * 40)

indice_poluicao = int(input("\n De acordo com as classificações, escolha o índice de poluição: \n 0 a 2 - Aceitável \n 3 a 5 - Suspender Atividades Grupo 1 \n 6 a 7 - Suspender Atividades Grupo 1 e 2 \n Acima de 8 - Suspender atividade de todos os grupos \n Digite a classificação:"))

match indice_poluicao:
    case 0 | 1 | 2:
        print("Consideração aceitável.")
    case 3 | 4 | 5:
        print("Suspender Atividades Grupo 1.")
    case 6 | 7:
        print("Suspender Atividades Grupo 1 e 2.")
    case 8 | _ if indice_poluicao > 8:
        print("Suspender atividades de todos os grupos.")
    case _:
        print("Caracter inválido!")

print('*' * 40)
