class Restaurant():
    def __init__(self, restaurantName, restaurantType):
        self.restaurantName= restaurantName
        self.restaurantType = restaurantType
        self.restaurantRating = 00
        
    def describe_restaurant(self, restaurantSurface, numberWorkers):
        self.restaurantSurface = restaurantSurface
        self.numberWorkers = numberWorkers
        print(f"Our restaurant has a surface equal of: {restaurantSurface}, in this restaurant work: {numberWorkers}")

    def update_rating(self):
        newRating = input("The restaurant rating: ")
        self.restaurantRating = newRating


firstNewRestaurant = Restaurant("Chicken Foo", "Fast food" )
firstNewRestaurant.update_rating()

print(f"The restaurant name: {firstNewRestaurant.restaurantName}, its type is {firstNewRestaurant.restaurantType}, its rating equal to {firstNewRestaurant.restaurantRating}")




