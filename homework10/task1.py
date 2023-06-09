# Напишите генератор generate_random_name(), используя модуль random,
# который генерирует два слова из латинских букв от 1 до 15 символов, разделенных пробелами
# Например при исполнении следующего кода:
# gen = generate_random_name()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
#
# Выводится:
# tahxmckzexgdyt ocapwy
# dxqebbukr jg
# aym jpvezfqexlv
# iuy qnikkgxvxfxtxv

import random
import string


def generate_random_name():

    letter = string.ascii_lowercase
    latin_words = []
    while True: # не знаем сколько раз позовут генератор
        for i in range(2): #нам нужно 2 слова
            words = ''.join([random.choice(letter) for x in range(random.randrange(1, 15, 1))]) #генерируем из набор букв слово в заданной длинне
            latin_words.append(words) #апендим сгенерированное слово к пустому списку. генерим 2 слова и в цикле получим здесь 2 слова листом
        yield " ".join(latin_words) #разбиваем список через пробел и делаем строкой, отдаем результат этого такта
        latin_words = [] #чистим сгенерированные слова для новой итерации


gen = generate_random_name()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
