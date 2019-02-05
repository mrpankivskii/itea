from functools import wraps


def contunie (func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        gen = func(*args, **kwargs)
        next(gen)
        return gen
    return wrapper

@contunie
def seen_words():
    output_data = False
    cache = set()
    while True:
        input_data = yield output_data
        if input_data in cache:
            output_data = True
        else:
            cache.add(input_data)
            output_data = False


if __name__ == '__main__':
    gen = seen_words()
    print(gen.send('mtea'))
    print(gen.send('itea'))
    print(gen.send('itea'))
