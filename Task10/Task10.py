# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.
# 5 -> 1 0 1 1 0
# 2

import random

n = input('input quantity: ')
coins = list()
for i in range(int(n)):
    coins.append(random.randint(0, 1))
print(coins)    
coin_a = 0
coin_b = 0

for i in range(int(n)):
    if (int(n) == 1):
        print('Nothing reverse')
    if (coins[i] == 1):
        coin_a += 1
    if (coins[i] == 0):
        coin_b += 1
print(coin_a if coin_a < coin_b else coin_b) 
                     
        
        