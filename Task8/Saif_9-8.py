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
        print(f"Greeting {self.first_name} Sir!")


class Privileges:
    def __init__(self):
        self.privileges = ["admin can add post", "admin can delete post", "admin can ban user"]

    def show_privileges(self):
        print("Admin has the following privileges:")
        for privilege in self.privileges:
            print("   " + privilege)


class Admin(User):
    def __init__(self, first_name, last_name, age, gender, occupation):
        super().__init__(first_name, last_name, age, gender, occupation)
        self.privileges = Privileges()

        
admin = Admin("Saif", "Ur Rehman", 1000, "male", "Programmer")
admin.describe_user()
admin.greet_user()
admin.privileges.show_privileges()

