# Задача 8: Требуется определить, можно ли от шоколадки размером 
# n × m долек отломить k долек, если разрешается сделать один 
# разлом по прямой между дольками (то есть разломить шоколадку 
# на два прямоугольника).

# *Пример:*

# 3 2 4 -> yes
# 3 2 1 -> no

x = int(input('Input width of choko: '))
y = int(input('Input length of choko: '))
z = int(input('How many of choko you need: '))
if z < x * y and ((z % x == 0) or (z % y == 0)):
    print('YES')
else:
    print('NO')      