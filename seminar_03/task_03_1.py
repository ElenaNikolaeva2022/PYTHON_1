# # Создать текстовый файл, записать в него построчно данные,
# # которые вводит пользователь.
# # Окончанием ввода пусть служит пустая строка.

# fname = input('файл')
# f = open(fname, 'w')
# while True:
#     s = input()
#     if s == '':
#         break
# f.write(s + '\n')
# f.close()           # а .append нужен для перехода на следующую итерацию

# # в Трминале:
# # появиться слово Файл написать слово text3_1 Enter
# # 1 Enter
# # 2 Enter
# # 3 Enter
# #  в файле text3_1 должны появиться цифры в столбик 1 2 3




# # В текстовом файле посчитать количество строк, а также для каждой отдельной строки
# # определить количество в ней символов и слов.
# f = open('text3_2.txt', 'r')
# countLines = 0
# countwordsInLines = []
# countCharsInLines = []
# for line in f:
#     countLines += 1
#     if line != '\n':
#         countwordsInLines.append(line.count(' ') + 1)
#     else:
#         countwordsInLines. append(0)
#     countCharsInLines.append(line.count('') - 2)
# f. close()
# print(countLines)
# print(countwordsInLines)
# print(countCharsInLines)

# # в Трминале:
# # 7                         # количесто строк
# # [1, 1, 0, 2, 7, 5, 2]     # количество слов в строке
# # [7, 5, 0, 11, 31, 9, 15]  # количество симвлов в строке




