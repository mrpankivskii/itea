def task_1():
    """На вхід програми подається один рядок з цілими числами. Числа розділені пропусками.
    Необхідно вивести суму цих чисел. Наприклад, якщо був введений рядок чисел 2 -1 9 6, то результатом роботи програми
    буде їх сума 16. Написати 2 функції( 1 функція приймає інпут від юзера, і передає агрумент
    2 функції яка робить обчислення і виводить результат)
"""

    number_line = input('Введіть числа розділені пропусками\n')
    task_1_1(number_line)


def task_1_1(num):
    li = list(num.split())
    res = 0
    for x in li:
        res += int(x)
    print(res)


def task_2():
    """Cтворіть словник з трьома річками і регіонами, територією яких вони протікають.
    Одна з можливих пар «ключ: значення» - 'Amazon': 'South America'.
    Додайте ще дві пари «річка: регіон» у словник. Виведіть повідомлення із назвами річки і регіону - наприклад,
    «The Amazon runs through South America.» для усіх елементів словника, враховуючи те,
    що у повідомлення у відповідні місця підставляються назви річок і територій.
    ( використати створення функції і метод format )
"""
    dct = {'Amazon': 'South America', 'Dnipro': 'Ukraine', 'Nil': 'Egipt'}
    for x in dct:
        print("The {} runs throu {} ".format(x, dct[x]))


def task_3():
    """Створіть англо-німецький словник, який називається e2g, і виведіть його на екран.
    Слова для словника: stork / storch, hawk / falke, woodpecker / specht і owl / eule.
    Виведіть німецький варіант слова owl. Додайте у словник, на ваш вибір, ще два слова та їхній переклад.
    Виведіть окремо: словник; ключі і значення словника у вигляді списків.
"""
    e2g = {'strk': 'storch', 'hawk': 'falke', 'woodpecker': 'specht', 'owl': 'eule'}
    print(e2g)
    print(e2g['owl'])
    e2g['1'] = '1'
    e2g['2'] = '2'
    print(list(e2g.keys()))
    print(list(e2g.values()))


def task_4():
    """Є словник (продовження на наст слайді):  inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'],
    'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}
Спробуйте зробити наступне:
     4a)    Додайте ключ до словника під назвою "pocket".
     4b)    Встановіть значення "pocket" як список, що складається з рядків 'seashell', 'strange berry', і  'lint’
     4с)    Відсортуйте ( .sort ()) елементи зі списку, що зберігаються під ключем  "backpack". ( і надрукуйте)
     4d)    Потім видаліть ("dagger") зі списку предметів, що зберігаються під ключем “backpack".
    4e)     Додайте 50 до числа, збереженого під "gold" ключем. І надрукуйте результат.

"""
 #4a-4b
    inventory = {
        'gold': 500,
        'pouch': ['flint', 'twine', 'gemstone'],
        'backpack': ['xylophone', 'dagger', 'bedroll', 'bread loaf'],
        'pocket': ['seashell', 'strange berry', 'lint']}
#4c
    # import ipdb; ipdb.set_trace()
    print(sorted(inventory['backpack']))
#4d
    backpack = list(inventory['backpack'])
    backpack.remove('dagger')
    inventory['backpack'] = backpack
#4e
    inventory['gold'] += 50
    print(inventory)


def task_5():
    """5a) Створіть новий словник під назвою prices за допомогою {}
    5b) Покладіть в словник такі значення "banana": 4, "apple": 2, "orange": 1.5, "pear": 3
    5с) Створити новий словник stocks.( який буде містити інформацію для кожного ключа із prices скільки товару
    ( запасу є на складі). Згенерувати значення випадковим чином.
    5d) Проітеруйтесь в циклі  через кожен  ключ  в prices. Для кожного ключа надрукуйте ключ разом із ціною, а також
    запасом на складі. Надрукуйте відповідь у наступному форматі:
apple
price: 2
stock: 5
   5d) Давайте визначимо, скільки грошей ви зробили б, якщо б ви продали всю їжу
   (змінна total, треба вирахувати і надрукувати її)
"""
    prices = {"banana": 4, "apple": 2, "orange": 1.5, "pear": 3}
    stocks = {"banana": 123, "apple": 212, "orange": 135, "pear": 153}
    for x in prices:
        print(x, '\nprices - ', prices[x], '\nstocks - ', stocks[x], '\ntotal - ', prices[x]*stocks[x])


def task_6():
    """Є дані
    lloyd = { "name": "Lloyd", "homework": [90.0,97.0,75.0,92.0],
    "quizzes": [88.0,40.0,94.0], "tests": [75.0,90.0] }
    alice = {"name": "Alice", "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0], "tests": [89.0, 97.0] }
    tyler = { "name": "Tyler",  "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],  "tests": [100.0, 100.0] }
6a) Створити список ( students ), що містить lloyd, alice, tyler
6b) Для кожного студента надрукувати інформацію у читабельному форматі
6с) Напишіть функцію average ( Приймає список, вертає результат.
Всередині функції викличіть вбудовану функцію sum() передавши аргумент.
Результат помістити в змінну total. Привести total до типу float ( число з плаваючою точкою).
Поділити total на кількість елементів у вхідному списку використавши len функцію. Вернути результат.
6d) Написати функцію get_letter_grade ( Використати if elif else. Якщо  90 і більше A, 70-90 B, 50-70 C, решта D.
Функція примає число вертає Оцінку A, B, C або D.)
6e) перевірити функцію get_letter_grade. Знайти середню оцінку по домашніх завданнях для кожного студента і надрукувати.
 (Тобто спочатку викликати функцію average[‘homework’], і передати результат в функцію get_letter_grade)
6e) Знайти середню оцінку для всього класу. ( в числовому і буквенному виразі )
"""
    lloyd = {"name": "Lloyd", "homework": [90.0, 97.0, 75.0, 92.0],
             "quizzes": [88.0, 40.0, 94.0], "tests": [75.0, 90.0]}
    alice = {"name": "Alice", "homework": [100.0, 92.0, 98.0, 100.0],
             "quizzes": [82.0, 83.0, 91.0], "tests": [89.0, 97.0]}
    tyler = {"name": "Tyler", "homework": [0.0, 87.0, 75.0, 22.0],
             "quizzes": [0.0, 75.0, 78.0], "tests": [100.0, 100.0]}
    students = [lloyd, alice, tyler]
    print(lloyd, "\n", alice, '\n', tyler)
    from pprint import pprint
    for x in students:
        pprint(students)

        
def average(var_list):
    total = sum(var_list)
    total = float(total)
    result = total / len(var_list)
    return result




if __name__ == '__main__':
    task_1()
