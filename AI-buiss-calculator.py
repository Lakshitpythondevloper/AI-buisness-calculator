# Print background : -
import Logo 
from prettytable import PrettyTable

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

def student_number_calculation(user_name3):
    
    print(Logo.logo_1)
    print(f"Welcome {user_name3}! 😉 in this section. Please give the information which asked in below.")
    user_prompt = int(input("Enter the total students number here in your class room:  "))

    student_list_name = []
    student_list_marks = []

    for students in range(0,user_prompt):
        student_name =  input(f"Enter the student names here please of your class {user_name3}:  ").title()
        student_list_name.append(student_name)

    # Ui for CLI
    print("")
    print("Okay here is a correct student name which you type: -") 
    print("")
    for deco in student_list_name:
        print(deco)
    print("")
    print("Now please enter the studnet marks here please with the total marks and subject!")
    print("")
    print(Logo.logo_3)
    total_marks = int(input("Enter the total marks of your exam please here in numerical:  "))
    subject = input("Enter the subject you want to print the numbers here please: ").title()
    print("")

    # Managing the Number of student
    for name in student_list_name:
        Marks_input = int(input(f"Enter the marks of {name} out of {total_marks} of {subject} subject:  "))
        student_list_marks.append(Marks_input)

    tabel = PrettyTable()
    tabel.field_names = ["Name", "Marks of student"]
    for names, marks in zip(student_list_name, student_list_marks):
        # Table formating
        tabel.add_row([names,marks])
    print(f"Here is a table of student marks of your {subject} subject : -")
    print(tabel)

    ask_user_prompt = input("Okay! I print the tables of your all students, now do you want to find the highest or lowest number of students? Type (Yes or No): ").lower()

    if ask_user_prompt =='yes':
        print("Okay!")
        ask_user_about_higher_or_lower = input("Do you want find high marks of which student or lower marks?: Type(H for higher or L for lower): ").capitalize()

        if ask_user_about_higher_or_lower == 'H':
            Higher_marks = max(student_list_marks)
            index = student_list_marks.index(Higher_marks)

            # Find the name of student
            student_higher_marks_name = student_list_name[index]
            print(f"Okay! here is a winne or 1st position student of your class {user_name3} 🏅: {student_higher_marks_name}")
        else:
            Lowest_marks = min(student_list_marks)
            index_lower = student_list_marks.index(Lowest_marks)

            # Find the name of student
            student_lowest_marks_name = student_list_name[index_lower]
            print(f"Okay!, sadly ☹️the lowest marks in your class is: {student_lowest_marks_name}. I hope it will done better.")
    else:
        print(Logo.logo_2)
        print(f"Okay {user_name3}! See you soon again 😀. Have a good day.")

# Login/introduction: -
print("Welcome to buis convertor!")

ask_user_name = input("Please enter you name: ").title()
print(f"Oh! hello {ask_user_name}! Welcome! Please select from the options I provided here. \n Here are your options: -\n 1. Convert percentage? \n 2. Find discount price? ? \n 3. Find marked price after dicount? \n 4. Student table printing and calculation")
print("\n")
print(f"What do you want to choose {ask_user_name}? Only type numbers! not in key words")
user_response = input("Choose options: ")

# Conditions : -

if user_response == '1':
    convert_percentage(ask_user_name)
elif user_response == '2':
    find_discount_price(ask_user_name)
elif user_response == '3':
    find_marked_price(ask_user_name)
elif user_response == '4':
    student_number_calculation(ask_user_name)
else:
    print("Sorry you type invalid numerical number or type another thing. Try again! ⚠️")

