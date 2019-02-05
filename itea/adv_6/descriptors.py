from datetime import date


class Counter:
    counter = 0

    def __init__(self):
        Counter.counter += 1


class IntDescriptor(Counter):

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        value = int(value)
        assert value > 0
        assert type(value) in (int, float)
        setattr(instance, self.name, value)


class StrDescriptor(Counter):

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        assert isinstance(value, str)
        assert len(value.strip()) > 1
        setattr(instance, self.name, value.strip())


class DateDescriptor(Counter):

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
