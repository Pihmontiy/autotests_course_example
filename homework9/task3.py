# Дан файл test_file/task_3.txt можно считать, что это запись покупок в магазине, где указана только цена товара
# В каждой строке файла записана цена товара.
# Покупки (т.е. несколько подряд идущих цен) разделены пустой строкой
# Нужно найти сумму трёх самых дорогих покупок, которые запишутся в переменную three_most_expensive_purchases

# Здесь пишем код

f = open('test_file/task_3.txt').read().split('\n')
summ = 0
price_list = []
for i in f:
    if i == '':
        price_list.append(int(summ))
        summ = 0
        continue
    summ += int(i)
three_most_expensive_purchases = sum(sorted(price_list, reverse=True)[0:3])


assert three_most_expensive_purchases == 202346
