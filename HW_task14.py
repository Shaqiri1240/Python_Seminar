# Требуется вывести все целые степени двойки (т.е. числа
# вида 2k
# ), не превосходящие числа N.
# 10 -> 1 2 4 8

n = int(input("Введите число: "))
k = 0
i = 0
while n >= 2**k:
    print(2**k)
    k += 1
