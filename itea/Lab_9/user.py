class User:
    def __init__(self, first_name, last_name, age, login_attemps):
        self.login_attemps = int(login_attemps)
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


    def describe_user(self):
        print(f"my name is {self.first_name}\nlast name - {self.last_name}\nand i`m {self.age} years old")


    def greeting_user(self):
        print('Hi {}'.format(self.first_name))


    def increment_login_attempts(self):
        self.login_attemps += 1


    def reset_login_attempts(self):
        self.login_attemps = 0