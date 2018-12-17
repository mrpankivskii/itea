#дз 5,6,8,9,11!!!!!!
from string import ascii_lowercase


def task_1():
    """
    Напишіть функцію, який приймає рядок як вхідний і повертає рядок задом наперед. 
    """
    line = input("Введіть рядок\n")
    print(''.join(reversed(line)))


def task_2():
    """
    Юзер вводить строку. (наприклад  inp = ‘saveChangesInTheEditor’). Вивести на екран скільки слів є
цьому інпуті. ( враховувати що нове слово починається із великої літери)
    """
    inp = "saveChangesInTheEditor"
    count = 0
    for x in inp:
        if 'A' <= x <= 'Z':
            count += 1
    print(count)


def task_3():
    """
pangram - строка яка містись усі літери англійської абетки. Перевірити чи введена строка є pangram
( import string    string.ascii_lowercase  це всі англійські  літери)
    """
    pangram = input("enter pangram\n")
    if ascii_lowercase == pangram:
        print("yes")
    else:
        print("not")


def task_4():
    """
    Є строка S, ми можемо перетворити кожну букву окремо на малу або велику, щоб створити іншу строку.
     Треба вернути список всіх можливих комбінацій. Наприклад є строка var = ‘it’
     результатом буде result_list = [‘IT’, “It”, “iT”, ‘it’].

    """
    s = input('Введіть текст\n')
    print(s.lower())
    print(s.upper())


def task_5():
    """Вам надається рядок, і ваше завдання - обміняти регістри
    ( великі букви замінити маленькими і навпаки). Www.HackerRank.com → wWW.hACKERrANK.COM
    """
    line = input('введіть стрічку\n')
    print(line.swapcase())


def task_6():
    """Вам дано рядок ( input )  і   ширину нового рядка який треба надрукувати. Ваше завдання полягає в тому,
    щоб обернути рядок у ширину . Наприклад рядок = ABCDEFGHIJKL
а new_width = 4. Відповідь має бути
ABCD
EFGH
IJKL
"""

def task_7():
    """Юзер вводить текст. У тексті якщо є два або більше пробіла,
    замінити одним. Табуляцію  теж замініти пробілом. Надрукувати результат. """
    s = input('Введіть текст\n')
    s_tab = s.expandtabs(1)
    s = s_tab.replace('  ', ' ')
    print(s)


def task_8():
    """Користувач вводить рядок і підрядок.
    Ви повинні надрукувати скільки разів підрядок є у рядку.
    Наприклад рядок =  ABCDCDC, підрядок = CDC, відповідь 2 рази. """
    s = input('Введіть рядок\n')
    ss = input('Введіть підрядок\n')
    count = s.find(ss)
    print(count)


def task_9():
    """Вам дано рядок. Розділити рядок розділювачем "" (пробіл)
    і приєднати результати, використовуючи дефіс. Надрукувати результат(ЗАМІНИТИ ПРОБІЛ ДЕФІСОМ)."""


def task_10():
    """Вам дають ім'я та прізвище людини на двох різних рядках. ( input ) Ваше завдання -
    прочитати їх і роздрукувати наступне: Hello firstname lastname! You just delved into python.
    """
    name = input("Введіть імя\n")
    lastname = input("Введіть прізвище\n")
    print(' Hello {} {}! You just delved into python.'.format(name, lastname))


def task_11():
    """(hackerrank) Юзер вводить строку. Перевірити чи ця строка є послідовністю!!!! цифр. Тобто
         var = ‘91011’  є послідовністю, треба надрукувати ‘YES’.
         var = ‘10001003’ не є послідовністю, треба надрукувати ‘NO’
    """
    input_number = input('Введіть стрічку\n')
    for index in range(1, 1 + len(input_number) // 2):
        first_number = int(input_number[:index])
        possible_string = ' '.join([str(x) for x in range(first_number, first_number + len(input_number))])
        if possible_string[:len(input_number)] == input_number:
            print('yes')
            return
    print('no')



def task_12():
    """hackerrank) Юзер вводить пароль.
    Вивести на екран кількість символів, яких не вистачає щоб цей пароль був “складним”.
    Для того щоб пароль був складним потрібно, щоб пароль складався як мінімум із 6 символів,
    містив у собі по одному символу із вказаних наборів:
    numbers = "0123456789"
	lower_case = "abcdefghijklmnopqrstuvwxyz"
	upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	special_characters = "!@#$%^&*()-+"
"""
    pas = input('Введіть пароль\n')
    num = 0
    n = 6 - len(pas)
    if len(pas) < 6:
        print("Пароль надто кототкий введіть ще {} символ(и)".format(n))
    if pas.isdigit():
        print("Пароль повинен містити не тільки цифри")
    else:
        num += 1
    if pas.islower():
        print("Пароль повинен містит букви верхнього регістру")
    else:
        num += 1
    if pas.isupper():
        print("Пароль повинен містити букви нижнього регістру")
    else:
        num += 1
    if pas.isalpha():
        print("Пароль повинен містити цифри ")
    if '!' or '@' or '#' or '$' or '%' or '^' or '&' or '*' or '(' or ')' or '-' or '+' in pas:
        print('Пароль надійний')
    else:
        print("Пароль повинен містити спеціальні символи'!@#$%^&*()-+'")


if __name__ == '__main__':
    task_11()
