from random import randint
from functools import reduce
from time import time, sleep


def task_1():
    """Напишіть функцію max_of_three, яка приймає три числа і вертає максимальне із них.
    Викликати функцію і надрукувати результат."""
    one = int(input('input number\n'))
    two = int(input('input number\n'))
    three = int(input('input number\n'))

    def max_of_three(one, two, three):
        numbers = [one, two, three]
        max_number = 0
        for x in numbers:
            if x > max_number:
                max_number = x
        print(max_number)

    max_of_three(one, two, three)


def task_2():
    """Написати функцію random_from_list, яка приймає список слів, і вертає те слово, яке є найдовшим."""

    def random_from_list(random_list):
        test_word = ''
        for word in random_list:
            if len(test_word) < len(word):
                test_word = word
        print(test_word)

    random_char = input("input strind\n")
    random_list = random_char.split(' ')
    random_from_list(random_list)


def task_3():
    """Написати функцію, яка випадковим чином вертає число у проміжку від 0 до 10.
    ( random_10) Відповідно Написати функцію (summarizer). Яка містить змінну result=0.
    Функція summarizer викликає функцію random_10 і додає до суми рузультат. Використати цикл while True.
    Якщо результат більше 100 то надрукуйте результат."""

    def random_10():
        return randint(1, 10)

    def summerizer():
        result = 0
        while True:
            result += random_10()
            if result > 100:
                print(result)
                break

    summerizer()


def task_4():
    """Написати функцію ( find_super ). Функція приймає на вхід число.
    А повинна вернути суму цифр вхідного числа ( якщо ця сума менша 10).
    Тобто якщо вхідне число = 12345. То сума цифр = 15 ( 15 > 10 ), тобто треба вернути суму цифр  вже 15.
    (застосувати рекурсію)
"""

    def find_super(number):
        li = list()
        for x in number:
            li.append(int(x))
        result = sum(li)
        return result if result < 10 else find_super(str(result))

    number = input('input number\n')
    print(find_super(number))


def task_5():
    """Написати функцію (len_of_args), яка приймає ключові та позиційні аргументи
    ( вертає довжину позиційних елементів - len(args) ) .
    Також  написати функцію rand_of_el, яка двічі викликає функцію len_of_args  і вертає різницю результатів.
    Викликати функцію rand_of_el і надрукувати результат."""

    def len_of_args(*args, **kwargs):
        return len(args)

    def rand_of_el():
        result = len_of_args() - len_of_args()
        return result

    print(rand_of_el())


def task_6():
    """Напишіть функцію!, яка приймає список ( в списку можуть бути дублікати елементів) і повертає новий список,
    який містить всі елементи першого списку, мінус усі дублікати. Викликати функцію, надрукувати результат.
"""

    def list_func(li):
        result = set(li)
        return list(result)

    string = input('input string\n')
    li = string.split(' ')
    print(list_func(li))


def task_7():
    """Напишіть декоратор ( функцію logg), яка обертає функції.
    Суть декоратора  в тому, що він логує (записує   у файл) позиційні і ключова аргументи. В кінці враппера записати
    у файл ‘Arguments are written\n’.  Також створити дві функції add & multiply, які підповідно додають, перемножують
    позиційні аргументи і вертають результат. Обернути функції add & multiply декоратором logg і викликати їх через
    if __name__ == “__main__”. Перевірити лог файл чи декоратор спрацював.
"""

    def logg(func):
        def inner(*args, **kwargs):
            with open('my_file', 'w') as my_file:
                # import ipdb; ipdb.set_trace()
                my_file.write(f"Arguments are written\n{args}\n{kwargs}’")
            result = func(*args, **kwargs)
            return result

        return inner

    @logg
    def add(*args):
        return sum(args)

    @logg
    def multiply(*args):
        multy = 1
        for x in args:
            multy *= x
        return multy

    add(1, 2, 3)
    multiply(1, 2, 3)


def task_8():
    """Скопіювати функцію add із попереднього прикладу. Написати декоратор cached.
    Суть декоратора в кешуванні роботи функції add.
    Тобто треба створити словник де ключами будуть аргументи ( позиційні )
    а значенням буде результат виконання функції add. Відповідно декоратор має перевіряти чи є дані в словнику
    (була вже викликана функція add із такими аргументами)  і вернути результат.
    Програмно перевірити чи дані беруться із кешу чи виконується функція add?
"""
    cashed_dict = dict()

    def cashed(func):
        def inner(*args, **kwargs):
            for key in cashed_dict:
                if key == args:
                    print(f"{cashed_dict[args]} - from cash")
                    return cashed_dict[args]
            else:
                cashed_dict[args] = func(*args, **kwargs)

        return inner

    @cashed
    def add(*args, **kwargs):
        print("add is called")
        print(sum(args))
        return sum(args)

    add(1, 2, 3)
    add(1, 2, 3)
    add(1, 2, 3)
    add(1, 3, 3)


def task_9():
    """Удосконалити декоратор із 8 завдання, щоб було можливість передати декоратору ключовий  аргумент
    наприклад time_caching=60,  і відповідно перевіряти чи дані є давнішими ніж time_caching,
    якщо давнішими наново виконати функцію add."""
    cashed_dict = dict()

    def cashed(*dec_args, **dec_kwargs):
        def wrapper(func):
            def inner(*args, **kwargs):
                for key in cashed_dict:
                    if key == args:
                        m = time() - cashed_dict[args][1]
                        if m < dec_kwargs['time_caching']:
                            print(f"{cashed_dict[args][0]} - from cash")
                            return cashed_dict[args]
                else:
                    cashed_dict[args] = [func(*args, **kwargs), time()]

            return inner

        return wrapper

    @cashed(time_caching=2)
    def add(*args, **kwargs):
        print("add is called")
        print(sum(args))
        return sum(args)

    add(1, 2, 3)
    add(1, 2, 3)
    sleep(3)
    add(1, 2, 3)
    add(1, 3, 3)


def task_10():
    """Написати 2 функції add (яка додає позиційні аргументи використовуючи builtin функцію sum)
    і add_old(додає позиційні аргументи в циклі for і вертає результат).
    Написати декоратор deprecated_add, обгорнути функцію add_old.
    У враппері натомість викликати функцію add замість add_old, і друкувати користувачеві повідомлення,
    що add_old функція є deprecated. Перевірити чи дійсно викликається функція add.
    (Удосканалити depracated _add від певної дати переданої декоратору в аргумент )"""
    def deprecated_add(func):
        def inner(*args, **kwargs):
            print("add_old функція є deprecated")
            return add(*args, **kwargs)

        return inner

    def add(*args, **kwargs):
        print(f"add - {sum(args)}")
        return sum(args)

    @deprecated_add
    def add_old(*args, **kwargs):
        summ = 0
        for x in args:
            summ += x
            print("add_old")
        return summ
    add_old(1, 2, 3, 7)


def task_11():
    """Напишіть функцію, яка генерує словник. Де ключами є слова square, cubic, four, five.
    А значення будуть лямбда функції які приймають число як аргумент, а вертають піднесення до відповідного степеня.
    У функції по черзі викликати лямбда функції із випадково згенерованим числом від 10 до 20. """
    number = int(input(("input number\n")))
    my_dict = dict()
    my_dict['square'] = lambda x: x ** 2
    my_dict['cubic'] = lambda x: x ** 3
    my_dict['four'] = lambda x: x ** 4
    my_dict['five'] = lambda x: x ** 5
    for key in my_dict:
        my_dict[key](number)
        print(my_dict[key](number))


def task_12():
    """ Написати функцію, яка генерує ( рандомно) список списків( 5 вкладених списків ) довжиною 5 елементів.
    Відсортувати 1 список по 4 елементу вкладених списків. Вивести відсортований список на екран.
    """

    def takeforth(elem):
        return elem[3]

    my_list = list()
    for x in range(5):
        my_inner_list = list()
        for y in range(5):
            my_inner_list.append(randint(1, 100))
        my_list.append(my_inner_list)
    print(my_list)
    print(sorted(my_list, key=takeforth))


# виводить результат роботи функції і ексепшин
def task_13():
    """Написати функцію( gen_random) яка генерує рандомне число від 1 до 10. Якщо число = 1,
    то вернути його, якщо більше 1 то викликати помилку (ImportError).
    Написати функцію run ( яка буде викликати функцію gen_random і друкувати результат.
    Створити декоратор retry, який буде 20 разів пробувати викликати функцію gen_random.
    Якщо за 20 разів gen_random не вернув результат то вернути ‘NO RESULT’. Запустити програму."""

    def gen_random():
        rand_number = randint(1, 10)
        if rand_number == 1:
            return rand_number
        else:
            raise ImportError

    def retry(func):
        def inner(*args, **kwargs):
            try:
                for x in range(20):
                    result = func(*args, **kwargs)
                    if result == 1:
                        return result
            except:
                print("NO RESULT")

        return inner

    @retry
    def ran():
        print(gen_random())

    ran()


def task_14():
    """ Створити лямбда функцію, що множить число на рандом від 1 до 10.
    Згенерувати список від 1 до 10.
    Застосувити лямда функцію до цього списку, відфільтрувати цей список ( позбутись непарних чисел) і знайти суму списку.
    ( Використати map, reduce, filter )
"""

    def filtration(a):
        if a % 2 == 0:
            return False
        else:
            return True

    my_list = list(range(10))
    my_func = list(map(lambda x: x * randint(1, 10), my_list))
    filter_func = list(filter(filtration, my_func))
    result = reduce(lambda a, x: a + x, filter_func)
    print(result)


def task_15():
    """ Напишіть функцію, яка приймає рядок як параметр і повертає True, якщо рядок є паліндром, інакше False.
    Паліндром ( слово читається однаково ззаду-наперед, var = var[::-1], var -> паліндром ( використати рекурсію)"""
    var = input('input palidrom\n')

    def palindrom_check(var):
        print(var)
        if var == var[::-1]:
            return True
        else:
            palindrom_check(var[1:-1])
            return False

    print(palindrom_check(var))

#----------------------------------------------------------------------------
def task_16():
    """ ** Задача із конем. ( треба обійти всі клітинки за 64 ходи)   Спробувати придумати алгоритм,
    якщо не вдається то є готовий алгоритм на вікіпедії. Відповідно треба реалізувати цей алгоритм."""


# ---------------------------------------------------------------------------
def task_17():
    """Написати timing декоратор. Суть якого виміряти час виконання функції.
    І після виконання декорованої функції надрукувати час.
    Написати функцію test_list_long
    ( ця функція  приймає аргумен n, і в циклі for послідовно додає числа від 1 до n до нашого списку)
    Функція test_list_long  нічого не вертає.
    Написати функцію test_list_advance ( приймає аргумент n і створює список довжиною n )
    li = [True]*n  .   В циклі for послідовно змінювати кожен елемент списку на значення від 1 до n.
    Ця функція теж нічого не вертає.
    В теорії функція test_list_advance  має працювати швидше оскільки С-масиви не будуть перекопійовуватись.
    Задекорувати створені функції timing декоратором і викликати із аргументом 10**12.
    """

    def timing(func):
        def inner(*args, **kwargs):
            func_start_time = time()
            func(*args, **kwargs)
            func_end_time = time()
            func_time = func_end_time - func_start_time
            print(func_time)
            return func_time

        return inner

    def test_list_long():
        pass

    @timing
    def test_list_advance(n):
        my_list = list()
        for x in range(n):
            my_list.append(randint(0, 9))

    test_list_advance(3)


def task_18():
    """Перевірити швидкість додавання елементів в кінець і на початок списків.
    Тобто створити дві функції які до пустого списку 10 тисяч разів додають в кінець
    ( друга функція вставляє на початок елементи). Задекорувати ці функції timing декоратором."""

    def timing(func):
        def inner(*args, **kwargs):
            func_start_time = time()
            result = func(*args, **kwargs)
            func_end_time = time()
            func_time = func_end_time - func_start_time
            print(f"time - {func_time} -|||- {func.__name__}")
            return result

        return inner

    my_list = list()

    @timing
    def add_in_end():
        for x in range(10000):
            my_list.append("element")

    @timing
    def add_in_start():
        for x in range(10000):
            my_list.insert(0, "element")

    add_in_start()
    add_in_end()


if __name__ == "__main__":
    task_10()
