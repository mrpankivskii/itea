from output_window import output


def task_1():
    """Напишіть код, який приймає рядок як вхідний і повертає рядок задом наперед. """
    user_input = input("Введіть строку\n")
    output_line = ''.join(reversed(user_input))
    output("input: "+user_input+"\n"+"Output: "+output_line)


def task_2():
    """Юзер вводить строку. (наприклад  inp = ‘saveChangesInTheEditor’). Вивести на екран скільки слів є цьому інпуті.
    ( враховувати що нове слово починається із великої літери)
"""
    user_input = input("Введіть строку\n")
    count = 0
    for x in user_input:
        if x.isupper():
            count += 1
    output("input: "+user_input+"\n"+"Output: "+str(count)+'Слів')


def task_3():
    """pangram - строка яка містись усі літери англійської абетки. Перевірити чи введена строка є pangram"""
    user_input = input("Введіть строку\n")
    pangram = "abcdefghijklmnopqrstuvwxyz"
    temp_pangram = list(pangram)
    for x in user_input:
        if x in list(temp_pangram):
            temp_pangram.remove(x)
    pangram = ''.join(temp_pangram)
    if len(pangram) == 0:
        output('True')
    else:
        output('FALSE')


def task_4():
    """Є строка S, ми можемо перетворити кожну букву окремо на малу або велику, щоб створити іншу строку.
    Треба вернути список всіх можливих комбінацій. Наприклад є строка var = ‘it’ результатом буде
    result_list = [‘IT’, “It”, “iT”, ‘it’]."""
    user_input = input("Введіть строку\n").lower()
    print(user_input)
    count = 0
    while not user_input.isupper():
        for x in user_input:
            if x.isupper():
                index = user_input.index(x)
                for y in user_input[:index+1]:
                    user_input = user_input.replace(y, y.lower(), 1)
            elif x.islower():
                if user_input.count(x) > 1:
                    count_dict = {x: user_input.count(x)}

                    if count == user_input.count(x) + 1:
                        count = 0
                else:
                    user_input = user_input.replace(x, x.upper(), 1)
                    break
        print(user_input)


def task_5():
    """Юзер вводить строку. Перевірити чи ця строка є послідовністю цифр. Тобто
         var = ‘91011’  є послідовністю, треба надрукувати ‘YES’.
         var = ‘10001003’ не є послідовністю, треба надрукувати ‘NO’
    """
    user_input = input("Введіть строку\n")
    temp_user_input = list(user_input)
    max_len = len(user_input) // 2
    for x in range(len(user_input)):
        if temp_user_input == 0:
            print(max_len)


def task_6():
    """(hackerrank) Юзер вводить пароль. Вивести на екран кількість символів, яких не вистачає
    щоб цей пароль був “складним”. Для того щоб пароль був складним потрібно, щоб пароль складався як мінімум із
    6 символів, містив у собі по одному символу із вказаних наборів:
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"
    """
    user_input = input("Введіть строку\n")
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"
    characters = [numbers, lower_case, upper_case, special_characters]
    password_len = len(user_input)
    counter = 4
    for word in characters:
        for letter in word:
            if letter in user_input:
                counter -= 1
                break
    if counter != 0 or password_len < 6:
        if counter > 6 - password_len:
            output("input {} more characters".format(counter))
        else:
            output("input {} more characters".format(6 - password_len))


if __name__ == "__main__":
    task_4()
