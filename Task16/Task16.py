# Задача 16:

# Требуется вычислить, сколько раз встречается некоторое число X 
# в массиве A[1..N].
# Пользователь вводит натуральное число N – количество 
# элементов в массиве и число, которое необходимо проверить - X.
# Заполните массив случайными натуральными числами от 1 до N/2.
# Выведите, сколько раз X встречается в массиве.

# Ввод: 5
# Ввод: 1

# 1 2 1 2 2
# Вывод: 2

import random

n = int(input('input number: '))
x = int(input('input find number: '))
nums = list()
count = 0
for i in range(int(n)):
    nums.append(random.randint(1, 9))
print(nums) 
for i in range (len(nums)):
    if nums[i] == x:
        count += 1
print(count)
