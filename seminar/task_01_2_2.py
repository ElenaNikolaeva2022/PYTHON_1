# Напишите программу, которая принимает 5 чисел
# и находит максимальное из них.
# -1, 4, 8, 7, 5 -> 8
# -78, 55, 36, 90, 2 -> 90


# 2 СПОСОБ:

num = [int(i) for i in input().split()] # Сначала инициализируем список.
print(max(num))                         # Затем находим максимальный элемент.

# В Терминале должно получиться так:
# -78 55 36 90 2 (вводим 5 чисел, затем Enter)
# 90             (автоматически находится максимальное число)