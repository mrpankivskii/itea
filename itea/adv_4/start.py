from models import IceCreamStand, Restaurant, Node, BinaryTree
from random import shuffle
from time import time


def task_3():
    """
Написати клас Restaurant. Конструктор ( метод __init__) має приймати 2 аргумента restaurant_name, cuisine_type
            ( cuisine - варіння, тобто тип приготування).
3.1 Написати метод describe_restaurant, що друкує інформацію про ресторан,
             метод open_restaurant,  що друкує інформацію про відкриття ресторану
3.2 Створити інстанс класу ресторан, викликати 2 методи.
3.3 Створити 3 ресторани ( 3 різні інстанси класу ресторан). Описати ( describe_restaurant ) для кожного інстансу.
3.4 Додати атрибут number_served до ресторану із дефолтним значенням - 0.  Створити інстанс класу ресторан,
            надрукувати кількість обслужених клієнтів.
            Змінити значення number_served, надрукувати знову кількість обслужених клієнтів.
3.5 Додати метод set_number_served. Викликати його в інстансу класу, перевірити результат.
            Додати метод increment_number_served.  Викликати цей метод, перевірити результат.
3.6 Створити клас IceCreamStand, що наслідується від Restaurant.
            Додати цьому класу атрибут flavors (різні смаки морозива) - це має бути список смаків.
            Написати метод, що показує ці flavors. Створити інстанс IceCreamStand, викликати цей метод.
3.7 Перемістити класи у модуль models.py ( стандартне місце для моделей).
            Із основного модуля імпортнути класи ресторану і морозива, викликати методи для перевірки.
"""
    restaurant_1 = Restaurant('best food', 'best')
    restaurant_2 = Restaurant('red dragon', 'japanese')
    restaurant_3 = Restaurant('italiano', 'italian')
    restaurant_1.describe_restaurant()
    restaurant_2.describe_restaurant()
    restaurant_3.describe_restaurant()
    restaurant_1.open_restaurant()
    print(f'served - {restaurant_1.number_served}')
    restaurant_1.set_number_served(8)
    print(f'served(set) - {restaurant_1.number_served}')
    restaurant_1.increment_number_served()
    print(f'served(increment) - {restaurant_1.number_served}')
    icecreamstand = IceCreamStand()
    icecreamstand.flavors_describe()


def task_4():
    """ Реалізувати бінарне дерево. Для цього створити клас BinaryTree. BinaryTree має мати атрибут root.
Елементами у бінарному дереві будуть інстанси класів Node. Клас Node має мати 2 атрибута left_node, right_node.
Запиляти метод def __contains__(self, key): як BinaryTree класу, так і Node класу. Цей метод має вертати True або False.
Створити список із 10 000 елементів. li = list(range(10000))  перемішати ці елементи from random imporrt shuffle.
Помістити елементи в бінарне дерево. Використати timing декоратор.
Перевірити програмно, що пошук по бінарному дереву працює швидше ніж пошук по списку.
Додати метод до бінарного дерева, який перебалансовує це дерево. Спробувати реалізувати друк БінДер
"""
    def timing(func):
        def inner(*args, **kwargs):
            start_time = time()
            func(*args, **kwargs)
            result = time() - start_time
            print(f'time is {result}')
            return result
        return inner
    tree = BinaryTree()
    node = Node(7)
    elements_list = list(range(10**6))
    tree.root = len(elements_list)//2
    shuffle(elements_list)
    for number in elements_list:
        tree.add_node(Node(number))

    @timing
    def binary_serch(number):
        if node.__contains__(number):
            print('find')

    @timing
    def list_serch(list, number):
        if number in list:
            print('find')
    binary_serch(70000)
    list_serch(elements_list, 70000)


def task_5():
    """Написати static_method ( із нижнім підчерком) декорато, щоб він працював аналогічно @staticmethod.
    Написати class_method  декоратор, щоб він працював аналогічно @classmethod декоратору."""
    def static_method(func):
        def inner(*args, **kwargs):
            result = func(*args, **kwargs)
            return result
        return inner


    def class_method(func):
        def inner(*args, **kwargs):
            result = func(*args, **kwargs)
            return result
        return inner


if __name__ == "__main__":
    task_4()


