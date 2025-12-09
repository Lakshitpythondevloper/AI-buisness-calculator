# Print background : -
import Logo 
from prettytable import PrettyTable

def programm():
        print(r''' 
    ____        _        ____                          _             
    | __ ) _   _(_)___   / ___|___  _ ____   _____ _ __| |_ ___  _ __ 
    |  _ \| | | | / __| | |   / _ \| '_ \ \ / / _ \ '__| __/ _ \| '__|
    | |_) | |_| | \__ \ | |__| (_) | | | \ V /  __/ |  | || (_) | |   
    |____/ \__,_|_|___/  \____\___/|_| |_|\_/ \___|_|   \__\___/|_|   ''')


        def convert_percentage(user_name):

            print(f"Okay {user_name}! Tumne 1st option choose kiyan hai. Great!")

            user_total_item = int(input(f"Achha btao {user_name}, tumhara total number kya hai? vah shayad tumahre marke bhi ho sakte hai, any thing, khanne ki chije etc. btao sirf number type karna!!: "))
            user_obtain_item = int(input(f"achha! {user_name}! tumhara total number ye hai {user_total_item}. achha ab mujhe ye btao ki tumhe kitne number mile ya bachhe. Jaisa ki maine btaya shayad ye tumhare marks ho sakte hai or khuch bhi . btao sirf number type karna!!: "))


            # Calculating the percentage: -

            Percentage = user_obtain_item/user_total_item*100

            print("Tikh hai bhai ye re tumhari percentage:",float(Percentage),"%")

        def find_discount_price(user_name1):

            print(f"Okay {user_name1}! Tumne 2nd option choose kiyan hai. Great!")
            user_marked_price = float(input(f"Achha btao {user_name1}, Tumhare product ki marked price kitni hai? Sirf number type karna!!: "))
            user_discount = float(input(f"Good! {user_name1}! tumhara marked price ye hai {user_marked_price}. Achha ab mujhe ye btao ki tumhare product ya khane ki chij par tumhe kitna discount mila hai. \n please bhai '%' iss sign ko tumhare number ke saath try mat karna ab jaldi btao: "))

            # Calculate the discount price: -

            price = user_discount/100*user_marked_price
            discount_price = user_marked_price-price
            print(f"Ye rahin tumhari discount price: {discount_price} ")
            user_feedback = input(f"{user_name1}! agar tum jayda product kharid te ho aur uska dicsount sabhi par same hai to kya tum um sabhi ka price niklwana chate ho?. Type 'yes' or 'No' or 'Na' ya 'Ha': ").capitalize()

            if user_feedback == 'Yes' or user_feedback == 'Ha':
                print(f"Sorry bahi mein dil se mafi chata hun {user_name1} 😔! Mein abhi apne code ko develop kar rah hun 🏗️ aur mein vayda karta hun ki isse mein jald hi GitHub repository mein dalunga.")
            else:
                print(f"Tikh hai to apn is session ko khalas karte hai bahi {user_name1}! Thank You for bat karne ke liye 😀")

        def find_marked_price(user_name2):

            print(f"Okay {user_name2}! Tumne 3rd option choose kiya hai. Great!")
            user_selling_price = float(input(f"Achha btao {user_name2}, Tumhari selling price kitni hai? Tell me: "))
            user_discount2 = float(input(f"Achha {user_name2}! tumhari seling price ye hai  {user_selling_price}. Achha merko ab uska discount btao jish par tumhare product par lga hai . please bhai '%' iss sign ko tumhare number ke saath try mat karna ab jaldi btao: "))

            # Calculate the marked price: -

            marked_price = (user_selling_price*100)/(100-user_discount2)
            print(f"Ye rahein tumhare product ke marked price jo tumne kharide hai{marked_price} ")

        def student_number_calculation(user_name3):
            
            print(Logo.logo_1)
            print(f"Welcome {user_name3}! 😉 in this section. Apni information yah dalna jo tumse phuche jayein. Vaise kya tum taecher hon? Kahr usee khuch farak nahin padta.")
            user_prompt = int(input("Tumahri class ke student ke total number type karein  "))

            student_list_name = []
            student_list_marks = []

            for students in range(0,user_prompt):
                student_name =  input(f"Apne student ke number type karien please {user_name3}:  ").title()
                student_list_name.append(student_name)

            # Ui for CLI
            print("")
            print("Okay! yeh rahein tumharre student naam: -") 
            print("")
            for deco in student_list_name:
                print(deco)
            print("")
            print("Ab yah student ke total marks aur uske subject ke bare mein yah dalein")
            print("")
            print(Logo.logo_3)
            total_marks = int(input("Tumhare jo exam tha vo kitne total number ka tha?:  "))
            subject = input("Tumahara subject konsa hai?: ").title()
            print("")

            # Managing the Number of student
            for name in student_list_name:
                Marks_input = int(input(f"{name} Iske yah marks dalon out of {total_marks} mein se. {subject} subject ke:  ")) # It is integer
                student_list_marks.append(Marks_input)

            tabel = PrettyTable()
            tabel.field_names = ["Name", "Marks of student"]
            for names, marks in zip(student_list_name, student_list_marks):
                # Table formating
                tabel.add_row([names,marks])
            print(f"Ye rahin tumhari tabel tum is copy karke kahin se bhi use kar sakte hon! : -")
            print(tabel)

            ask_user_prompt = input("Okay! AB meine yah table print kar de hai kya tum sabse jayda or kam kiske ayein hai yah janna chate hun Type (Yes or No) or (Ha aur Na): ").lower()

            if ask_user_prompt =='yes' or ask_user_prompt == 'ha':
                print("Okay!")
                ask_user_about_higher_or_lower = input("Kya tum student ke jayda marks janna chate hun ya kam?: Type (jayda ke liye H or kam ke liyein L): ").capitalize()

                if ask_user_about_higher_or_lower == 'H':
                    Higher_marks = max(student_list_marks)
                    index = student_list_marks.index(Higher_marks)

                    # Find the name of student
                    student_higher_marks_name = student_list_name[index]
                    print(f"Okay! ye raha tumahare winner studnet  {user_name3}, jo ki haiiii 🏅: {student_higher_marks_name}")
                else:
                    Lowest_marks = min(student_list_marks)
                    index_lower = student_list_marks.index(Lowest_marks)

                    # Find the name of student
                    student_lowest_marks_name = student_list_name[index_lower]
                    print(f"Okay!, sadly ☹️sabse kam tumahri class mein iske hai: {student_lowest_marks_name}. Mein ummid karta hun ki ye age jake achha karein ga.")
            else:
                print(Logo.logo_2)
                print(f"Okay {user_name3} bhai! Dubara milte hai 😀. Tumhara achha din jayein.")

            # Login/introduction: -
        print("Apka yha swagat hai!")

        ask_user_name = input("Karpya karke apna naam likheye: ").title()
        print(f"achha! hello {ask_user_name} bhai! Welcome! Yah se apn option choose karen jo app karvana chate hai: -. \n Ye rahen tumhare option: -\n 1. Percenatge mein badlna? \n 2. Discount price nikalna ? \n 3. Discount se phalein marked price nikalana \n 4. Bacche ke marks print karna or calculate karna.")
        print("\n")
        print(f"Tum kya choose karna chahoge {ask_user_name}? Sirf number type karna! keywords mein nahin: ")
        user_response = input("Option choose karein: ")

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
            print("Soory! tumne shayad galat number type kiya hain ya isse bahar ka number type kiya hai. dubara try karon! ⚠️")

tabel_hindi = PrettyTable()
tabel_hindi.field_names = ["Cautions ⚠️"]
tabel_hindi.add_row(["1. All langauge of this programm in Hindi so if you are a foreigner of Hindi language, You should go to english version of that programm."])
tabel_hindi.add_row(["2. It may contain joking part an friendly style talking in this programms, so don't angrey for that it is a programmed."])
tabel_hindi.add_row(["3. You can also write prompt in Hindi in english key words like 'Namsate!' or you can also type in english."])
print(tabel_hindi)

ask_user = input("Did you want to agree with cautions. Did we start in hindi? Type(Y/N): ").capitalize()

if ask_user == 'Y':
    print("Okay!")
    programm()
else:
    print("Sorry about going there ☹️. If you’re not comfortable with caution, you could try another English version that works better for you.")