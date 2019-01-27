import pickle


deputy_dict = dict()
fraction_dict = dict()


class Human:
    def __init__(self, weight, height):
        self.weight = weight
        self.height = height

    def __eq__(self, other):
        return self.weight == other.age and self.height == other.height

    def __hash__(self):
        return hash(self.height) + hash(self.weight)

    def __str__(self):
        return f'Weight {self.weight}. Height - {self.height}.'


class Deputat(Human):
    def __init__(self, last_name, name, date_of_birth, height, weight, bribe_taker=False, bribe_value=None):
        super().__init__(height, weight)
        self.last_name = last_name
        self.name = name
        self.date_of_birth = date_of_birth
        self.bribe_taker = bribe_taker
        self.bribe_value = bribe_value

    def __eq__(self, other):
        return self.last_name == other.last_name and \
               self.name == other.name and  \
               self.date_of_birth == other.date_of_birth and \
               self.bribe_taker == other.bribe_taker and \
               self.bribe_value == other.bribe_value

    def __hash__(self):
        return hash(self.last_name) + hash(self.name) + hash(self.date_of_birth) + hash(self.bribe_taker) + \
               hash(self.bribe_value)

    def __str__(self):
        if self.bribe_taker:
            return f'Name - {self.name}. Last name - {self.last_name}. Born in {self.date_of_birth}. \
             Bribe value {self.bribe_taker}.'
        else:
            return f'Name - {self.name}. Last name - {self.last_name}. Born in {self.date_of_birth}. Don`t take a bribe'

    def give_tribute(self, bribe):
        if not self.bribe_taker:
            print(f'Don`t take a bribe')
        else:
            print(f'{bribe}')
            self.bribe_taker = True
            if bribe >= 10000:
                print('The police will imprison the deputy')
            else:
                self.bribe_value = bribe

# ----------------------------------------------------------------------------------------------


class Fraction:

    def __init__(self, fraction_name):
        self.fraction_name = fraction_name

    def add_deputy(self):
        global deputy_dict
        count_deputy = 0
        name = input('Input name of deputy.\n')
        last_name = input('Input last name of deputy.\n')
        date_of_birth = input('Input date of birth\n')
        weight = input('Input weight of deputy\n')
        height = input('Input height of deputy\n')
        bribe_taker = input('Did the deputy takes bribe? If yes enter 1, in other way enter 0\n')
        if bribe_taker == '1':
            bribe_value = input('Input the bribe value\n')
        else:
            bribe_value = None
        count_deputy += 1
        deputy_dict[count_deputy] = Deputat(name, last_name, date_of_birth, weight, height, bool(bribe_taker),
                                            bribe_value)
        print(deputy_dict)

    def del_deputy(self):
        global deputy_dict
        temp_dict = dict()
        name = input('Input name of deputy.\n')
        last_name = input('Input last name of deputy.\n')
        date_of_birth = input('Input date of birth\n')
        weight = input('Input weight of deputy\n')
        height = input('Input height of deputy\n')
        bribe_taker = input('Did the deputy takes bribe? If yes enter 1, in other way enter 0\n')
        if bribe_taker == '1':
            bribe_value = input('Input the bribe value\n')
        else:
            bribe_value = None
        temp_dict['deputy'] = Deputat(name, last_name, date_of_birth, weight, height, bool(bribe_taker), bribe_value)
        for key in deputy_dict:
            if temp_dict['deputy'] == deputy_dict[key]:
                del_key = key
        del deputy_dict[del_key]
        print(deputy_dict)

# ------------------------------------------------------------------------------------------------

    def print_bribe_taker(self):
        """Відсортувати депутатів за хабарем(fanctor)"""
        pass

# ------------------------------------------------------------------------------------------------

    def print_bigest_bribe_taker(self):
        """Вивести найбільшого хабарника"""
        pass

# ------------------------------------------------------------------------------------------------

    def print_all_deputy_in_fraction(self):
        for key in deputy_dict:
            print(deputy_dict[key].__dict__)
            """Відсортувати депутатів за імям прізвищем(fanctor)"""


    def delete_all_deputy_from_fraction(self):
        for key in deputy_dict:
            del deputy_dict[key]

# ------------------------------------------------------------------------------------------------

    def is_deputy_in_fraction(self):
        pass


class VerkhovnaRada:

    def add_fraction(self):
        global fraction_dict
        fraction_name = input("Input fraction name\n")
        fraction_dict.add(Fraction(fraction_name))

    def del_fraction(self):
        global fraction_dict
        print(fraction_dict.__dict__)
        fraction_name = input("Input fraction name\n")
        for key in fraction_dict:
            if key == fraction_name:
                del_key = key
        del fraction_dict[del_key]

class DBOfVerchovnaRada:
    @staticmethod
    def read_from_DB():
        global deputy_dict, fraction_dict
        with open('deputys.pickle', 'rb') as deputys_target, open('fraction.pickle', 'rb') as fraction_target:
            deputy_dict = pickle.load(deputys_target)
            fraction_dict = pickle.load(fraction_target)

    @staticmethod
    def write_to_DB():
        global deputy_dict, fraction_dict
        with open('deputys.pickle', 'wb') as deputys_target, open('fraction.pickle', 'wb') as fraction_target:
                pickle.dump(deputy_dict, deputys_target, pickle.HIGHEST_PROTOCOL)
                pickle.dump(fraction_dict, fraction_target, pickle.HIGHEST_PROTOCOL)
