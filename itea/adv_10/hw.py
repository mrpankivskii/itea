import requests
from time import time
from threading import Thread

list_of_urls = ['http://24tv.ua', 'http://zik.ua', 'http://zaxid.net', 'https://github.com/openprocurement',
                'https://www.youtube.com']


def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time()
        result = func(*args, *kwargs)
        end_time = time() - start_time
        print(end_time)
        return result
    return wrapper


counter = 0


@timer
def urls():
    for x in list_of_urls:
        t1 = TestThread(x)
        t1.start()
        t1.join()


class TestThread(Thread):
    def __init__(self, url):
        super().__init__()
        self.name = 'test'
        self.url = url

    def run(self):
        global counter
        counter += 1
        print(self.url, requests.get(self.url).status_code)


if __name__ == '__main__':
    urls()
