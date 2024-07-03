#Adivinhe o Número: 
#Implemente um jogo em que o programa escolhe um número aleatório e
# o usuário tenta adivinhar qual é.
# O programa deve fornecer dicas (maior ou menor)
# até que o usuário acerte o número.
import random

numero_escolhido = int (input("Digite um numero: "))
numero_automatico = random.randint(1, 10)

maior = (numero_automatico < numero_escolhido)
menor = (numero_escolhido > numero_automatico)

if maior:
    print("O número digitado deve ser menor.")
elif menor:
    print("O número digitado deve ser maior.")
else:
    print("Acertou o número!")
