from time import time


def task_1():
    """"""
    def timing(func):
        def inner(*args, **kwargs):
            start_time = time()
            func(*args, **kwargs)
            result = time() - start_time
            print(f'time is {result}')
            return result
        return inner

    custom_set = range(10000)
    custom_list = range(10000)

    new_list = custom_list + list(range(10**8 + 10**8 + 10000))

    @timing
    def set_test():
        for x in new_list:
            res = x in custom_set

    @timing
    def set_test():
        for x in new_list:
            res = x in custom_list


if __name__ == "__main__":
    task_1()
