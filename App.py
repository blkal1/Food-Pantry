import database_pantry
from datetime import datetime


MENU_PROMPT = """ ---Food Pantry ---

Please Choose one of these options:

1) Add a new product
2) See all my products
3) Find a product by name
4) Find a product by expiration date
5) Exit Process

What is your selection?: """


def menu():
    connection = database_pantry.connect()
    database_pantry.create_tables(connection)

    while (user_input := input(MENU_PROMPT)) != "5":
        if user_input == "1":
            product_name = input("Enter the name of the household product: ")
            quantity_number = int(input("Enter the number of household product: "))
            dick = str(input("Enter date (yyyy-mm-dd): "))
            expiration_date = datetime.strptime(dick, "%Y-%m-%d").date()
            house_rating = int(input("Enter your rating score for this product (0-100): "))

            database_pantry.add_food_pantry(connection, product_name, quantity_number, expiration_date, house_rating)

        elif user_input == "2":
            Food_Manager = database_pantry.get_all_pantry(connection)
            for food in Food_Manager:
                print(f"{food[1]}  ({food[2]}) ({food[3]}) - {food[4]}/100")

        elif user_input == "3":

            product_name = input("Enter a household product name to find: ")
            Food_Manager = database_pantry.get_all_pantry_by_name(connection, product_name)
            
            for food in Food_Manager:
                print(f"{food[1]}  ({food[2]})  ({food[3]}) - {food[4]}/100")

        elif user_input == "4":
            
            expiration_date = str(input('Enter the expiration date: ')) 
            Food_Manager = database_pantry.get_all_pantry_by_expiration_date(connection, expiration_date)
            
            for time in Food_Manager:
                print(f"{time[1]}  ({time[2]})  ({time[3]}) - {time[4]}/100")
                
        elif user_input == "5":
                
            product_name = input("Enter product to find: ")
            house_rating = database_pantry.get_fav_food(connection, product_name)
            
            print("The favorite household item for {product_name} is:  {house_rating[4]}")
                        
        else:
            print("Invalid input, try again!...ahahaha")
  


menu()