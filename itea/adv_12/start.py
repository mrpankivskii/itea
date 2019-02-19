from decimal import *
from datetime import datetime
from collections import namedtuple, deque
from math import fabs


def task_1():
    number = int(input())
    students = dict()
    for x in range(number):
        name = input().split(' ')
        students[name[0]] = [Decimal(x) for x in name[1:]]
    name2 = input()
    mark = Decimal(sum(students[name2]) / (len(name) - 1))
    print(mark.quantize(Decimal('0.01'), rounding=ROUND_05UP))


def task_2():
    """
2
Sun 10 May 2015 13:54:36 -0700
Sun 10 May 2015 13:54:36 -0000
Sat 02 May 2015 19:54:36 +0530
Fri 01 May 2015 13:54:36 -0000

    """
    date = list()
    number = int(input())*2
    for x in range(number):
        date.append(input())
        date[x] = datetime.strptime(date[x], '%a %d %b %Y %H:%M:%S %z')
    for x in range(number):
        if x % 2 == 0:
            dif = (date[x] - date[x+1]).total_seconds()
            print(int(fabs(dif)))


def task_3():
    """
5
ID         MARKS      NAME       CLASS
1          97         Raymond    7
2          50         Steven     4
3          91         Adrian     9
4          72         Stewart    5
5          80         Peter      6

    """
    number = int(input())  # enter number of students
    titles = input().split()  # eter titles
    TupleOfStudents = namedtuple('TupleOfStudents', ' '.join(titles))
    students = list()
    for x in range(number):
        student = input().split()  # enter students
        students.append(TupleOfStudents(*student))
    result = 0
    for x in students:
        result += int(x.MARKS)
    print(result/number)


def task_4():
    """
6
append 1
append 2
append 3
appendleft 4
pop
popleft

    """
    number = int(input())  # enter number of commands
    dec = deque()
    for x in range(number):
        command = input().split(' ')  # enter commands
        if command[0] == 'append':
            dec.append(command[1])
        elif command[0] == 'appendleft':
            dec.appendleft(command[1])
        elif command[0] == 'pop':
            dec.pop()
        elif command[0] == 'popleft':
            dec.popleft()
    print(' '.join(dec))


if __name__ == '__main__':
    task_2()
