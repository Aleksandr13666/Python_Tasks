# Задача 32: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

# После загрузки задания, вы можете проверить себя самостоятельно с помощью эталонного решения


list = [1, 2 ,-3, 6, 5, 9, -5, 7, 2, 1, -9]
min_num = int(input("Введите минимальное число: "))
max_num = int(input("Введите максимальное число: "))

for i in range(len(list)):
    if list[i] >= min_num and list[i] <= max_num:
        print(i)