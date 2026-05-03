class Restaurant():
    def __init__(self, restaurantName, restaurantType):
        self.restaurantName= restaurantName
        self.restaurantType = restaurantType
        self.restaurantRating = 00
    
    def update_rating(self):
        newRating = input("The restaurant rating: ")
        self.restaurantRating = newRating


firstNewRestaurant = Restaurant("Chicken Foo", "Fast food" )
firstNewRestaurant.update_rating()

print(f"The restaurant name: {firstNewRestaurant.restaurantName}, its type is {firstNewRestaurant.restaurantType}, its rating equal to {firstNewRestaurant.restaurantRating}")




