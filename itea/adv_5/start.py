from time import time


<<<<<<< HEAD
def test_1():
=======
def task_1():
>>>>>>> 4b0fb9bd485bec4fe92f6f5db97bf78e0f0fce73
    """"""
    def timing(func):
        def inner(*args, **kwargs):
            start_time = time()
            func(*args, **kwargs)
            result = time() - start_time
            print(f'time is {result}')
            return result
        return inner

<<<<<<< HEAD
    custom_set = set(range(100000))
    custom_list = list(range(100000))
    new_list = custom_list + list(range(10**8, 10**8 + 100000))
=======
    custom_set = range(10000)
    custom_list = range(10000)

    new_list = custom_list + list(range(10**8 + 10**8 + 10000))
>>>>>>> 4b0fb9bd485bec4fe92f6f5db97bf78e0f0fce73

    @timing
    def set_test():
        for x in new_list:
            res = x in custom_set

    @timing
<<<<<<< HEAD
    def list_test():
        for x in new_list:
            res = x in custom_list
    set_test()
    list_test()


def task_0():
    """Створити базовий клас для машин (Car). Інстанси класу мають мати такі атрибути ( fields):
 type (gas, electron, petrol),  model, year, max speed.
Написати методи цьому класу: get_car_type, change_type
Створити дочірні класи для кожного типу машини(Gas, Electron, Petrol )

0.0) Cтворити інстанс класу Car
       Викликати метод get_car_type, надрукувати те, що вернув цей метод
       Викликати метод change_type, потім викликати знову get_car_type, перевірити що все працює


0.1) Базовий кейс, абстрактний метод.
Вдосконалити попереднє завдання, щоб код працював наступним чином:
car = Car('BMW', 2018, 300)
petrol_car = car.set_car_type('petrol')  # It returns `PetrolCar` instance.
petrol_car.get_model()  # Returns `BMW`
petrol_car.get_year()  # Returns 2018
petrol_car.get_max_speed()  # Returns 300
gas_car = car.set_car_type('gas')  # It returns `GasCar` instance.
"""




if __name__ == "__main__":
    test_1()
=======
    def set_test():
        for x in new_list:
            res = x in custom_list


if __name__ == "__main__":
    task_1()
>>>>>>> 4b0fb9bd485bec4fe92f6f5db97bf78e0f0fce73
