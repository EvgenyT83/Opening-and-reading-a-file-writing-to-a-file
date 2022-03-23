result_list = []
file_list = []
import os
import glob
os.remove("sort.txt")
def get_rezult():
    for i in glob.glob('*txt'):
         file_list.append(i)
    for i in file_list:
        my_dict = {}
        with open(i, 'r', encoding='utf-8') as file:
            my_dict['Имя файла'] = i
            lines = file.read()
            my_dict['Количество строк'] = len(lines)
            my_dict['Содержимое файла'] = lines
            result_list.append(my_dict)
    res = sorted(result_list, key=lambda x: x['Количество строк'])
    # создаем файл
    with open("sort.txt", "w", encoding='utf-8') as text_file:
        for element in res:
             text_file.write(element['Имя файла'] + '\n')
             text_file.write(str(element['Количество строк']) + '\n')
             text_file.write(str(element['Содержимое файла']) + '\n')
    return
get_rezult()

