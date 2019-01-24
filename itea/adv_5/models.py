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
    def __init__(self, last_name, name, date_of_bday, bribe_taker, bribe_value):
        self.last_name = last_name
        self.name = name
        self.date_of_bday = date_of_bday
        self.bribe_taker = bribe_taker
        self.bribe_value = bribe_value

    def __eq__(self, other):
        return self.last_name == other.last_name and \
               self.name == other.name and  \
               self.date_of_bday == other.date_of_bday and \
               self.bribe_taker == other.bribe_taker and \
               self.bribe_value == other.bribe_value

    def __hash__(self):
        return hash(self.last_name) + hash(self.name) + hash(self.date_of_bday) + hash(self.bribe_taker) + \
               hash(self.bribe_value)

    def __str__(self):
        return f'Weight {self.weight}. Height - {self.height}.'

