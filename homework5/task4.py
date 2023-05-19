# Игра "Эрудит"
# Нужно написать программу scrabble, которая помогает считать кол-во очков (points), полученное за слово (word)
# По одному очку вы получите за буквы а, в, е=ё, и, н, о, р, с, т.
# Два очка стоит д, к, л, м, п, у.
# Три балла получают за б, г, ь, а также я.
# Четыре балла стоят буквы й, ы.
# 5 очков засчитывается за ж, з, х, ц, ч.
# 6 и 7 очков не предусмотрено.
# Восемь можно получить за букву ф, ш, э, ю.
# 10 баллов стоит буква щ,
# а 15 - ъ
# Например (Ввод --> Вывод):
# курс --> 6 (к=2, у=2, р=1, с=1)


def scrabble(word):
    price = dict.fromkeys(['а', 'в', 'е', 'ё', 'и', 'н', 'о', 'р', 'с', 'т'], 1)
    price.update(dict.fromkeys(['д', 'к', 'л', 'м', 'п', 'у'], 2))
    price.update(dict.fromkeys(['б', 'г', 'ь', 'я'], 3))
    price.update(dict.fromkeys(['й', 'ы'], 4))
    price.update(dict.fromkeys(['ж', 'з', 'х', 'ц', 'ч'], 5))
    price.update(dict.fromkeys(['ф', 'ш', 'э', 'ю'], 8))
    price.update(dict.fromkeys(['щ'], 10))
    price.update(dict.fromkeys(['ъ'], 15))
    points = 0
    for i in word:
        points += price[i]
    print(points)
    return points

# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


data = ["курс", 'авеинорстё', 'дклмпеу', 'бгья', 'йы', 'жзхцч', 'фшэю', 'щъ', "карабасбарабас", "околоводопроводного",
        "еженедельное", 'эхоэнцефалограф', 'человеконенавистничество', 'делопроизводительница']

test_data = [6, 10, 13, 12, 8, 25, 32, 25, 21, 26, 20, 54, 34, 36]

for i, d in enumerate(data):
    assert scrabble(d) == test_data[i], f'С набором {d} есть ошибка, не проходит проверку'
    print(f'Тестовый набор {d} прошёл проверку')
print('Всё ок')
