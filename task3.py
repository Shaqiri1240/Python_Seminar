a = int(input("Введите кол-во учеников в первом классе: "))
b = int(input("Введите кол-во учеников во втором классе: "))
c = int(input("Введите кол-во учеников в третьем классе: "))
total_desks = 0
total_desks += a // 2 + a % 2
total_desks += b // 2 + b % 2
total_desks += c // 2 + c % 2

print(total_desks)