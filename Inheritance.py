class User:
    def __init__ (self, email, first_name, last_name):
        self.email = email 
        self.first_name = first_name 
        self.last_name = last_name 

    def greeting(self):
        return f'Hi {self.first_name} {self.last_name}'


class AdminUser(User):
    def active_users(self):
        return '500'

tiffany = AdminUser('tiffany@devcamp.com', 'Tiffany', 'Hudgens')

kristine = User('kristine@devcamp.com', 'Kristine', 'Hudgens')

print(tiffany.active_users())
# print(kristine.active_users())  Kristine is not part of AdminUser class
print(kristine.greeting())
print(tiffany.greeting())


500
Hi Kristine Hudgens
Hi Tiffany Hudgens


