votos_brancos = int(input("Digite a quantidade de votos brancos: "))
votos_nulos = int(input("Digite a quantidade de votos nulos: "))
votos_validos = int(input("Digite a quantidade de votos validos: "))


total_eleitores = votos_brancos + votos_nulos + votos_validos

percentual_branco = (votos_brancos * 100)/total_eleitores
percentual_nulos = (votos_nulos * 100)/total_eleitores
percentual_validos = (votos_validos * 100)/total_eleitores

print(f"O percentual de votos brancos foram: {percentual_branco}")
print(f"O percentual de votos nulos foram: {percentual_nulos}")
print(f"O percentual de votos validos foram: {percentual_validos}")

