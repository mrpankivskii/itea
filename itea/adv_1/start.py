from random import randint


def printing(a):
    if type(a) == int:
        for x in range(a):
            print(x)
    elif type(a) == str:
        for x in a:
            print(x)


def loop():
    inp = int(input('enter here\n'))
    while inp > 0:
        inp -= 1
        if inp % 2 == 0:
            continue
        if inp == 5:
            break
    else:
        print('else')
    print('after loop while')


def task_1():
    """На вхід програми подається один рядок з цілими числами.
    Числа розділені пропусками. Необхідно вивести суму цих чисел.
    Наприклад, якщо був введений рядок чисел 2 -1 9 6, то результатом роботи програми буде їх сума 16.
    Написати 2 функції( 1 функція приймає інпут від юзера, і передає агрумент 2 функції
    яка робить обчислення і виводить результат)"""

    def user_input():
        user_inputed = input("enter number\n")
        resulting(user_inputed)

    def resulting(inp):
        user_iput = inp.split()
        count = 0
        for x in user_iput:
            count += int(x)
        print(count)

    user_input()


def task_2():
    """Cтворіть словник з трьома річками і регіонами, територією яких вони протікають.
    Одна з можливих пар «ключ: значення» - 'Amazon': 'South America'. Додайте ще дві пари «річка: регіон» у словник.
    Виведіть повідомлення із назвами річки і регіону - наприклад, «The Amazon runs through South America.»
    для усіх елементів словника, враховуючи те, що у повідомлення у відповідні місця підставляються назви річок і територій.
     ( використати створення функції і метод format )
"""
    my_dict = {'Amazon': 'South America', 'Ukraine': 'Dnipro', 'Russia': 'Lena'}
    for x, y in my_dict.items():
        print("The {} runs through {}".format(x, y))


def task_3():
    """Створіть англо-німецький словник, який називається e2g, і виведіть його на екран.
    Слова для словника: stork / storch, hawk / falke, woodpecker / specht і owl / eule.
    Виведіть німецький варіант слова owl. Додайте у словник, на ваш вибір, ще два слова та їхній переклад.
    Виведіть окремо: словник; ключі і значення словника у вигляді списків.
"""
    e2g = {"stork": "storch", "hawk": "falke", "woodpecker": "specht", "owl": "eule"}
    print(e2g["owl"])
    e2g['yes'] = "ya"
    e2g["no"] = 'nine'
    print(e2g)
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
    4e)     Додайте 50 до числа, збереженого під "gold" ключем. І надрукуйте результат."""
    inventory = {'gold': 500, 'pouch': ['flint', 'twine', 'gemstone'], 'backpack': ['xylophone', 'dagger', 'bedroll', 'bread loaf']}
    inventory['pocket'] = ['seashell', 'strange berry', 'lint']
    print(sorted(inventory['backpack']))
    inventory['backpack'].remove('dagger')
    inventory['gold'] += 50
    print(inventory)


def task_5():
    """5a) Створіть новий словник під назвою prices за допомогою {}
    5b) Покладіть в словник такі значення "banana": 4, "apple": 2, "orange": 1.5, "pear": 3
    5с) Створити новий словник stocks.( який буде містити інформацію для кожного ключа із prices скільки товару
    ( запасу є на складі). Згенерувати значення випадковим чином.
    5d) Проітеруйтесь в циклі  через кожен  ключ  в prices. Для кожного ключа надрукуйте ключ разом із ціною,
    а також запасом на складі. Надрукуйте відповідь у наступному форматі:
apple
price: 2
stock: 5
   5d) Давайте визначимо, скільки грошей ви зробили б, якщо б ви продали всю їжу ( змінна total,
   треба вирахувати і надрукувати її )
"""
    prices = {"banana": 4, "apple": 2, "orange": 1.5, "pear": 3}
    stocks = dict()
    for x in prices:
        stocks[x] = randint(10, 20)
    print()
    total = 0
    for x in prices:
        print(' {}\n price:   {}\n stock:  {}'.format(x, prices[x], stocks[x]))
        total += prices[x] * stocks[x]
    print('total: ', int(total))


def task_6():
    """Є дані
lloyd = { "name": "Lloyd", "homework": [90.0,97.0,75.0,92.0],  "quizzes": [88.0,40.0,94.0], "tests": [75.0,90.0] }
alice = {"name": "Alice", "homework": [100.0, 92.0, 98.0, 100.0],  "quizzes": [82.0, 83.0, 91.0], "tests": [89.0, 97.0]}
yler = { "name": "Tyler",  "homework": [0.0, 87.0, 75.0, 22.0], "quizzes": [0.0, 75.0, 78.0],  "tests": [100.0, 100.0] }
6a) Створити список ( students ), що містить lloyd, alice, tyler
6b) Для кожного студента надрукувати інформацію у читабельному форматі
6с) Напишіть функцію average ( Приймає список, вертає результат.  Всередині функції викличіть вбудовану функцію sum()
передавши аргумент. Результат помістити в змінну total. Привести total до типу float ( число з плаваючою точкою).
Поділити total на кількість елементів у вхідному списку використавши len функцію. Вернути результат.
6d) Написати функцію get_letter_grade ( Використати if elif else. Якщо  90 і більше A, 70-90 B, 50-70 C, решта D.
Функція примає число вертає Оцінку A, B, C або D.)
6e) перевірити функцію get_letter_grade. Знайти середню оцінку по домашніх завданнях для кожного студента і надрукувати.
(Тобто спочатку викликати функцію average[‘homework’], і передати результат в функцію get_letter_grade)
6e) Знайти середню оцінку для всього класу. ( в числовому і буквенному виразі )
"""
    lloyd = {"name": "Lloyd", "homework": [90.0, 97.0, 75.0, 92.0], "quizzes": [88.0, 40.0, 94.0],
             "tests": [75.0, 90.0]}
    alice = {"name": "Alice", "homework": [100.0, 92.0, 98.0, 100.0], "quizzes": [82.0, 83.0, 91.0],
             "tests": [89.0, 97.0]}
    yler = {"name": "Tyler", "homework": [0.0, 87.0, 75.0, 22.0], "quizzes": [0.0, 75.0, 78.0], "tests": [100.0, 100.0]}
    students = [lloyd, alice, yler]
    for x in students:
        for key, values in x.items():
            print("{} - {}".format(key, values))
        print('\n')

    def average(students):
        total = float(sum(students)) / len(students)
        return total

    def get_letter_grade(mark):
        if mark >= 90:
            return 'A'
        elif 70 <= mark < 90:
            return'B'
        elif 50 <= mark < 70:
            return'B'
        else:
            return'D'
    average_mark = []
    for x in students:
        print("{}'s average mark for homework - {}".format(x['name'], get_letter_grade(average(x["homework"]))))
        average_mark.append(average(x["homework"]))
        average_mark.append(average(x["quizzes"]))
        average_mark.append(average(x["tests"]))
    print("Average mark for all - {}({})".format(get_letter_grade(average(average_mark)), int(average(average_mark))))


if __name__ == "__main__":
    task_6()
