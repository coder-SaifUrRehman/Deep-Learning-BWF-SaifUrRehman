class User:
    def __init__(self, first_name, last_name, age, gender, occupation):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.occupation = occupation

    def describe_user(self):
        print(f"User profile for {self.first_name} {self.last_name}:")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"Occupation: {self.occupation}")

    def greet_user(self):
        print(f"Hello, {self.first_name} Sir! Good Morning")


user1 = User("umer", "CH", 21, "male", "Loaffer(lol)")

user1.describe_user()
user1.greet_user()


class Admin(User):
    def __init__(self, first_name, last_name, age, gender, occupation):
        super().__init__(first_name, last_name, age, gender, occupation)
        self.privileges = ["you can add post", "you can delete post", "you can ban user"]

    def show_privileges(self):
        print(f"Admin {self.first_name} {self.last_name} has following privileges:")
        for privilege in self.privileges:
            print(f"\t {privilege}")

admin = Admin("Saif", "Ur Rehman", 21, "male", " Programmer")
admin.describe_user()
admin.greet_user()
admin.show_privileges()
