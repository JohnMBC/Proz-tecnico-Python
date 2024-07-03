nome = "Johnny"
sobrenome = "Carvalho"
idade = 35
etnia = "pardo"
crenca = "protestante"

nome_input = str(input("Qual seu nome? "))
sobre_input = str(input("Por favor, Digite seu sobrenome: "))
idade_input = int(input("Qual sua idade? "))
etnia_input = str(input("Qual sua etnia? "))
crenca_input = str(input("Qual sua crença? "))

if  nome_input == nome and sobre_input == sobrenome and idade_input == idade and etnia_input == etnia and crenca_input == crenca:
    print ("Ei {} que nome Lindo vc tem!.".format(nome_input) + " A concatenação do seu nome com seu sobrenome e: {} {}".format (nome_input, sobrenome) +
    " vc tem {} anos, {} e {}".format(idade_input, etnia_input, crenca_input))

elif nome_input == nome and sobre_input != sobrenome:
    print("Eii seu nome é: {}. E é um nome bonito.".format(nome_input))
    print("A concatenação do seu nome com seu sobrenome é: {} {}".format(nome_input, sobre_input))
    print("Mais não está completamente bonito. Você tem {} anos, é da cor {} e professa ser {}.".format(idade_input, etnia_input, crenca_input))

elif nome_input != nome and sobre_input == sobrenome:
    print("Eiii seu nome é: {}. E não é tão bonito.".format(nome_input))
    print("A concatenação do seu nome com seu sobrenome é: {} {}".format(nome_input, sobre_input))
    print("Posso considerar como relativamente bonito. Você tem {} anos, {} e {}".format(idade_input, etnia_input, crenca_input))

else:
    print("Eiiii seu nome é: {}".format(nome_input))
    print("A concatenação do seu nome com seu sobrenome é: {} {}".format(nome_input, sobre_input))
    print("Você tem {} anos, {} e {}".format(idade_input, etnia_input, crenca_input))
    print("Seu nome não é tão bonito, mas é um nome. E não é agradavel(a).")




