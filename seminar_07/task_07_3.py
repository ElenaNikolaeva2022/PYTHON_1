# 3. Напишите функцию triangle(a, b, c), которая принимает на вход три длины
# отрезков и определяет, можно ли из этих отрезков составить треугольник.
# Входные данные
# Выходные данные
# triangle(1, 1, 2)
# Это не треугольник
# triangle(7, 6, 10)
# Это треугольник

# 1 вариант.
def triangle(x, y, z):
    return x + y > z and x + z > y and y + z > x

# a = 1
# b = 1
# c = 12

a = 7
b = 6
c = 10

if triangle(a, b, c):
    print('Это треугольник')
else:
    print('Это не треугольник')
# в Терминале получим ответ:
# Это треугольник


# 2 вариант.
a = int(input())
b = int(input())
c = int(input())

if (a + b) > c and (a+c) > b and (b + c) > a:

    print('Это треугольник')
else:
    print('Это не треугольник')

# в Терминале вводим три цифры и получим ответ:
# 7  
# 6 
# 10  
# Это треугольник