from math import sqrt
from math import pi
from collections import Counter


def task1():
    """Попросіть користувача ввести число.
     Залежно від того,  яке число ( парне чи непарне ),
     надрукуйте відповідне повідомлення користувачеві.
     ( Число парне ( Число непарне )
     """
    user_input = input('VVedit chuslo\n')
    print('Number {} {} '.format(user_input, "!"))
    input_number = int(user_input)
    if input_number % 2 == 0:
        print("Parne")
    else:
        print("ne parne")


def task2():
    """
    Попросіть користувача ввести свій вік.
    Залежно від того,  яке вік ( повнолітній чи неповнолітній ),
    надрукуйте відповідне повідомлення користувачеві.
    ( Можна йти в диско клуб чи неможна)
     """
    user_input = input('VVedit vash vik\n')
    print('vik - {} '.format(user_input))
    input_number = int(user_input)
    if input_number >= 18:
        print(" u pass")
    else:
        print("too young")


def task3():
    """
    Візьміть список, скажімо, наприклад, цей  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
     і напишіть програму, яка роздруковує всі елементи списку менше 5.
    """
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    for x in a:
        if x < 5:
            print(x)


def task4():
    """
    Квадратне рівняння a*x*x + b*x + c = 0, “взяти” від юзера 3 числа
    a, b, c  і розвязати квадратне рівняння, надрукувати корені.
    Якщо розвязків нема тоді друкуємо розвязків нема.
    """
    a = float(input('VVedit a\n'))
    print('a =  {}'.format(a))
    b = float(input('VVedit b\n'))
    print('b =  {}'.format(b))
    c = float(input('VVedit c\n'))
    print('c =  {}'.format(c))
    d = b * b - 4 * a * c
    if d < 0:
        print("nema koreniv\a")
    elif d == 0:
        x = -b / (2 * a)
        print("x1 ={}\nx2 ={}\a".format(x, x))
    else:
        x1 = (-b - sqrt(d)) / (2 * a)
        x2 = (-b + sqrt(d)) / (2 * a)
        print("x1={}\nx2={}\a".format(x1, x2))


def task5():
    """
Напишіть функцію Python, щоб знайти максимальну та мінімальну кількість з послідовності чисел.
    """
    a = []
    n = int(input("Введіть довжину списку\n"))
    for i in range(0, n):
        na = int(input("Введіть число сиску № {}\n".format(i + 1)))
        a.append(na)
    c = Counter(a)
    print("Максимальна кількісь повторень - {}\nМінімальна кількість повторень - {}".format(c.most_common()[1],
                                                                                            c.most_common()[-1]))


def task5_2():
    a = [0, 1, 1, 1, 3, 5, 5]
    max_element = a[0]
    max_element_count = 1
    min_element = a[0]
    min_element_count = 1
    for x in a:
        temp_count = 0
        for y in a:
            if x == y:
                temp_count += 1
        if temp_count > max_element_count:
            max_element_count = temp_count
            max_element = x
        if temp_count < min_element_count:
            min_element_count = temp_count
            min_element = x
    print("Максимальний елемент - {} максимальна кількість повторень - {}".format(max_element, max_element_count))
    print("Мінімальний елемент - {} мінімальна кількість повторень - {}".format(min_element, min_element_count))


def task6():
    """
Напишіть функцію Python, яка приймає позитивне ціле число
і повертає суму куба всіх додатних цілих чисел, менших за вказаний номер.
    """
    x = int(input('Введіть позитивне ціле число\n'))
    y = 0
    for i in range(0, x,1):
        y = y + i * i * i

    print("Сума куба всіх додатніх чисел менших за {} = {} ".format(x, y))


def task7():
    """
Напишіть функція python до суми перших n натуральних чисел.
    """
    x = 0
    y = int(input('Введіть n\nn = '))
    for i in range(0, y):
        x = x + i
    print("Сума перших n натуральних чисел = {}".format(x))


def task8():
    """
Напишіть функцію Python до суми трьох цілих чисел.
Однак, якщо два значення однакові сума буде нульова.
    """
    a = int(input("Введіть ціле число a\na = "))
    b = int(input("Введіть ціле число b\nb = "))
    c = int(input("Введіть ціле число c\nc = "))
    x = a + b + c
    if a == b:
        print("сума = 0")
    elif a == c:
        print("сума = 0")
    elif b == c:
        print("сума = 0")
    else:
        print("Сума = {}".format(x))


def task9():
    """
Напишіть функцію Python для підрахунку числа 4 у певному списку. ( скільки четвірок є в списку )
    """
    a = []
    n = int(input("Введіть довжину списку\n"))
    for i in range(0, n):
        na = int(input("Введіть число сиску №{}\n".format(i + 1)))
        a.append(na)
    print("В даному списку 4 зустрічається {} раз".format(a.count(4)))


def task10():
    """
Напишіть функцію Python, щоб отримати обєм сфери з радіусом 6.
    """
    r = 6
    print(4/3 *( pi * r * r * r))


def task11():
    """
Напишіть функцію Python, яка приймає ціле число (n) і обчислює значення n + nn + nnn
    """
    n = int(input("Vvedit tsile chuslo\nn = "))
    y = n + n * n + n * n * n
    print("n + nn + nnn = {}".format(y))


if __name__ == "__main__":  # модуль запустится тільки коли він є головним
    task10()
