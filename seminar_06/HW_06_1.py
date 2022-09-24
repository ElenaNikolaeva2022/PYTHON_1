# # 1. Дана последовательность чисел.
# # Получить список уникальных элементов заданной последовательности.
# # Пример:
# # [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]

# a = [1, 2, 3, 5, 1, 5, 3, 10]
# res = [x for x in a if a.count(x) == 1]

# print(res)

# =================================================================================

# # 2. Задание
# # Формат: На семинаре и в лекциях мы разобрали новые функции,
# # которые позволяют улучшить код прошлых задач.
# # Задача: предложить улучшения кода для уже решённых задач
# # (не менее 4 задач нужно улучшить):
# # С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension
# # В этом случае можно пропустить совсем тривиальные
# # (т.е. задачу 1 или 2 тут точно решать не имеет смысла) - исходите из уровня группы и студента.


# # 1. lambda, filter, map, list comprehension.

def filter(numbers, function):
    result = []
    for number in numbers:
        if function(number):
            result.append(number)
    return result


numbers = [1, 2, 3, 4, 5, 6, 7, 8]

# для чётных чисел
print(filter(numbers, lambda number: number % 2 == 0))

# для нечётных чисел
print(filter(numbers, lambda number: number % 2 != 0))

# список квадратов чисел
print(list(map(lambda x: x**2, numbers)))

# привести числа к строке
print(list(map(lambda x: str(x), numbers)))

# =================================================================================

# # list comprehension

# def f(x):
#     return x ** 3

# list = [(i, f(i)) for i in range(1, 13) if i % 2 == 0]
# print(list)

# =================================================================================

# Распределение победителей по занятым местам.

# enumerate
winners = ['Alex', 'Max', 'Kate']
for number, winner in enumerate(winners, 1):
    print(number, winner)


# zip
number = [1, 2, 3]
data = list(zip(winners, number))
print(data)

# =================================================================================

# # filter

# # Найти чётные числа.
# # 1. Решение с функцией filter

# numbers = (1, 2, 3, 4, 5, 6, 7, 8)

# def is_even(number):
#     return number % 2 == 0

# result = filter(is_even, numbers)
# print(result)
# result = list(result)
# print(result)


# # 2. Решение c функцией lambda
# print(list(filter(lambda number: number % 2 == 0, numbers)))

# =================================================================================
