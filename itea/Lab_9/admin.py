from user import User
class Admin(User):
    def __init__(self, privileges):
        self.privileges = privileges
        self.privileges = ['Allowed to add messages\n', 'Allowed to delete users\n', 'Allowed to ban users']


    def show_priveleges(self):
        print(self.privileges)
