# Задача No9. Решение в группах
# По данному целому неотрицательному n вычислите
# значение n!. N! = 1 * 2 * 3 * ... * N (произведение всех
# чисел от 1 до N) 0! = 1 Решить задачу используя цикл
# while
# Input: 5
# Output: 120

n = int(input('Input num: '))
fact = 1
if n == 1:
    print(n)
else:    
    while n > 0:
        fact *= n
        n -= 1   
print(fact)    