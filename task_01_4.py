# Напишите программу, которая будет принимать на вход дробь
# и показывать первую цифру дробной части числа.
# Примеры:
# 6.78 -> 7
# 5 -> Нет
# 0.34 -> 3 

## Способ 1

# num = float(input('Введите число: '))
# number = num * 10
# if int(number % 10) == 0:
#     print('Нет') 
# else:
#     print(int(number % 10))


## Способ 2

d = 6.78
d1 = int((d * 10) % 10)
print(d1) 

# В Терминале должно получиться так: 
# После нажатия на "запуск", сразу будет результат: 7
