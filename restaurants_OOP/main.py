from restaurant_hw import Restaurant

"A OOP program with different types of cuisine that gest input for number of customer served"

def main():
    japanese_restaurant = Restaurant(
        name = "kawasaki sushi",
        cuisine = "japanese food",
        # number_served = 33
    )

    chinease_restaurant = Restaurant(
        name = "niam yam",
        cuisine = "chinease food"
    )

    russian_restaurant = Restaurant(
        name = "babushka's",
        cuisine = "russian food",
        # number_served = 16
    )

    print(japanese_restaurant.describe_restaurant())
    print(japanese_restaurant.open_restaurant())
    japanese_restaurant.set_number_served()
    print(japanese_restaurant.restaurant()) 
    japanese_restaurant.increment_number_served()
    print(japanese_restaurant.restaurant()) 
    print(chinease_restaurant.describe_restaurant())
    print(chinease_restaurant.open_restaurant())
    print(chinease_restaurant.restaurant())
    print(russian_restaurant.describe_restaurant())
    print(russian_restaurant.open_restaurant())
    print(russian_restaurant.restaurant())
     
if __name__ == "__main__":
    main()