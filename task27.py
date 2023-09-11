string = input("Введите фразу")
string = string.upper()
word_list = string.split()
count = len(set(word_list))
print(count)

# print(len(set(input("Введите текст: ").lower().split()))) В одну строку.