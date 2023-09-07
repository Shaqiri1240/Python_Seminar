length = int(input("Введите кол-во чисел: "))
list_1 = list(map(int, input("Введите числа через пробел: ").split()))
k = int(input("Введите на какое кол-во чисел вы хотите переместить список вправо: "))

list_1 = list_1[-k:] + list_1[:-k]

print(list_1)