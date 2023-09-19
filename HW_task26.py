# Напишите рекурсивную функцию sum(a, b), возвращающую
# сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.
# Функция не должна ничего выводить, только возвращать значение.

def power(a,b):
    if b == 0:
        return 1
    return power(a,b - 1) * a
a = int(input("Enter a: "))
b = int(input("Enter b: "))
print(power(a,b))