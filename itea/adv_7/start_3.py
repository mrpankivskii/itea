my_list = ['a', 'b', 'c', 'd']


def my_enumerate(elements):
    counter = 0
    while counter < len(elements):
        yield counter, elements[counter]
        counter += 1


def test():
    for index, data in my_enumerate(my_list):
        print(f'{index}, {data} - my enumerate')
    for ingex, data in enumerate(my_list):
        print(f'{ingex}, {data} - enumerate')


if __name__ == '__main__':
    test()
