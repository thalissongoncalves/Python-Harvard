from random import choice
from random import randint
from random import shuffle

# .choice serve para retornar aleatoriamente um valor dos valores dentro da lista, 50/50
coin = choice(["heads", "tails"])
print(coin)

# .randint serve para retornar um número inteiro aleatório entre os valores definidos no args da function
number = randint(1, 10)
print(number)

# .shuffle serve para embaralhar uma lista
cards = ["jack", "queen", "king"]
shuffle(cards)
for card in cards:
    print(card)