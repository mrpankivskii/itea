from threading import Thread, Condition
import requests
from queue import Queue

queue = Queue()
condition = Condition()


class First(Thread):
    def __init__(self, url):
        super().__init__()
        self.name = 'First_Thread'
        self.url = url

    def run(self):
        while_condition = AlmostAlwaysTrue(20)
        while while_condition:
            print(f'{self.name}{while_condition.counter}\n')
            condition.acquire()
            responce = requests.get(self.url)
            queue.put(responce.status_code)
            condition.notify()
            condition.release()


class Second(Thread):
    def __init__(self, f_name):
        super().__init__()
        self.name = 'Second_Thread'
        self.f_name = f_name

    def run(self):
        with open(self.f_name, 'w') as target:
            while_condition = AlmostAlwaysTrue(20)
            condition.acquire()
            while while_condition:
                if queue.empty():
                    condition.wait()
                print(f'{self.name}{while_condition.counter}\n')
                item = queue.get()
                target.write(f'{while_condition.counter}  {str(item)}\n')
            condition.release()


class AlmostAlwaysTrue:
    def __init__(self, counter):
        self.counter = counter
        self.start = 0

    def __bool__(self):
        if self.counter > 0:
            self.counter -= 1
            return True
        return False


if __name__ == '__main__':
    t1 = First('https://24tv.ua')
    t2 = Second('Result.txt')
    t1.start()
    t2.start()
    t1.join()
    t2.join()
