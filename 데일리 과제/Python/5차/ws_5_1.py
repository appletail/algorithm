# apple,rottenBanana,apple,RoTTenorange,Orange

basket = list(input().split(','))
fruits = []

for fruit in basket:
    fruit = fruit.lower()
    
    if 'rotten' in fruit:
        fruits.append(fruit[6:])
    else:   
        fruits.append(fruit)

print(fruits)
