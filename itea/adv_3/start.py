from random import randint
import csv
import pickle
from module1 import load_db_pickle
import requests
import json


def task_1():
    """Написати функцію, яка створить  файл numbers.txt, якщо його не існує.
    Запишіть у файл 10 чисел, кожне з нового рядка ( згенерувати модулем random від 1 до 100).
    Напишіть функцію, яка зчитує ці числа з файлу і обчислює їх суму, виводить цю суму на екран і,
    водночас, записує цю суму у інший файл під назвою sum_numbers.txt
"""
    with open("numbers.txt", 'w') as numbers:
        for x in range(10):
            numbers.write(str(randint(1, 100)) + '\n')
    summ = 0
    with open("numbers.txt", 'r') as numbers:
        for x in numbers:
            summ += int(x.strip())
    print(f'sum = {summ}')
    with open("sum_numbers.txt", 'w') as summs:
        summs.write(str(summ))


def task_2():
    """Створіть новий файл у текстовому редакторі і напишіть 3 рядки тексту у ньому про можливості Python.
    Кожен рядок повинен починатися з фрази: In Python you can .... Збережіть файл під ім’ям learning_python.txt.
    Напишіть функцію, яка зчитує файл і виводить текст з перебором рядків об’єкта файлу і зі збереженням рядків у списку
    з подальшим виведенням списку поза блоком with"""
    my_list = ['print', 'write files', 'read files']
    with open("learning_python.txt", 'w') as python:
        for x in my_list:
            python.write(f'In Python you can {x}\n')

    def reading():
        with open("learning_python.txt", 'r') as python:
            for x in python:
                print(x)
                my_list.append(x)
        print(my_list)
    reading()


def task_3():
    """Функція replace() може використовуватися для заміни будь-якого слова у рядку іншим словом.
    Прочитайте кожен рядок зі створеного у попередньому завданні файлу learning_python.txt і замініть слово
    Python назвою іншої мови, наприклад C при виведенні на екран. Це завдання написати в окремій функції."""
    with open("learning_python.txt", 'r') as python:
        for x in python:
            print(x.replace('Python', 'C'))


def task_4():
    """Завантажте текстову версію однієї з книг із сайту Project Gutenberg’s.
    Замініть усі розриви рядків у тексті символом пропуску і запишіть відформатований текст у новий файл
    formatted_text.txt."""
    with open("book.txt", 'r') as book:
        my_book_str = book.read()
    my_book_str = my_book_str.replace('\n', ' ')
    with open("formatted_text.txt", 'w') as formated:
        formated.write(my_book_str)


def task_5():
    """Завантажте текстову версію книги
    The Life and Adventures of Robinson Crusoe By Daniel Defoe із сайту Project Gutenberg’s.
    Витягніть із тексту заголовки усіх розділів, які мають вигляд, на зразок: CHAPTER I—START IN LIFE.
    Запишіть знайдені назви у новий файл chapters.txt
"""
    with open("book2.txt", 'r') as book:
        for x in book:
            if "CHAPTER" in x:
                with open("chapters.txt", 'a') as chapters:
                    chapters.write(x)


def task_6():
    """ До попередньої задачі. Визначте відсоток малих і великих літер у тексті, що зберігається у файлі.
Скористайтеся, як зразком вхідного файлу, текстовий файл із сайту Project Gutenberg’s. Використайте функцію isalpha()"""
    with open("book2.txt", 'r') as book:
        upper_counter = 0
        lower_counter = 0
        counter = 0
        for x in book.read():
            if x.isalpha():
                counter += 1
                if x.isupper():
                    upper_counter += 1
                if x.islower():
                    lower_counter += 1
    lower = (lower_counter / counter) * 100
    upper = (upper_counter / counter) * 100
    print(f'lower - {lower}%\nuper - {upper}%')


def task_7():
    """7) Робота із info.csv файлом. Використати кодування encoding='ISO-8859-1'   У файлі вказано школи із Англії.
    7.1) зчитати файл і помістити дані в певну структуру ( змінну)
    7.2) (окрема ф-я) відфільтрувати дані де є вказано адресу сайту і зберегти в базі даних pickle
    7.3) (окрема ф-я) відфільтрувати дані де директорами є Ms і Mrs. Потім зберегти у json файлі дані про номер школи,
    місто, моб тел ( якщо є) , сайт ( якщо є), імя та прізвище директора.
    7.4) Написати ф-ю яка рахує кількість відкритих шкіл після 2000 року. Надрукувати результат.
    7.5) Відфільтрувати школи які вже є закритими, відповідно відкриті школи записати в файл оpened.csv.
"""
    title = list()

    def site_sort():
        global title
        with_sites = list()
        for number, row in enumerate(info):
            if number == 0:
                title = row
            index = title.index('SchoolWebsite')
            if row[index]:
                with_sites.append(f'{str(row)}\n')
        with open('sites.pickle', 'wb') as sites:
            pickle.dump(with_sites, sites, pickle.HIGHEST_PROTOCOL)

    def school_counter():
        count = 0
        for x in info:
            if int(x['OpenDate']) > int('01-01-2000'):
                count += 1
        return count

    with open('info.csv', encoding='ISO-8859-1') as info_csv:
        info = csv.reader(info_csv, delimiter=",")
        site_sort()
        print(school_counter())


def task_8():
    """Отримати тендери по url https://lb.api.openprocurement.org/api/2.4/tenders?offset=2018-03-19.
    Для цього використати requests бібліотеку.
Пройтись по всіх id тендерів і отримати тендер повністю
( по url https://lb.api.openprocurement.org/api/2.3/tenders/09076ffc415e4d57ad7046aacc91b6e1 ).
(In [32]: resp = requests.get('https://jsonplaceholder.typicode.com/todos/1')
In [33]: resp.json()
Out[33]: {'userId': 1, 'id': 1, 'title': 'delectus aut autem', 'completed': False})
  8.1) Записати контракт на найвищу суму у файл max_contract.json. Контракти можуть бути у тендерів із статусом complete
  8.2) Надрукувати кількість неуспішних тендерів. ( статус яких = unsuccessful )
  8.3) Надрукувати загальну кількість учасників ( унікальних )
 у всіх  тендерах ( tender -> bids -> identifier -> id )  В одному тендері може бути кільки bids ( пропозицій )
  8.4) Надрукувати середню кількість bids ( пропозицій) на один тендер.
  8.5) Якщо тендер має тип ( procurementMethodType)  aboveThresholdUA  або майданичик, що створив цей тендер
  ( поле owner ) ->  prom.ua  то ці тендери зберегти в файлі tenders.pickle
"""
    respond = requests.get('https://lb.api.openprocurement.org/api/2.4/tenders?offset=2018-03-19')
    resp = respond.json()
    list_of_dicts = resp['data']
    tender_list = list()
    for x in list_of_dicts:
        tend = requests.get(f"https://lb.api.openprocurement.org/api/2.3/tenders/{str(x['id'])}")
        tender = tend.json()
        tender_list.append(tender)

    def max_velue():
        contract_values = list()
        for tender in tender_list:
            if tender['data']['status'] == 'complete':
                contract_values.append(tender['data']['contracts'][0]['value']['amount'])
        max_contract_value = max(contract_values)
        return max_contract_value

    def contract():
        for tender in tender_list:
            if tender['data']['contracts'][0]['value']['amount'] == max_velue():
                with open('max_contract.json', 'wb') as max_contract_value_file:
                    json.dump(tender, max_contract_value_file)

    def unsuccessful():
        count = 0
        for tender in tender_list:
            if tender['data']['status'] == 'unsuccessful':
                count += 1
        return count

    def contractors():
        contractors_list = list()
        for tender in tender_list:
            if tender['data']['contracts']['suppliers'][0]['contactPoint']['name'] not in contractors_list:
                contractors_list.append(tender['data']['contracts']['suppliers'][0]['contactPoint']['name'])
        print(len(contractors_list))

    contract()
    print(f'unsuccessful - {unsuccessful()} tenders')
    #contractors()


def task_9():
    """ Створити 2 модуля (module2.py, module1.py).  У модулі module2.py написати ф-ю max_of_three.
У модулі module1 написати 2 функції ( create_db_pickle яка відповідно записує у pickle файл словник із ключем
max_func_from_module2 значення функції max_of_three імпортованої із module2.)
Друга функція load_db_pickle має завантажити файл pickle отримати обєкт і викликати ф-ю max_of_three.
Виконати функції створення і читання pickle, перевірити чи вони працюють.
"""
    load_db_pickle()


if __name__ == "__main__":
    task_9()
