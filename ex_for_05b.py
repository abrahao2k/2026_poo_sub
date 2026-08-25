import random

cartoes = int(input("Quantos cartões? "))

for x in range(cartoes):
    
    print(sorted(random.sample(range(1,61), 6)))

