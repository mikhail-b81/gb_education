# 2. Создать текстовый файл (не программно), сохранить в нём несколько строк,
# выполнить подсчёт строк и слов в каждой строке.

with open('lesson_5_task_2.txt') as file:
    file_content = file.readlines()
    count_row = len(file_content)
    print(f'Колличество строк в файле: {count_row}\n')
    for i in range(count_row):
        print(f'{i+1} строка содержит {len((file_content[i]).split())} слов. Содержимое строки: ', file_content[i])


