class User:
    def __init__(self, first_name, last_name, age):
       # self.login_attemps = login_attempts
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    def describe_user(self):
        print(f"my name is {self.first_name}\nlast name - {self.last_name}\nand i`m {self.age} years old")

   # def increment_login_attempts(self):
     #   self.login_attemps += 1








if __name__ == "__main__":
    user = User('Vitalii', 'pankivskyi', '23')
    user.describe_user()