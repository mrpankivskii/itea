#дз 3(слово а не індекс)
from random import randint
from collections import Counter
def task_1():
    """Напишіть функцію max_of_three, яка приймає три числа і вертає максимальне із них.
    Викликати функцію і надрукувати результат."""
    a = int(input('Введіть 3 числа через Enter\n'))
    b = int(input('\n'))
    c = int(input('\n'))
    print(max_ofthree(a, b, c))

def max_ofthree(a, b, c):
    li = [a, b, c]
    return max(li)


def task_2():
   """аписати функцію random_from_list, яка приймає список слів, і вертає те слово, яке є найдовшим."""
   li = (input('введіть список\n'))
   lis = li.split()
   print(lis[random_from_list(lis)])
def random_from_list(lis):
    max_len = 0
    for i, x in enumerate(lis):
        if len(x) > max_len:
            max_len = len(x)
            index = i
    return index


def task_3():
    """Написати функцію, яка випадковим чином вертає число у проміжку від 0 до 10. ( random_10)
    Відповідно Написати функцію (summarizer). Яка містить змінну result=0.
    Функція summarizer викликає функцію random_10 і додає до суми рузультат.
    Якщо результат більше 100 то надрукуйте результат.
"""
    summarize()

def random_10():
    return randint(0, 10)


def summarize():
    result = 0
    while result < 100:
        result += random_10()
    print(result)


def task_4():
    """Написати функцію ( find_super ). Функція приймає на вхід число.
    А повинна вернути суму цифр вхідного числа ( якщо ця сума менша 10). Тобто якщо вхідне число = 12345.
    То сума цифр = 15 ( 15 > 10 ), тобто треба вернути суму цифр  вже 15. (застосувати рекурсію)
"""
    number = input('Введіть числа\n')
    li = number.split()
    print(find_super(li))

def find_super(number):
    suma = 0
    for x in number:
        suma += int(x)
    if suma > 10:
        return find_super(str(suma))
    else:
        return suma


def task_5():
    """Написати функцію (len_of_args), яка приймає ключові та позиційні аргументи
    ( вертає довжину позиційних елементів - len(args) ) .
    Також  написати функцію rand_of_el, яка двічі викликає функцію len_of_args  і вертає різницю результатів.
    Викликати функцію rand_of_el і надрукувати результат."""
    print(rand_of_el())

def len_of_args(*args, **kwargs):
    return len(kwargs)

def rand_of_el():
    res = len_of_args() - len_of_args()
    return res

def task_6():
    """Напишіть функцію!, яка приймає список ( в списку можуть бути дублікати елементів)
    і повертає новий список, який містить всі елементи першого списку, мінус усі дублікати.
    Викликати функцію, надрукувати результат.
"""
    li = list(input('Введіть елементи списоку\n'))
    print(li)
    list_to_set(li)
    print(list_to_set(li))

def list_to_set(li):
    se = set(li)
    li = list(se)
    return li


def task_7():
    '''Напишіть функцію, яка приймає рядок як параметр і повертає True, якщо рядок є паліндром, інакше False.
     Паліндром ( слово читається однаково ззаду-наперед, var = var[::-1], var -> паліндром ( використати рекурсію)'''

    plindrom = input('Введіть рядок\n')
    if_palindrom(plindrom)


def if_palindrom(plindrom):
    print('function is callled fith {}'.format(plindrom))
    if not plindrom:
        return True
    elif plindrom[0] == plindrom[-1]:
        return if_palindrom(plindrom)
    else:
        plindrom = plindrom[1:-1:]
        if_palindrom(plindrom)


def task_8():
    """Написати функцію, яка генерує ( рандомно) список списків( 5 вкладених списків ) довжиною 5 елементів.
    ( додавати числа 1 - 100) Відсортувати кожен список по 4 елементу вкладених списків.
    Вивести відсортований список на екран.
"""
    rand_generator()


def rand_generator():
    lim = []
    for x in range(5):
        lili = []
        for y in range(5):
            lili.append(randint(1, 100))
        lim.append(lili)
    for x in range(5):
        print(sorted(lim[x]))


def task_9():
    """Написати функцію для заміни одного символу в строці.
    Функція приймає 2 аргументи: 1аргумент - індекс символа який треба замінити, 2 аргумент - новий символ.
    Вернути нову строку.
"""
    lin = input('Введіть строку\n')
    arg = input('Введіть аргумент\n')
    ind = input('Введіть індекс\n')
    lin_change(lin, arg, ind)
    print(lin_change(lin, arg, ind))


def lin_change(lin, arg, ind):
    lin2 = lin[0:int(ind)-1] + arg + lin[int(ind):-1]
    return lin2


def task_10():
    """Написати функцію для підрахунку слів. Юзер вводить кількість слів, а потім відповідно ці слова по черзі.
    Деякі слова можуть повторюватись. Надрукувати кількість унікальних слів, а також скільки кожне слово повторилось.
    Порядок виводу повторень має співпадати із порядком введення слів.
"""
    number = int(input('Введіть кількість слів\n'))
    lis_1 = []
    for x in range(number):
        lis_1.append(input('введіть слово\n'))
    print(len(set(lis_1)))
    print(Counter(lis_1))


def task_11():
    """Написати функцію. У функції згенерувати 2 множити за допомогою randint(30, 50).
    Кожна множина має містити 10 елементів.
    Функція має вернути список елементів які є в 1 множині, але нема в 2 множині
"""
    se1 = []
    se2 = []
    for x in range(10):
         se1.append(randint(30, 50))
    for y in range(10):
         se2.append(randint(30, 50))
    se3 = set(se1) - set(se2)
    return(se3)

if __name__ == '__main__':
    task_10()
