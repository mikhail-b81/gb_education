# 1. Создать программный файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных будет свидетельствовать пустая строка.

print('Введите любой текст построчно. Пустая сторока означает - выход')
with open('lessontest.txt', 'w+') as file:
    check_len = -1
    while check_len != 0:
        user_text = input('Ввидете новую строку: ')
        check_len = len(user_text)
        file.write(user_text+'\n')

