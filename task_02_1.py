# ЗАДАЧА
# Искусственный интеллект Антон, созданный Гилфойлом, взломал сеть умных холодильников.
# Теперь он использует их в качестве серверов "Пегого дудочника".
# Помогите владельцу фирмы отыскать все зараженные холодильники.
# Для каждого холодильника существует строка с данными, состоящая из строчных букв и цифр,
# и если в ней присутствует слово "anton" (необязательно рядом стоящие буквы, главное наличие
# последовательности букв), то холодильник заражен и нужно вывести номер холодильника,
# нумерация начинается с единицы
# Формат входных данных
# В первой строке подаётся число п - количество холодильников. 
# В последующих п строках вводятстроки, содержащие латинские строчные буквы и цифры,
# в каждой строке от 5 до 100 символов.
# Формат выходных данных
# Программа должна вывести номера зараженных холодильников через пробел.
# Если таких холодильников нет, ничего выводить не нужно.

# Sample Input 1: (перевод: Пример Ввода 1)
# 6
# 222anton456
# a1n1t1o1n1
# 0000a0000n00t00000o000000n
# gylfole
# richard
# ant0n

# Sample Output 1: (перевод: Пример Вывода 1)
# 1 2 3

# РЕШЕНИЕ
# # 1 вариант
# list = ['222anton456', 'a1n1t1o1n1',
#         '0000a0000n00t00000o000000n', 'gylfole', 'richard', 'ant0n']
# print(list)
# for i in list:
#     if 'a' in i:
#         if 'n' in i:
#             if 't' in i:
#                 if 'o' in i:
#                     if 'n' in i:
#                         print(list.index(i) + 1)

# РЕШЕИЕ
# # 2 вариант
# n = int(input())
# list1 = []
# for i in range(n):
#     a = input()
#     if 'a' in a:
#         a = a[a.find('a'):]
#         if 'n' in a:
#             a = a[a.find('n'):]
#             if 't' in a:
#                 a = a[a.find('t'):]
#                 if 'o' in a:
#                     a = a[a.find('o'):]
#                     if 'n' in a:
#                         list1.append(i + 1)
# print(*list1)


# ЗАДАЧА
# Sample Input 2:
# 9
# osfjwoiergwoignaewpjofwoeijfnwfonewfoignewtowenffnoeiwowjfninoiwfen
# anton
# aoooooooooontooooo
# elelelelelelelelelel
# ntoneeee
# tonee
# 253235235a5323352n25235352t253523523235oo235523523523n
# antoooooooooooooooooooooooooooooooooooooooooooooooooooon
# unton
# Sample Output 2:
# 1 2 7 8

# Sample Input 3:
# 1
# anton

# Sample Output 3:
# 1

# Перевод:
# Пример ввода 3:
# 1
# антон

# Пример вывода 3:
# 1

# РЕШЕИЕ:
# list = ['osfjwoiergwoignaewpjofwoeijfnwfonewfoignewtowenffnoeiwowjfninoiwfen', 'anton',
#         'aoooooooooonooooo', 'elelelelelelelelelel', 'ntoneeee', 'tonee', '253235235a5323352n25235352t253523523235oo235523523523n', 'antoooooooooooooooooooooooooooooooooooooooooooooooooooon', 'unton']
# print(list)
# for i in list:
#     if 'a' in i:
#         if 'n' in i:
#             if 't' in i:
#                 if 'o' in i:
#                     if 'n' in i:
#                         print(list.index(i) + 1)








# ЗАДАЧА
# Орел и решка
# Дана строка текста, состоящая из букв русского алфавита "О" и "Р".
# Буква "О" - соответствует выпадению Орла,
# а буква "Р" - соответствует выпадению Решки.
# Напишите программу, которая подсчитывает наибольшее количество подряд выпавших Решек.
# Формат входных данных
# На вход программе подается строка текста, состоящая из букв русского алфавита "О" и "Р".
# Формат выходных данных Программа должна вывести наибольшее количество подряд выпавших Решек.
# Примечание. Если выпавших Решек нет, то необходимо вывести число 0.
# Тестовые данные
# Sample Input 1:
# Sample Output 1:
# 3
# Sample Input 2:
# ООООООРРРОРОРРРРРРР
# Sample Output 2:
# 7

# РЕШЕНИЕ
# 1 вариант
# a = ['ООООООРРРОРОРРРРРРР']
# max = 0
# for i in range(len(a)):
#     count = 0
#     if a[i] == 'P':
#         count += 1
#         if count > max:
#             max = count
# print(max)

# РЕШЕИЕ
# # 2 вариант
# s = input()
# t = 0
# while 'P' * (t + 1) in s:
#     t += 1
# if t != 0:
#     print (t)
# else:
#     print = (0)

# # 3 вариант
# list_eagle = list(input().split('О'))
# print(len(max(list_eagle)))

# # 4 вариант
# print(len(max(list(input().split('О')))))


# # ЗАДАЧА 1. Напишите программу, которая принимает на вход число N
# # и выдаёт последовательность из N членов.
# # *Пример: *
# # - Для N = 5: 1, -3, 9, -27, 81

# # РЕШЕНИЕ 1. Закономерность для известного количества чисел последовательности.
# number_n = int(input('Введите число n: '))
# for i in range(number_n):
#     print((-3) ** i, end = ' ')


# # ЗАДАЧА 2. Напишите программу, в которой пользователь будет задавать две строки,
# # а программа - определять количество вхождений одной строки в другой

# # РЕШЕНИЕ. 1 вариант
# string_1 = input()
# string_2 = input()
# if string_1 > string_2:
#     print(string_1.count(string_2))
# else:
#     print(string_2.count(string_1))
# # В Терминале вводим, например, ааапроллщщщщаааггшщщщщиитаааыыве, нажимаем Enter
# # затем вводим ааа, нажимаем Enter
# # Получаем ответ: 3 (т.е. три раза встречается ааа в первой строке)


# # # РЕШЕНИЕ. 2 вариант
# a ='pyt'
# b = 'pythonpythonpython'
# count = 0
# for i in range(0, len(b) - len(a)):
#     if b[i:i + len(a)] == a:
#         count += 1
# print(count)
