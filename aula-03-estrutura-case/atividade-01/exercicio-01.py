import os 
os.system('cls')


print('*' * 40)

letra = input("Digite uma letra:")

match (letra.lower()):
    case "a" | "e" | "i" | "o" | "u" :
        print(f"A letra {letra} é uma vogal")
        
    
    case _ if letra.isdigit(): 
        print("o caracter digitado é um numero")
        
    case _: 
        print(f"A letra {letra} é uma consoante")        
        
print('*' * 40)
