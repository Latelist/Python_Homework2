# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

n = 60
p = 2
res = 2

while res <= n:
    print(res)
    res = 2 ** p
    p += 1