users = {
    'Charles': {
        'first': 'Charles',
        'last': 'Babbage',
        'location': 'US',
        'age': 50
    },
    'Philip': {
        'first': 'Mark',
        'last': 'Philip',
        'location': 'UK',
        'age': 100
    },
}

for username, info in users.items():
    print(f"Username: {username}")
    full_name = info['first'] + " " + info['last']
    location = info['location']
    age = info['age']
    print(f"\tFull name: {full_name}")
    print(f"\tLocation: {location}")
    print(f"\tAge: {age}")

