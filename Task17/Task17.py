# Задача No17. Решение в группах
# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6

import random

my_list = [random.randint(1, 10) for _ in range(random.randint(5, 10))]
print(my_list)
my_set = set(my_list)
print(my_set)
length = len(my_set)
print(length)