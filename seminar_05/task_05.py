# # Урок 5. Ускоренная обработка данных:
# # lambda, filter, map, zip, enumerate, list comprehension

# # Задача 1. НОД двух чисел. Объяснение решения задачи:
# # НОД – это математический термин, обозначающий наибольший общий делитель,
# # который может идеально разделить два числа. 
# # НОД также известен как наибольший общий фактор(HCF).
# # Например, HCF / GCD двух чисел 54 и 24 равен 6.
# # Поскольку 6 – это наибольший общий делитель, который полностью делит 54 и 24.
# # Разберемся как найти НОД двух чисел в Python. Умножим:
# # 24 = 2 X 2 X 2 X 3
# # 60 = 2 X 2 X 3 X 5
# # НОД = Умножение общих коэффициентов
# # = 2 X 2 X 3
# # = 12

# # Решение 1.1. НОД двух чисел.
# a = 678
# b = 9
# while a != b:
#     if a > b:
#         a -= b
#     else:
#         b -= a
# print(a)
# # в Терминале ответ:
# # 3


# # Решение 1.2. НОД двух чисел.
# a = 678
# b = 9
# while b != 0:
#     a, b = b, a % b
# print(a)
# # в Терминале ответ:
# # 3


# # Задача 2. Объявите анонимную (лямбда) функцию для определения вхождения 
# # в переданную ей строку фрагмента "plr".
# # То есть, функция должна возвращать True, если такой фрагмент
# # присутствует в строке и False - в противном случае.

# contains = lambda s, sample = 'ra': sample in s
# s = input()
# print(contains(s))
# # если в Терминале вводим слово, например, fds ответ будет - Ложь:
# # fds
# # False

# # если в Терминале вводим слово, например, tratata ответ будет - Истина:
# # tratata
# # True


# # Задача 3. В файле находится N натуральных чисел, записанных через пробел.
# # Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1].
# # Найдите это число.

# # Решение 3.1.
# with open('text_5_3.txt', 'r') as n:
#     lst = [int(i) for i in n.readline().split()]
#     for i in range(1, len(lst)):
#         if lst[i] - lst[i - 1] > 1:
#             print(lst[i] - 1)

# # в файле (text_5_3.txt) написать, например 1 2 3 5 7 9
# # 1 2 3 5 7 9
# # в Терминале программа найдёт недостающие цифры:
# # 4
# # 6
# # 8


# # Решение 3.2.
# def find_num(lst):
#     for i in range(1, len(lst)):
#         if lst[i] - lst[i - 1] > 1:
#             return i, lst[i] - 1
#     return -1, -1
# 
# 
# with open("text_5_3.txt", "r") as fin:
#     lst = [int(i) for i in fin.readline().split()]
#     print(lst)
#     pos, num = find_num(lst)
#     print(pos, num)
#     if (pos != -1):
#         lst.insert(pos, num)
#     print(lst)
# # в Терминале программа найдёт недостающие цифры:
# # [1, 2, 3, 5, 7, 9]
# # 3 4
# # [1, 2, 3, 4, 5, 7, 9]



# Задача 4. Напишите программу, удаляющую из текста все слова, содержащие "абв".
# Решение 1.

# with open("words_5_4.txt", "r") as fin:
#     for line in fin:
#         words = line.split()
#         for word in words:
#             if "абв" in word:
#                 words. remove(word)
#         sentence = " ".join(words)
#         print(sentence)
# Пишем в файле (words_5_4.txt):
# Напишите абв программу, абв удаляющую абв из абв текста абв все слова, абв  содержащие "абв".
# в Терминале ответ:
# Напишите программу, удаляющую из текста все слова, содержащие


# Задача 4. Напишите программу, удаляющую из текста все слова, содержащие "абв".
# Решение 2.

txt = input("Введите текст через пробел:\n")
find_txt = "абв"
lst = [i for i in txt.split() if find_txt not in i]
print(f'Результат: {" ".join(lst)}')

# в Терминале:
# Введите текст через пробел:
# Напишите абв программу, абв для абв этой абв задачи.
# Результат: Напишите программу, для этой задачи.
