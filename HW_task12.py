#  Петя и Катя – брат и сестра. Петя – студент, а Катя –
# школьница. Петя помогает Кате по математике. Он задумывает два
# натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
# этого Петя делает две подсказки. Он называет сумму этих чисел S и их
# произведение P. Помогите Кате отгадать задуманные Петей числа.
# 4 4 -> 2 2
# 5 6 -> 2 3
s = int(input("Введите сумму: "))
p = int(input("Введите произведение: "))
# s = x + y -> x = s - y
# p = x * y -> p = (s - y) * y -> p = s*y - Y^2 -> y^2 -s*y + p = 0
# В квадратном уравнении ax2 + bx + c = 0
# a = 1
# b = S
# c = p
D = s**2 - 4 * 1 * p
y1 = int((s + D**0.5) / 2*1)
y2 =int((s - D**0.5) / 2*1)
x1 = s - y1
x2 = s - y2

print(y2,x2)
