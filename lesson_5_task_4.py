# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
#
# Напишите программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.


# lesson_5_task_4.txt
# lesson_5_task_4_new.txt

num_dict = {1:'Один', 2:'Два', 3:'Три', 4:'Четыре'}
new_list = []

with open('lesson_5_task_4.txt', encoding="utf-8") as file:
    file_content = file.readlines()
    count_row = len(file_content)
    for i in range(count_row):
        row_list = file_content[i].split()
        new_list.append(num_dict[int(row_list[2])]+' '+row_list[1]+' '+row_list[2])



with open('lesson_5_task_4_new.txt', 'w+', encoding="utf-8") as file:
    for row in new_list:
        file.write(row + '\n')
