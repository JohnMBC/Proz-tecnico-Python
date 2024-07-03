#crie duas listas de 10 números cada com números aleatórios, 
#gere uma terceira lista onde cada elemento, 
#vai ser a somatória da posicão das duas listas 
import random 
list_one = []
list_two = []
list_tree =[]

for i in range (10):
    list_one.append(random.randint(0, 10))
    list_two.append(random.randint(0, 10))
    
for i in range (10):
    list_tree.append(list_one[i] + list_two[i])
    
print(list_one)
print(list_two)
print(list_tree)
    