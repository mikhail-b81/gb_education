# 6. Сформировать (не программно) текстовый файл.
# В нём каждая строка должна описывать учебный предмет и наличие лекционных, практических и лабораторных занятий по предмету.
# Сюда должно входить и количество занятий. Необязательно, чтобы для каждого предмета были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести его на экран.
#
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
# Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

# lesson_5_task_6.txt

with open('lesson_5_task_6.txt', encoding="utf-8") as file:
    file_content = file.readlines()


subject_dict = {}
for row in file_content:
    subject_list = row.split(':')
    hours_list = subject_list[1].split()
    sum_hours = 0
    for hours in (hours_list):
        digitals = '0'
        for digital in hours:
            if digital.isdigit():
                    digitals += digital
        sum_hours += int(digitals)
    subject_dict[subject_list[0]] = sum_hours


print(subject_dict)



