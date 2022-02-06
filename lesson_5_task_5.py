# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить её на экран.

from random import randint

count_num = randint(5, 20)


with open('lesson_5_task_5.txt', 'w+', encoding="utf-8") as file:
    for i in range(count_num):
        var_num = randint(1, 100)
        file.write(str(var_num) + ' ')


with open('lesson_5_task_5.txt', encoding="utf-8") as file:
    file_content = file.readline()
    file_list = file_content.split(' ')
    file_list.pop(-1)
    sum_num = 0
    for num in file_list:
        sum_num += int(num)


print(sum_num)

