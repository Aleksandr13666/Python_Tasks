# Задача No25. Решение в группах
# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию
# .split()

letters = "a a a b c a a d c d d"
letters_dict = {}
result = letters.split(" ")
print(letters)
print(letters_dict)
for i in range(len(letters)):
    if lettars_dict.get(letters[i]) == None:
        letters_dict[letters[i]] = 0
        result += f"{letters[i]}"
    else:
        letters_dict[letters[i]] += 1
        result += f"{letters[i]}_{letters_dict[letters[i]]}"
print(result)        