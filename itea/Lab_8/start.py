from random import randint


def logg(func):
    def inner(*args, **kwargs):
        with open('logg.txt', 'a') as log_file:
            log_file.write(str(args))
            log_file.write(str(kwargs))
            result = func(*args, **kwargs)
            log_file.write('Arguments are writen')
            return result
    return inner


@logg
def add(*args, **kwargs):
    return sum(args)


@logg
def multiplay(*args, **kwargs):
    result = 1
    for x in args:
        result *= x
    return sum(args)


@logg
def task_1(a, b, c):
    """Напишіть декоратор ( функцію logg), яка обертає функції. Суть декоратора  в тому, що він логує (записує у файл)
    позиційні і ключова аргументи. В кінці враппера записати у файл ‘Arguments are written’.
    Також створити дві функції add & multiply, які підповідно додають, перемножують позиційні аргументи.
    Обернути функції add & multiply декоратором logg і викликати їх через if __name__ == “__main__”.
    Перевірити лог файл чи декоратор спрацював. """


def task_2():
    """Скопіювати функцію add із попереднього прикладу. Написати декоратор cached.
    Суть декоратора в кешуванні роботи функції add.
    Тобто треба створити словник де ключами будуть аргументи ( позиційні )
    а значенням буде результат виконання функції add. Відповідно декоратор має перевіряти чи є дані в словнику
    (була вже викликана функція add із такими аргументами)  і вернути результат.
    Програмно перевірити чи дані беруться із кешу чи виконується функція add. sorted ?
"""


def task_3():
    """Написати 2 функції add ( додає позиційні аргументи в циклі for і вертає результат) і add_advance
    ( яка додає позиційні аргументи використовуючи builtin функцію sum). Написати декоратор deprecated_add,
    обгорнути функцію add. У враппері натомість викликати функцію add_advanced замість add, і друкувати користувачеві
    повідомлення, що add функція є deprecated. Перевірити чи дійсно викликається функція add_advance.
"""


def deprecatd_add(func):
    def wrapper(*args, **kwargs):
        print('add is deprecated')
        return add_advance(*args, **kwargs)
    return wrapper


@deprecatd_add
def add(*args, **kwargs):
    res = 0
    for x in args:
        res += x
    print("add")
    return res


def add_advance(*args, **kwargs):
    print('add_advance')
    return sum(args)


def task_4():
    """Напишіть функцію, яка генерує словник. Де ключами є слова square, cubic, four, five.
    А значення будуть лямбда функції які приймають число як аргумент, а вертають піднесення до відповідного степеня.
    У функції по черзі викликати лямбда функції із випадково згенерованим числом від 10 до 20."""


def generator(*args, **kwargs):

    dikt = {'square': lambda x: x**2, 'cubic': lambda x: x**3, 'four': lambda x: x**4, 'five': lambda x: x**5}
    for key in dikt:
        print(dikt[key](randint(10, 20)))


def task_5():
    """Написати функцію, яка генерує ( рандомно) список списків( 5 вкладених списків ) довжиною 5 елементів.
    Відсортувати 1 список по 4 елементу вкладених списків. Вивести відсортований список на екран.
"""
    m = list()
    for x in range(5):
        mm = list()
        m.append(mm)
        for y in range(5):
            mm.append(randint(0, 100))
    print(sorted(m, key=lambda i: i[3]))


def task_6():
    """Написати функцію( gen_random) яка генерує рандомне число від 1 до 10.
    Якщо число = 1, то вернути його, якщо більше 1 то викликати помилку (ImportError).
    Написати функцію run ( яка буде викликати функцію gen_random і друкувати результат.
    Створити декоратор retry, який буде 20 разів пробувати викликати функцію gen_random.
    Якщо за 20 разів gen_random не вернув результат то вернути ‘NO RESULT’. Запустити програму.
"""


def retry(func):
    def my_funk(*args, **kwargs):
        for x in range(20):
            print("x={}".format(x))
            try:
                res = func(*args, **kwargs)
                return res
            except:
                continue
        print('NO RESULT')
    return my_funk


def run():
    print(gen_random())

@retry
def gen_random():
    num = randint(1, 10)
    if num == 1:
        return num
    raise Exception(ImportError)


if __name__ == "__main__":
    run()