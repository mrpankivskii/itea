import requests
from time import time
from threading import Thread, BoundedSemaphore

list_of_urls = ['http://24tv.ua', 'http://zik.ua', 'http://zaxid.net',
                'https://github.com/openprocurement',
                'https://www.youtube.com'] * 100


def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time()
        result = func(*args, *kwargs)
        print(time()- start_time)
        return result
    return wrapper


class TestThread(Thread):
    def __init__(self, name, list_of_urls, bounded_semaphore):
        super().__init__()
        self.name = name
        self.list_of_urls = list_of_urls
        self.bounded_semaphore = bounded_semaphore

    def run(self):
        with self.bounded_semaphore:
            for index, url in enumerate(self.list_of_urls):
                print(f'{self.name} {index} {url}')
                response = requests.get(url)
                list_of_urls_responses.append(response.status_code)


@timer
def main(number_of_threads):
    list_of_threads = []
    bounded_semaphore = BoundedSemaphore(5)
    for idx in range(number_of_threads):
        t = TestThread(f'test{idx}', list_of_urls[idx::num_of_threads],
                       bounded_semaphore)
        t.start()
        list_of_threads.append(t)
    _ = [t.join() for t in list_of_threads]


if __name__ == '__main__':
    for num_of_threads in range(10, 110, 10):
        global list_of_urls_responses
        list_of_urls_responses = []
        print(f'{num_of_threads}')
        main(num_of_threads)
