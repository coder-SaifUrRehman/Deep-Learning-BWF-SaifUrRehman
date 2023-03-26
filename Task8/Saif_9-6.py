class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"The restaurant {self.restaurant_name} serves {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def display_flavors(self):
        print(f"Ice cream flavors available at" + self.restaurant_name.title() + " are: ")
        for flavor in self.flavors:
            print("\t" + flavor,end='')

ice_cream_stand = IceCreamStand("Bell n tell", "Ice Cream", ["Chocolate", "Vanilla", "Strawberry", "Apple"])
ice_cream_stand.describe_restaurant()
ice_cream_stand.display_flavors()

