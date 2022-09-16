# # ЗАДАЧА 1. Транслитирация вводимого текста.

# lang = {'а': 'a',
#         'б': 'b',
#         'в': 'v',
#         'г': 'g',
#         'д': 'd',
#         'е': 'e',
#         'ё': 'e',
#         'ж': 'zh',
#         'з': 'z',
#         'и': 'i',
#         'й': 'y',
#         'к': 'k',
#         'л': 'l',
#         'м': 'm',
#         'н': 'n',
#         'о': 'o',
#         'п': 'p',
#         'р': 'r',
#         'с': 's',
#         'т': 't',
#         'у': 'u',
#         'ф': 'f',
#         'х': 'kh',
#         'ц': 'ts',
#         'ч': 'ch',
#         'ш': 'sh',
#         'щ': 'shch',
#         'ъ': '',
#         'ы': 'y',
#         'ь': '',
#         'э': 'e',
#         'ю': 'yu',
#         'я': 'ya',
#          ' ': ' '
# }
#
# value = 'Мама мыла раму'
# result = ' '
#
# for i in value:
#         result += lang[i.lower()]
#
# print(result)
#
# # в Терминале будет:
# # mama myla ramu


# # ЗАДАЧА 1. Словарь. от преподавателя
# t = ['a', 'b', 'v', 'g',  'd', 'e', 'e', 'zh', 'z', 'i', 'y', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u','f',
#      'kh', 'ts', 'ch', 'sh', 'shch', '', 'y', '', 'e', 'yu', 'ya', ' ']
#
# start_index = ord('a')
# title = 'Переводим этот текст, сейчас!'
# print(title.lower())
#
# slug = ""
# for s in title.lower():
#     if "а" <= s <= "я":
#         slug += t[ord(s) - ord('а')]
#         print(ord(s) - ord('a'), ord(s), ord('a'))
# #  elif s == "ё":
# #     slug = 'yo'
# #  elif s in " !?;:.,":
# #     slug = "-"
#     else:
#         slug += s
#
# # while slug.count('--'):
# #    slug = slug.replace('--', '-')
#
# print(slug)


# # ЗАДАЧА 2. Задайте строку из набора чисел. Напишите программу,
# # которая покажет большее и меньшее число.
# # В качестве символа-разделителя используйте пробел.
#
# n = '1 2 3 4 5'
# min = int(n[0])
# max = int(n[0])
# for i in n.split(sep = ' '):
#     if int(i) < min:
#         min = int(i)
#     if int(i) > max:
#         max = int(i)
# print(min, max)
# # в Терминале:
# # 1 5
#
# # str = '12 40 0 15'
# # lst = [int(i) for i in str.split()]
# # print(min(lst))
# # print(max(lst))
# # в Терминале:
# # 0
# # 40


# # ЗАДАЧА 3. Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
# # 1) с помощью математических формул нахождения корней квадратного уравнения
# # 2) с помощью дополнительных библиотек Python
#
# def discriminant(a: float, b: float, c: float) -> float:
#     return b ** 2 - 4 * a * c
#
#
# def solve_quadratic(a: float, b: float, c: float) -> str:
#     if a == 0:
#         raise ValueError("Not quadratic equation")
#
#     d = discriminant(a, b, c)
#     if d < 0:
#         return "No roots"
#     elif d == 0:
#         return f"One root x = {-b / (2 * a)}"
#     else:
#         x1 = (-b + d ** 0.5) / (2 * a)
#         x2 = (-b - d ** 0.5) / (2 * a)
#         return f"Two roots: x1 = {x1}, x2 = {2}"
#
# if __name__ == "__main__":
#     print(solve_quadratic(5, -9, -2))
#     print(solve_quadratic(1, -4, 4))
#     print(solve_quadratic(1, -5, 9))
#     print(solve_quadratic(0, 1, 2))


# # ЗАДАЧА 3. Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
# # 1) с помощью математических формул нахождения корней квадратного уравнения
# # 2) с помощью дополнительных библиотек Python
#
# import math
# a = int(input("a= "))
# b = int(input("b= "))
# c = int(input("c= "))
# D = b ** 2 - 4 * a * c
# print(D)
# if D < 0:
#   print("Корней нет")
# elif D == 0:
#   x = -b / 2 * a
#   print (x)
# else:
#   x1 = (-b + math.sqrt(D)) / (2 * a)
#   x2 = (-b - math.sqrt(D)) / (2 * a)
#   print(x1)
#   print(x2)



# ЗАДАЧА 4. Задайте два числа. Напишите программу,
# которая найдёт НОК (наименьшее общее кратное) этих двух чисел.

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
i = min(a, b)
while True:
    if i % a == 0 and i % b == 0:
        break
    i += 1
print(i)

