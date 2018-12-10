def task_1():
    """
     Попросіть користувача своє ім'я та вік. Надрукуйте ім'я, стільки разів, скільки юзеру років.
    """
    age = int(input("Введіть ваш вік\n"))
    name = input("Введіть ваше імя\n")
    i = 1
    while i < age:
        i += 1

        print(name)


def task_2():
    """
    Встановіть змінну total що дорівнює 0.   Встановіть змінну guess що дорівнює від 1 до 10. Юзер має лише 4 спроби,
    щоб вгадати результат.
   У циклі while перевіряти, що total не дорівнює 4,   попросіть користувача ввести вгадування для числа від 1 до 10.
   Якщо юзер вгадав guess, то вийти із циклу while, недрукувати “you win ”. У циклі total інкрементувати( тобто додати 1).
   Якщо за 4 спроби невгадав, надрукувати “you lose”.
    """
    total = 0
    guess = 5
    print("Відгадайте число від 1 до 10. У вас є 4 спроби!")
    while total < 4:
        total += 1
        number = int(input("спроба № {}\n".format(total)))
        if number == guess:
            print("Вітаю!! Ви користали {} спроби".format(total))
            break
    else:
        print("Ви не відгадали")


def task_3():
    """
    Встановіть змінну name рівною "" (пуста стрічка). В нескінченному циклі while перевіряти інпут від юзера.
    Коли name не співпадає з "Iron Man", додайте рядок введення, який запитує: "Яка головна роль Тоні Старка"?
    Якщо юзер пише вірну відповідь вийти із циклу.
    """
    name = ""
    while name != "Iron Man":
        name = input('Яка головна роль Тоні Старка?')


def task_4():
    """
    Юзер вводить число. Якщо число менше 5, райзнути помилку Exception, якщо більше 4,
    то надрукувати квадрати чисел від 0 до введеного юзером значення.
    """
    number = int(input("Введіть число\n"))
    if number < 5:
        raise Exception("<5")
    if number > 4:
        output = 0
    for i in range(0, number):
        output += i ** 2
    print(output)

    try:
        task_4()
    except Exception as e:
        print(e.args[0])


def task_5():
    '''
Напишіть  програму, яка запитує список чисел (через пробіл в одному рядку), і наприкінці виводить максимальне
і мінімальне число.
    '''
    numbers = input("Введіть список\n")
    str_numbers = numbers.split()
    int_numbers = [int(x) for x in str_numbers]
    print(min(int_numbers), max(int_numbers))


def task_6():
    """
    Напишіть програму, яка знайде всі такі цифри, які діляться на 7, але не діляться на  5,
     від 2000 до 3200 (обидва включені). Надрукувати ці числа в одному рядку.
    """
    output = []
    for i in range(2000,3201):
        if (i % 7 == 0) & (i % 5 != 0):
            output.append(i)
    print(output)

def task_6_1():
    int_numbers = [int(x) for x in range(2000, 3201) if x % 7 == 0 and x % 5 != 0]
    print(int_numbers)


def task_7():
    """
    Є список letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"].
    Треба надрукувати слайс списку що містить d , e , f літери.
    """
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
    output = letters[3:6]
    print(output)


def task_8():
    """
    Напишіть програму Python, щоб перемножити всі елементи у списку. Надрукувати результат.
    """
    numbers = input("Введіть список\n")
    str_numbers = numbers.split()
    int_numbers = [int(x) for x in str_numbers str_numbers[x-1]*str_numbers[x]]
#reduce

if __name__ == "__main__":
    task_7()
