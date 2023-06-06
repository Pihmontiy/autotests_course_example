# Дан текстовый файл test_file/task1_data.txt
# Он содержит текст, в словах которого есть цифры.
# Необходимо удалить все цифры и записать получившийся текст в файл test_file/task1_answer.txt


f1 = open('test_file/task1_data.txt', encoding='utf-8')
f2 = open('test_file/task1_answer.txt', 'w', encoding='utf-8')
text1 = ''.join(f1.readlines())
for i in text1:
    if i.isdigit() is True:
        del i
    else:
        f2.write(i)
f1.close()
f2.close()


# Здесь пишем код

# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


with open("test_file/task1_answer.txt", 'r', encoding='utf-8') as file1:
    with open("test_file/task1_ethalon.txt", 'r', encoding='utf-8') as file2:
        answer = file1.readlines()
        ethalon = file2.readlines()
        assert answer == ethalon, "Файл ответа не совпадает с эталонном"
print('Всё ок')
