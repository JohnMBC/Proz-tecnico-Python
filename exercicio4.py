dicionario_traducao = {
    "apple":"maça",
    "orange":"laranja",
    "grape": "uva",
    "banana": "banana",
    "açai": "açaí",
    "acerola": "acerola",
    "avocado": "abacaxi",
    "blackberry": "amora",
    "blueberry": "mirtilo",
    "breadfruit": "fruta-pão",
    
}
print (dicionario_traducao)

original = input("Digite a palavra em inglês: ")
traducao = input("Digite a palavra em ptbr: ")

dicionario_traducao[original] = traducao
print()

busca = input("Digite a palavra que deseja traduzir: ")

if busca in dicionario_traducao:
    traducao_user = dicionario_traducao[busca]
    print(traducao_user)
else:
    print("Palavra não encontrada")
    


print(traducao_user)