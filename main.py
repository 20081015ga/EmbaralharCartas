import random
  
naipes = ['Ouro', 'Copas', 'Espadas', 'Paus']
numeros = ['ÁS', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
  
cartas = []
  #For para naipes
for i in range (4):
    #for para os numeros 
    for u in range (13):
      cartas.append (str(numeros[u])+" de "+naipes[i])

    quantidade = int(input("Digite a quantidade de cartas:"))

random.shuffle(cartas)
for i in range (quantidade):
    print(cartas[i])