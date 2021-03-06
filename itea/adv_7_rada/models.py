from utils import Sorting
from descriptors import IntDescriptor, StrDescriptor, DateDescriptor
from abc import ABC, abstractmethod

class RadaMetaClass(type):
    counter = 0

    def __new__(cls, name, bases, dct):
        new_dict = dict()
        for attr, value in dct.items():
            if attr == 'int_types':
                for el in dct[attr]:
                    new_dict[el] = IntDescriptor()
                    cls.counter += 1
            elif attr == 'str_types':
                for el in dct[attr]:
                    new_dict[el] = StrDescriptor()
                    cls.counter += 1
            else:
                new_dict[attr] = value

        return type.__new__(cls, name, bases, new_dict)


class Human(metaclass=RadaMetaClass):
    """This is doc"""
    int_types = ['weight', 'height']

    def __init__(self, weight, height):
        self.weight = weight
        self.height = height

    def __hash__(self):
        return hash(self.weight) + hash(self.height)

    def __eq__(self, other):
        if self.weight == other.weight and \
                self.height == other.height:
            return True
        return False


class Deputat(Human, ABC, metaclass=RadaMetaClass):
    str_types = ['surname', 'name']

    date_of_birth = DateDescriptor()

    def __init__(self, surname, name, date_of_birth, weight, height):
        super().__init__(weight, height)
        self.surname = surname
        self.name = name
        self.date_of_birth = date_of_birth

    def __hash__(self):
        return hash(self.surname) + \
               hash(self.name) + \
               hash(self.date_of_birth)

    def __eq__(self, other):
        if self.surname == other.surname and \
                self.name == other.name and \
                self.date_of_birth == other.date_of_birth:
            return True
        return False

    def __str__(self):
        return f'{self.name} {self.surname}'


class UKDeputat(Deputat):
    def __init__(self, surname, name, date_of_birth, weight, height, bribe_taker):
        super().__init__(surname, name, date_of_birth, weight, height)
        self.bribe_taker = bribe_taker
        self.bribes_amount = 0

    def give_tribute(self):
        if not self.bribe_taker:
            print(f'{self} doesnt take bribes')
        else:
            bribe_amount = int(input("Entre bribe amount\n"))
            if bribe_amount > 10000:
                print("Міліція ув’язнить депутата")
            else:
                self.bribes_amount += bribe_amount


class PLDeputat(Deputat):
    def __init__(self, surname, name, date_of_birth, weight, height):
        super().__init__(surname, name, date_of_birth, weight, height)


class Spiker(Human):
    def delete_all_bribe_taker_from_Verhovna_rada(self):
        pass


class Fraction(ABC):
    name = StrDescriptor()

    @abstractmethod
    def __init__(self, name):
        self.name = name
        self.deputats = set()

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        if self.name == other.name:
            return True
        return False

    def __str__(self):
        return f'Name: {self.name}. Deputats: {len(self.deputats)}'

    def add_deputat(self, deputat):
        if deputat in self.deputats:
            print(f'{deputat} already in fraction')
        else:
            self.deputats.add(deputat)

    def remove_deputat(self, deputat):
        if deputat in self.deputats:
            self.deputats.remove(deputat)
            print(f'{deputat} was removed')
        else:
            print(f'{deputat} is not in {self}')

    def print_all_deputats(self):
        sorted_list = list(self.deputats)
        sorted_list.sort(key=Sorting('name', 'surname'))
        for dep in sorted_list:
            print(dep)

    def clear(self):
        self.deputats = set()
        print(f'{self} is empty')

    def __contains__(self, deputat):
        if deputat in self.deputats:
            return True
        return False


class UKFraktion(Fraction):

    def print_all_bribe_takers(self):
        sorted_list = list(self.deputats)
        sorted_list.sort(key=Sorting('bribes_amount'))
        for dep in sorted_list:
            if dep.bribe_taker:
                print(dep)

    def get_biggest_bribe_taker(self):
        sorted_list = list(self.deputats)
        sorted_list.sort(key=Sorting('bribes_amount'))
        max_bribe_amount = sorted_list[0]
        if max_bribe_amount.bribe_taker:
            return max_bribe_amount

    @staticmethod
    def get_deputat():
        surname = input('Enter surname\n')
        name = input('Enter name\n')
        date_of_birth = input('Enter date_of_birth\n')
        weight = input('Enter weight\n')
        height = input('Enter height\n')
        bribe_taker = input('Enter bribe_taker\n')
        deputat = UKDeputat(surname, name, date_of_birth, weight, height, bribe_taker)
        return deputat


class PLFraction(Fraction):

    @staticmethod
    def get_deputat():
        surname = input('Enter surname\n')
        name = input('Enter name\n')
        date_of_birth = input('Enter date_of_birth\n')
        weight = input('Enter weight\n')
        height = input('Enter height\n')
        deputat = PLDeputat(surname, name, date_of_birth, weight, height)
        return deputat


class VerhovnaRada(ABC):

    def __init__(self):
        self.fractions = set()

    def add_fraction(self):
        fraction_name = input('Enter fraction name\n')
        self.fractions.add(Fraction(fraction_name))

    def remove_fraction(self):
        fraction_name = input('Enter fraction name\n')
        self.fractions.discard(Fraction(fraction_name))

    def print_all_fractions(self):
        for fraction in self.fractions:
            print(fraction)
            fraction.print_all_deputats()

    def add_deputat_to_fraction(self, fraction, deputat):
        fraction.add_deputat(deputat)

    def remove_deputat_fromm_fraction(self, fraction, deputat):
        fraction.remove_deputat(deputat)

    def show_all_bribe_takers(self):
        for fraction in self.fractions:
            fraction.print_all_bribe_takers()

    def show_biggest_bribe_taker(self):
        all_deputats = set()
        for fraction in self.fractions:
            all_deputats.union(fraction.deputats)

        sorted_list = list(all_deputats)
        sorted_list.sort(key=Sorting('bribes_amount'))
        max_bribe_amount = sorted_list[0]
        if max_bribe_amount.bribe_taker:
            print(max_bribe_amount)

    def show_all_deputats(self):
        for fraction in self.fractions:
            fraction.print_all_deputats()

    def __contains__(self, fraction):
        if fraction in self.fractions:
            return True
        return False


class UKRada(VerhovnaRada):
    pass


class PLRada(VerhovnaRada):
    pass