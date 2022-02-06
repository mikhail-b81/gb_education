# 7. Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка будет содержать
# данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
#
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчёт средней прибыли её не включать.
# Далее реализовать список.
# Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить её в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
#
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджер контекста.

# lesson_5_task_7.txt

import json


with open('lesson_5_task_7.txt', encoding="utf-8") as file:
    file_content = file.readlines()


company_dict = {}
all_profit = 0
count_company_profit = 0
for row in file_content:
    company_list = row.split()
    company_profit = int(company_list[2]) - int(company_list[3])
    if company_profit > 0:
        all_profit += company_profit
        count_company_profit += 1
    company_dict[company_list[0]] = company_profit


average_profit = round(all_profit/count_company_profit)
average_profit_dict = {'average_profit': average_profit}
result_list = [company_dict, average_profit_dict]
# print('-'*20)
# print('Общая прибыль: ', all_profit)
# print('Компании с прибылью: ', count_company_profit)
# print('average_profit: ', average_profit)
# print(company_dict)
# print(average_profit_dict)
# print(result_list)

with open('lesson_5_task_7_result.json', 'w') as file:
    json.dump(result_list, fp=file)


