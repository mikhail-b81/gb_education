# 3. Создать текстовый файл (не программно).
# Построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников.
# Выполнить подсчёт средней величины дохода сотрудников.
# Пример файла:
#
# Иванов 23543.12
# Петров 13749.32

with open('lesson_5_task_3.txt', encoding="utf-8") as file:
    file_content = file.readlines()
    count_row = len(file_content)
    total_salary = 0
    print('Список сотрудников у которых оклад менне 20 тысяч: ')
    for i in range(count_row):
        row = (file_content[i]).split()
        if float(row[1]) < 20000.00:
            print(row[0])
        total_salary += float(row[1])


print('-'*20)
print('Средняя величина дохода: ', round(total_salary/(count_row),2))

