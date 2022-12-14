# Напишите программу, которая принимает 5 чисел
# и находит максимальное из них.
# -1, 4, 8, 7, 5 -> 8
# -78, 55, 36, 90, 2 -> 90

# Берём из 2 способа и соединяем:
# num = [int(i) for i in input().split()]
# print(max_num)


## 3 СПОСОБ:

print(max([int(i) for i in input().split()]))

# В Терминале должно получиться так:
# -78 55 36 90 2 (вводим 5 чисел, затем Enter)
# 90             (автоматически находится максимальное число)