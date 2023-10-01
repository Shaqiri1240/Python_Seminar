numbers = [int(i) for i in input("Введите числа: ").split()]
data = {}
for i in numbers:
    if i not in data:
        data[i] = 1 # i: 1
    else:
        data[i] += 1
    print(data)
print(sum([i // 2 for i in data.values()]))