def task_1():
    """Створіть новий файл numbers.txt  і запишіть у нього 10 чисел, кожне з нового рядка
    ( згенерувати модулем random від 1 до 100).
    Напишіть програму, яка зчитує ці числа з файлу і обчислює їх суму, виводить цю суму на екран
    і, водночас, записує цю суму у інший файл під назвою sum_numbers.txt
"""
    with open('numbers.txt', 'w') as numbers_file:
        for numbers in range(10):
            inp = input('Введіть число\n')
            numbers_file.write('{}{}'.format(inp, '\n'))
    summ = 0
    with open('numbers.txt', 'r') as numbers_file:
        for numbers in numbers_file:
            summ += int(numbers)
    print(summ)
    with open('sum_numbers.txt', 'w') as sum_file:
        sum_file.write(str(summ))


def task_2():
    """Створіть новий файл у текстовому редакторі і напишіть 3 рядки тексту у ньому про можливості Python.
    Кожен рядок повинен починатися з фрази: In Python you can ....
    Збережіть файл під ім’ям learning_python.txt.
    Напишіть функцію, яка зчитує файл і виводить текст
    з перебором рядків об’єкта файлу і зі збереженням рядків у списку з подальшим виведенням списку поза блоком with"""
    with open("lerning_python.txt", 'w') as python_file:
        for line in range(3):
            inp = input('Введіть можливість python3\n')
            python_file.write("In Python you can {}\n".format(inp))
    with open("lerning_python.txt", 'r') as python_file:
        file_list = ''
        for i in python_file:
            file_list += i
    print(file_list)


def task_3():
    """Функція replace() може використовуватися для заміни будь-якого слова у рядку іншим словом.
    Прочитайте кожен рядок зі створеного у попередньому завданні файлу learning_python.txt
    і замініть слово Python назвою іншої мови, наприклад C при виведенні на екран.
    Це завдання написати в окремій функції.
"""


def replace():
    with open("lerning_python.txt", 'r') as replace_file:
        file_line = replace_file.read()
        print(file_line.replace('Python', 'C'))


def task_4():
    """Завантажте текстову версію однієї з книг із сайту Project Gutenberg’s.
    Замініть усі розриви рядків у тексті символом пропуску
    і запишіть відформатований текст у новий файл formatted_text.txt.
"""
    with open('book.txt', 'r') as book_file:
        book = book_file.read()
    with open('formated_text.txt', 'w') as book_file:
        book_file.write(book.replace('\n', ' '))


def task_5():
    """Завантажте текстову версію книги
    The Life and Adventures of Robinson Crusoe By Daniel Defoe із сайту Project Gutenberg’s.
    Витягніть із тексту заголовки усіх розділів, які мають вигляд, на зразок: CHAPTER I—START IN LIFE.
    Запишіть знайдені назви у новий файл chapters.txt
"""
    with open('book2.txt', 'r') as book2_file,\
            open('chapters.txt', 'w') as chapters_file:
        for line in book2_file:
            if line.find('CHAPTER ') != -1:
                chapters_file.write("{}\n".format(line))


def task_6():
    """До попередньої задачі. Визначте відсоток малих і великих літер у тексті, що зберігається у файлі.
    Скористайтеся, як зразком вхідного файлу, текстовий файл із сайту Project Gutenberg’s.
    Використайте функцію isalpha()"""
    with open('book3.txt', 'r') as book3_file:
        text = book3_file.read()
    upper_count = 0
    lower_count = 0
    element_counter = 0
    for letter in text:
        element_counter += 1
        if letter.isalpha():
            if letter.isupper():
                upper_count += 1
            elif letter.islower():
                lower_count += 1
    all_letters = upper_count + lower_count
    percent_of_upper_letter = round((upper_count / all_letters) * 100)
    percent_of_lower_letter = round((lower_count / all_letters) * 100)
    print("apper - {}% \nlower - {}%\n{}".format(percent_of_upper_letter, percent_of_lower_letter,element_counter))


if __name__ == '__main__':
    task_6()
