# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества.
# m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

n = int(input("количество элементов"))
m = int(input("количество элементов"))
n1 = set()
m1 = set()
for i in range(n):
    x = int(input("Введите числа: "))
    n1.add(x)
for i in range(m):
    y = int(input("Введите числа: "))
    m1.add(y)

u = sorted(n1.intersection(m1))
print(u)


