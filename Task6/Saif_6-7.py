# Define a dictionary representing a person
person1 = {
    "first_name": "Saif",
    "last_name": "Ur Rehman",
    "age": 21,
    "city": "Bahawalpur"
}

# Define a dictionary representing another person
person2 = {
    "first_name": "Maqsood",
    "last_name": "Ahmad",
    "age": 19,
    "city": "Isl"
}

person3 = {
    "first_name": "Ali",
    "last_name": "akber",
    "age": 21,
    "city": "Lahore"
}

people_list = [person1, person2, person3]

for person in people_list:
    print("First Name:", person["first_name"])
    print("Last Name:", person["last_name"])
    print("Age:", person["age"])
    print("City:", person["city"])
    print("next one")
