n = int(input("Введите трехзначное число: "))
res = 0
a = n % 10
b = n // 10 % 10
c = n // 100
res = a + b + c
print(f"{res} = {c} + {b} + {a}")