# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
#  Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества.
#  Затем пользователь вводит сами элементы множеств.

n = int(input('Input quantity first list of numbers: '))
num_list_one = []
for i in range(n):
    num = int(input('Input numbers: '))
    num_list_one.append(num)
print(num_list_one)

m = int(input('Input quatity second list of numbers: '))
num_list_second = []
for i in range(m):
    num = int(input('Input numbers: '))
    num_list_second.append(num)
print(num_list_second)

num_list_third = sorted(num_list_one.intersection(num_list_second))
print(num_list_third)