# Задача No3. Решение в группах
# В некоторой школе решили набрать три новых
# математических класса и оборудовать кабинеты для
# них новыми партами. За каждой партой может сидеть
# два учащихся. Известно количество учащихся в
# каждом из трех классов. Выведите наименьшее
# число парт, которое нужно приобрести для них.
# Input: 20 21 22(ввод чисел НЕ в одну строку)
# Output: 32

n1 = int(input('First: '))
n2 = int(input('Second: '))
n3 = int(input('Third: '))

n1 = n1 // 2 + n1 % 2
n2 = n2 // 2 + n2 % 2
n3 = n3 // 2 + n3 % 2
sum = n1 +n2 +n3
print(sum)