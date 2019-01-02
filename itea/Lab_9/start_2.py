from user import User
from admin import Admin


if __name__ == "__main__":
    user1 = User('Vitalii', 'Pankivskyi', '23', 0)
    user2 = User('Vitalik', 'Pankiv', '25', 0)
    user3 = User('Vita', 'Pankivska', '20', 0)
    user1.describe_user()
    user1.greeting_user()
    user2.describe_user()
    user2.greeting_user()
    user3.describe_user()
    user3.greeting_user()
    user1.increment_login_attempts()
    user1.increment_login_attempts()
    user1.increment_login_attempts()
    print(user1.login_attemps)
    user1.reset_login_attempts()
    print(user1.login_attemps)
    admin = Admin('')
    print(admin.privileges)
