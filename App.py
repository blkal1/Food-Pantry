import FoodPantryDB

MENU_PROMPT = '''
Please Choose one of these options:

1) Add a new product
2) See all my products
3) Find a product by name
4) See which is the home fav item
5) Exit Process

What is your selection: ? '''

def menu():
    connection = FoodPantryDB.connect()
    FoodPantryDB.create_tables(connection)

    while (user_input :=  input(MENU_PROMPT)) != "5":
        if user_input == "1":
            pass
        elif user_input == "2":
            pass
        elif user_input == "3":
            pass
        elif user_input == "4":
            pass
        else:   
            print("Invalid input, try again!...ahahaha")
                   
menu()