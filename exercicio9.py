# crie uma função calculadora em Python 
# que peça ao usuario para inserir numeros
# inteiros e faça o calculo desses numeros 

def calculadora(numero, outro_numero):
    soma = numero + outro_numero
    subtracao = numero - outro_numero
    multiplicacao = numero * outro_numero
    divisao = numero / outro_numero
    
    return soma, subtracao, multiplicacao, divisao

numero = int(input("Digite um numero: "))
operador = str(input("Digite qual operador: "))
outro_numero = int(input("Digite outro numero: "))
if operador == "+":
    print("o resultado da soma e: {}" .format(numero + outro_numero))
if operador == "-":
    print(calculadora(numero, outro_numero)[1])
if operador == "*":
    print(calculadora(numero, outro_numero)[2])
if operador == "/":
    print(calculadora(numero, outro_numero)[3])
 
else:
    print("Operador invalido")



    
    
    

