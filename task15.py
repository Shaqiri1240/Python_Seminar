n = int(input("Введите кол-во арбузов: "))
x = int(input("Введите массу арбуза: "))
min_mass = x
max_mass = x
for i in range(n-1):
    x = int(input("Введите массу арбуза: "))
    if min_mass > x:
        min_mass = x
    elif max_mass < x:
        max_mass = x
print(f"Минимальная масса {min_mass} и Максимальная масса {max_mass}")
