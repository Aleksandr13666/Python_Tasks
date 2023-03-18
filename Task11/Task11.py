# Задача No11. Решение в группах
# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6

n = int(input('Input a digit fib: '))
a = 0
b = 1
counter = 1
while(a <= n):
    print(a)
    if n == a:
        print(f"digit is on {counter} position")
        break
    elif n < a:
            print("Digit is not exist")
    else:
        a, b = b, a + b
        counter += 1        
        