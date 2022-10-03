# # 1.Напишите программу, удаляющую из текста все слова, 
# # содержащие ""абв"".

# my_text = 'Напишите абв напиабв програбвмму программу, удаляющую из \
#     этого абв текста все вабвс слова, содерабващие содержащие "абв"'

# def del_some_words(my_text):
#     my_text = list(filter(lambda x: 'абв' not in x, my_text.split()))
#     return " ".join(my_text)

# my_text = del_some_words(my_text)
# print(my_text)


# 1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
import re

def remove_words_with_substring(sentence, substring):
    return re.sub(r"\s*[а-яА-Я\w]*" + substring + r"[а-яА-Я\w]*", "", sentence)

print(remove_words_with_substring("Мы неабв очень любим Питон     \n иабв Джавуабв!", "абв"))

