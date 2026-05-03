class Restaurant():
    def __init__(self, restaurantName, restaurantType):
        self.restaurantName= restaurantName
        self.restaurantType = restaurantType
    
    def describe_restaurant(self, restaurantSurface, numberWorkers):
        self.restaurantSurface = restaurantSurface
        self.numberWorkers = numberWorkers
        print(f"Our restaurant has a surface equal of: {restaurantSurface}, in this restaurant work: {numberWorkers}")

    # def open_restaurant(self):
    #     print("Welcome to our restaurant")


firstNewRestaurant = Restaurant("Chicken Foo", "Fast food")
secondNewRestaurant = Restaurant("Amazigh", "Algerian kitchen")
thirdNewRestaurant = Restaurant("Matrushka", "Russian kitchen")

print(f"The first restaurant is named {firstNewRestaurant.restaurantName}, its type is {firstNewRestaurant.restaurantType}")
print(f"The second restaurant is named {secondNewRestaurant.restaurantName}, its type is {secondNewRestaurant.restaurantType}")
print(f"The second restaurant is named {thirdNewRestaurant.restaurantName}, its type is {thirdNewRestaurant.restaurantType}")


firstNewRestaurant.describe_restaurant("140", 35)
secondNewRestaurant.describe_restaurant("180", 40)
thirdNewRestaurant.describe_restaurant("250", 80)


