class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"The restaurant {self.restaurant_name} serves {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")
        
restaurant1 = Restaurant("ROYALS", "Asian")
restaurant2 = Restaurant("XYZ Resturant", "Abc")
restaurant3 = Restaurant("Abc Resturant", "XYZ")

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()
restaurant3.open_restaurant()
