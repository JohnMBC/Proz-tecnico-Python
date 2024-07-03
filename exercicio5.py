import random

#Crie duas listas de 10 números cada como number aleatórios,
#gere uma terceira lista onde cada elemento vai ser a somátoria
#da posião das duas listas

lista1 = [random.randint(1, 10) for _ in range(10)]
lista2 = [random.randint(1, 10) for _ in range(10)]

# Gere uma terceira lista onde cada elemento será a soma das posições das duas listas
lista3 = [lista1[i] + lista2[i] for i in range(10)]

print(lista3)


 
 