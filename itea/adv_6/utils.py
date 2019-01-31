from datetime import date
import os
import pickle


class Sorting:

    def __init__(self, *args):
        self.attribute_names = args

    def __call__(self, instance):
        values = []

        for attr in self.attribute_names:
            values.append(getattr(instance, attr))

        return values


def load_rada():
    db_path = os.path.dirname(os.path.abspath(__file__)) + '/db.pickle'
    if not os.path.exists(db_path):
        return None

    with open(db_path, 'rb') as source:
        data = pickle.load(source)
    return data['rada']


def save_rada(rada):
    database_path = os.path.dirname(os.path.abspath(__file__)) + '/db.pickle'

    with open(database_path, 'wb') as target:
        pickle.dump({'rada': rada}, target)


class Counter:
    def __init__(self, count=0):
        self.count = count


class IntDescriptor(Counter):
    def __init__(self, count):
        super().__init__(count)
        count += 1

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        value = int(value)
        assert instance(value, int) and value > 0
        setattr(instance, self.name, value)

    def __delete__(self, instance):
        delattr(instance, self.name)


class StrDescriptor(Counter):
    def __init__(self, count):
        super().__init__(count)
        count += 1

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        value = str(value)
        assert instance(value, str) and len(value) > 2
        setattr(instance, self.name, value)

    def __delete__(self, instance):
        delattr(instance, self.name)


class DateDescriptor(Counter):
    def __init__(self, count):
        super().__init__(count)
        count += 1

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        day, month, year = value.split('-')
        value = date(int(year), int(month), int(day))
        assert instance(value, date)
        setattr(instance, self.name, value)

    def __delete__(self, instance):
        delattr(instance, self.name)
