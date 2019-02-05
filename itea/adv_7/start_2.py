from functools import wraps


def contunie (func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        gen = func(*args, **kwargs)
        next(gen)
        return gen
    return wrapper


@contunie
def file_coroutine():
    while True:
        input_data = yield
        with open('final_numbers.txt', 'a') as target:
            target.write(f'{str(input_data)}\n')


@contunie
def filter_40_70(file_coroutine):
    while True:
        input_deta = yield
        if 40 < input_deta < 70:
            file_coroutine.send(input_deta)


@contunie
def even_filter(filter_40_70):
    while True:
        input_data = yield
        if input_data % 2 == 0:
            filter_40_70.send(input_data)

@contunie
def gen_number(even_filter):
    conter = 1
    while conter <= 100:
        yield
        even_filter.send(conter)
        conter += 1


if __name__ == '__main__':
    file = file_coroutine()
    f4070 = filter_40_70(file)
    efilter = even_filter(f4070)
    gen = gen_number(efilter)
    list(gen)

