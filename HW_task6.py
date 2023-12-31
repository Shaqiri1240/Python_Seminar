# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.

# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.

# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.

# Вам требуется написать программу, которая проверяет счастливость билета с номером n и выводит на экран yes или no.

# Пример:


# n = 385916 -> yes
# n = 123456 -> no

n = int(input("Введите шестизначное число вашего билета: "))
sum_1 = 0
sum_2 = 0
sum_1 += n // 1_000_00
sum_1 += n // 1_000_0 % 10
sum_1 += n // 1_000 % 10
sum_2 += n // 1_00 % 10
sum_2 += n // 1_0 % 10
sum_2 += n % 10
if sum_1 == sum_2:
    print("Yes")
else:
    print("No")