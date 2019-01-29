import pickle


deputy_dict = {'1': 1}
fraction_dict = {'id': "name"}


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


class Fraction(Deputat):

    def __init__(self, fraction_name, last_name, name, date_of_birth, height, weight, bribe_taker, bribe_value):
        super().__init__(last_name, name, date_of_birth, height, weight, bribe_taker, bribe_value)
        self.fraction_name = fraction_name

    def add_deputy(self):
        global deputy_dict
        self.name = input('Input name of deputy.\n')
        self.last_name = input('Input last name of deputy.\n')
        self.date_of_birth = input('Input date of birth\n')
        self.weight = input('Input weight of deputy\n')
        self.height = input('Input height of deputy\n')
        self.bribe_taker = input('Did the deputy takes bribe? If yes enter 1, in other way enter 0\n')
        if self.bribe_taker == '1':
            self.bribe_value = input('Input the bribe value\n')
        else:
            self.bribe_value = None
        count = 0
        while count in deputy_dict:
            count += 1
        deputy_dict[count] = [self.name, self.last_name, self.date_of_birth, self.weight, self.height,
                                     bool(self.bribe_taker), self.bribe_value]
        print(deputy_dict)

    def del_deputy(self):
        global deputy_dict
        temp_dict = dict()
        self.name = input('Input name of deputy.\n')
        self.last_name = input('Input last name of deputy.\n')
        self.date_of_birth = input('Input date of birth\n')
        self.weight = input('Input weight of deputy\n')
        self.height = input('Input height of deputy\n')
        self.bribe_taker = input('Did the deputy takes bribe? If yes enter 1, in other way enter 0\n')
        if self.bribe_taker == '1':
            self.bribe_value = input('Input the bribe value\n')
        else:
            self.bribe_value = None
        temp_dict['deputy'] = [self.name, self.last_name, self.date_of_birth, self.weight, self.height,
                                     bool(self.bribe_taker), self.bribe_value]
        for key in deputy_dict:
            if temp_dict['deputy'] == deputy_dict[key]:
                del_key = key
        del deputy_dict[del_key]
        print(deputy_dict)

# ------------------------------------------------------------------------------------------------!!!!!!!!!!!!!!!!!!!!!!!

    def print_bribe_taker(self):
        print(deputy_dict)
        """Відсортувати депутатів за хабарем(fanctor)"""
        def sort(a):
            return a[7]
        id = 0
        temp_dict = dict()
        for values in deputy_dict.values():
            for index, x in enumerate(list(values)):
                print(x)
            '''
            if values[5] == True:
                id += 1
                temp_dict[id] = deputy_dict[values]'''
        print(sorted(temp_dict.values(), key=sort))

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


class VerkhovnaRada(Fraction):
    def __init__(self, fraction_name):
        super().__init__(fraction_name)

    def add_fraction(self):
        global fraction_dict
        print(fraction_dict)
        self.fraction_name = input("Input fraction name\n")
        count = 0
        while count in fraction_dict:
            count += 1
        fraction_dict[count] = self.fraction_name

    def del_fraction(self):
        global fraction_dict
        print(fraction_dict)
        fraction_name = input("Input fraction name\n")
        del_key = 0
        for key in fraction_dict:
            if key == fraction_name:
                del_key = key
        del fraction_dict[del_key]
        print(fraction_dict)

    def print_all_fractions(self):
        print(fraction_dict)
        for key in fraction_dict:
            if key != 'id':
                print(fraction_dict[key])

    def print_target_fraction(self, fraction_name):
        for key, x in fraction_dict.items():
            if x == fraction_name:
                print(fraction_dict[key])

    def add_deputy_to_target_fraction(self):
        self
    def  del_deputy_from_fraction(self):
        pass
    def print_all_bribe_takers_in_rada(self):
        pass
    def print_the_bigest_bribe_taker_in_rada(self):
        pass
    def print_all_deputy_in_rada(self):
        pass
    def is_deputy_in_rada(self):
        pass


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
