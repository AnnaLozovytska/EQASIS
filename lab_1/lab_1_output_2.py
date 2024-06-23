class User:
    ENGINEER = 1
    MANAGER = 2

    def __init__(self, name, age, user_type, phone):
        self.name = name
        self.age = age
        self.user_type = user_type
        self.phone = phone

    def print_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Type: {'Engineer' if self.user_type == self.ENGINEER else 'Manager'}")
        print(f"Phone: {self.phone}")

# Приклад використання
user = User("John", 25, User.ENGINEER, "+380509379992")
user.print_details()
