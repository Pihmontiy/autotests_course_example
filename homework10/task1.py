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
    for i in range(2):
        words = ''.join([random.choice(letter) for i in range(random.randrange(1, 15, 1))])
        latin_words.append(words)
    return latin_words
gen = generate_random_name()
print(gen)

# Здесь пишем код