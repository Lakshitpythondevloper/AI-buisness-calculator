# Print background : -

print(r''' 
 ____        _        ____                          _             
| __ ) _   _(_)___   / ___|___  _ ____   _____ _ __| |_ ___  _ __ 
|  _ \| | | | / __| | |   / _ \| '_ \ \ / / _ \ '__| __/ _ \| '__|
| |_) | |_| | \__ \ | |__| (_) | | | \ V /  __/ |  | || (_) | |   
|____/ \__,_|_|___/  \____\___/|_| |_|\_/ \___|_|   \__\___/|_|   ''')


def convert_percentage(user_name):

    print(f"Okay {user_name}! You choose 1st option. Great!")

    user_total_item = int(input(f"Tell me {user_name}, What is your total number? It may be your marks, any thing, food items etc. Tell: "))
    user_obtain_item = int(input(f"Good! {user_name}! your total number is {user_total_item}. Now tell me the obtained number. It also may be your marks, any thing, food items etc as I say. Tell: "))


    # Calculating the percentage: -

    Percentage = user_obtain_item/user_total_item*100

    print("Here is a percentge:",float(Percentage),"%")

def find_discount_price(user_name1):

    print(f"Okay {user_name1}! You choose 2nd option. Great!")
    user_marked_price = float(input(f"Tell me {user_name1}, What is your marked price of your product? Tell me: "))
    user_discount = float(input(f"Good! {user_name1}! your marked price is {user_marked_price}. Now tell me the discount number of you product or food items. please don't use '%' sign with your discount number! Tell me: "))

    # Calculate the discount price: -

    price = user_discount/100*user_marked_price
    discount_price = user_marked_price-price
    print(f"Here is your discount price: {discount_price} ")
    user_feedback = input(f"{user_name1}! If you buy multiple products and each product has same discount, so do you like to calculate all product discount price?. Type 'yes' or 'No': ").capitalize()

    if user_feedback == 'Yes':
        print(f"I am extremely sorry for that {user_name1} 😔! I am currently developing my code 🏗️ and promise to share the fully developed update of this project soon on my GitHub repository.")
    else:
        print(f"Okay so we finish our this section {user_name1}! Thank you so much for talking with me.😀")

def find_marked_price(user_name2):

    print(f"Okay {user_name2}! You choose 4th option. Great!")
    user_selling_price = float(input(f"Tell me {user_name2}, What is your selling price of your product? Tell me: "))
    user_discount2 = float(input(f"Good! {user_name2}! your selling price is {user_selling_price}. Now tell me the discount number of you product or food items. please don't use '%' sign with your discount number! Tell me: "))

    # Calculate the marked price: -

    marked_price = (user_selling_price*100)/(100-user_discount2)
    print(f"Here is your marked price: {marked_price} ")

# Login/introduction: -
print("Welcome to buis convertor!")

ask_user_name = input("Please enter you name: ").capitalize()
print(f"Oh! hello {ask_user_name}! Welcome! Please select from the options I provided here. \n Here are your options: -\n 1. Convert percentage? \n 2. Find discount price? ? \n 3.Find marked price after dicount?")
print("\n")
print(f"What do you want to choose {ask_user_name}? Only type numbers")
user_response = input("Choose options: ")

# Conditions : -

if user_response == '1':
    convert_percentage(ask_user_name)
elif user_response == '2':
    find_discount_price(ask_user_name)
elif user_response == '3':
    find_marked_price(ask_user_name)
    

