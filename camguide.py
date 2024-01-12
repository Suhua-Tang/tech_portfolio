'''
This is my first portfolio project, which functions as a tour guide for \
tourists visiting Cambridge.

'''

# request information on the user name, and display greeting! 

first_name = input("What's your first name? ").capitalize()

print(first_name,"welcome to Cambridge!")
print("My name is Camguide, your local tour guide in Cambridge. \n")
print("I can make some recommendations for a one-day tour based on your budget. \n")# make recommendations as a guide
print("Enter 'q' to quit the enquiry\n")

while True: # request budget information from the user between 0 and 100 pounds

    try: 
        budget = input("Please enter your budget between 0 to 100 pounds : ")
        if budget == 'q':
            break
        elif float(budget) == 0: # when the budget is equal to 0
            print("There are many places of interest that you can visit for free. \
Cambridge University and Fitzwilliam Museums are the major tourist attractions in this category.\n")
            
            while True: # request the user to enter uni or museum.  

                try:
                    free_destination = input("Enter 'Uni' or 'Mus' for more information: ").capitalize()
                    if free_destination == "Mus":
                        print("Housing over half a million objects, the Fitzwilliam \
has an amazing variety of beautiful artefacts and art from around the world. \
See everything from Egyptian coffins to Impressionist masterpieces; \
illuminated manuscripts to Renaissance sculpture; rare coins to Asian arts.\
For more information, visit their website at https://fitzmuseum.cam.ac.uk/ \n")
                        break
                    elif free_destination == "Uni":
                            print("Cambridge, home to the world-renown University of Cambridge, consisits of 31 colleges: \n")             
                            cambridge_college_list = ["Christ's College", "Churchill College", "Clare College", "Clare Hall", \
                                        "Corpus Christi College", "Darwin College", "Downing College", "Emmanuel College", \
                                        "Fitzwilliam College", "Girton College", "Gonville and Caius College", \
                                        "Homerton College", "Hughes Hall", "Jesus College", "King's College", \
                                        "Lucy Cavendish College", "Magdalene College", "Murray Edwards College",\
                                        "Newnham College", "Pembroke College", "Peterhouse", "Queens' College", \
                                        "Robinson College", "St Catharine's College", "St Edmund's College", \
                                        "St John's College", "Selwyn College", "Sidney Sussex College", \
                                        "Trinity College", "Trinity Hall", "Wolfson College"]
                            cambridge_college_list.sort()
                            user_college_input=list(enumerate(cambridge_college_list, start=1))
                            print(user_college_input)

                            while True: # user might be interested in different colleges, therefore, keep requesting info until until the condition to break is met, in this case, when 'exit' is entered.
                                try:
                                    college = input("Please enter number of the college you are interested in.\
 Enter 'exit' if not interested : ")
                                    if college == "exit":
                                        break
                                    elif college == "1":
                                        print("Christ's College is thought to have the oldest outdoor swimming pool in \
 the UK, dating from the mid 17th century. ")
                                        continue
                                    elif college == "2":
                                        print("Are you a fan of Churchill's speeches? \
If so, ou can read them first hand in the college, where originals of the great speeches are kept there!")
                                        continue
                                    elif college == "3":
                                        print("Clare Hall maybe Cambridge's most family-friendly college, \
with group meals held every month!")
                                        continue
                                    elif college == "4":
                                        print("In Clare’s vibrant courtyard, where the River Cam gracefully flows, \
students dance through academic pursuits and the lively May Ball")
                                        continue
                                    elif college == "5":
                                        print("The college has a famous clock that chimes 101 times each night, \
a nod to the original 100 scholars supported by the college")
                                        continue
                                    elif college == "6":
                                        print("Darwin College has the distinction of being the first graduate college,\
 with its students working towards Masters degrees or PhDs.")
                                        continue
                                    elif college == "7":
                                        print("The stunning architecture and \
gardens at Downing are bound to take your breath away")
                                        continue
                                    elif college == "8":
                                        print("Emmanuel, where the legacy of Sir David Attenborough meets the modern \
pulse of student life in a dynamic fusion of past and present.")
                                        continue
                                    elif college == "9":
                                        print("Welcome to the 'the Best of the Old and the New' college. \
Fitzwilliam College is home to a dynamic, welcoming international community!")
                                        continue
                                    elif college == "10":
                                        print("Girton college was Britain's first residential college for women \
offering a degree-level education!")
                                        continue
                                    elif college == "11":
                                        print("Gonville and Caius, where the ancient Tree Court stands \
witness to centuries of academic growth and flourishing traditions")
                                        continue
                                    elif college == "12":
                                        print("Homerton College has a rich legacy offering high-quality teacher training. \
It became a full college of the university in 2010.")
                                        continue
                                    elif college == "13":
                                        print("Hughes Hall has a reputation for its inclusive and friendly atmosphere.")
                                        continue
                                    elif college == "14":
                                        print("stands out for its historic charm, characterized by a blend of medieval \
and neoclassical architecture, and Jesus's college is renowned for \
fostering a close-knit academic community in the heart of Cambridge.")
                                        continue
                        
                                    elif college == "15":
                                        print("King's college is renowned for its Festival of Nine Lessons and Carols, \
a Christmas Eve service broadcast to millions worldwide.")
                                        continue
                                    elif college == "16": 
                                        print("Lucy Cavendish College has a focus on providing a supportive environment \
for mature female students returning to education.")
                                        continue
                                    elif college == "17":
                                        print("Magdalene, where the riverside tranquility meets the scholarly echoes \
of Samuel Pepys in the heart of a picturesque haven.")
                                        continue
                                    elif college == "18":
                                        print("Murray Edwards, where sisterhood reigns in a haven of academic pursuit,\
celebrating the power of women in the scholarly narrative")
                                        continue
                                    elif college == "19":
                                        print("As one of the oldest women's colleges at Cambridge,Newnham College has \
a beautiful garden known as 'The Pfeiffer.'")
                                        continue
                                    elif college == "20":
                                        print("Pembroke, where the timeless beauty of its gardens and the echoes \
of John Maynard Keynes' wisdom create an oasis of academic inspiration.")
                                        continue
                                    elif college == "21":
                                        print("The college has a beautiful deer park known as \"The Grove.\"")
                                        continue
                                    elif college == "22":
                                        print("Queen's boasts its unique Mathematical Bridge, spanning the River Cam!")
                                        continue
                                    elif college == "23":
                                        print("Robinson College is known for its striking stainless steel sculpture, \
the \"Millennium Needle.\"")
                                        continue
                                    elif college == "24":
                                        print("The college has a strong tradition of music and choral performances.")
                                        continue
                                    elif college == "25":
                                        print("Sidney Sussex, where the red-brick allure echoes the footsteps of Oliver\
 Cromwell, inviting students to history-rich halls.")
                                        continue
                                    elif college == "26":
                                        print("with a mix of historic and modern buildings, the college is known \
for its beautiful Fellows' Garden.")
                                        continue    
                                    elif college == "27":
                                        print("The postgraduate college is known for its vibrant social life and \
events with a diverse international community. ")
                                        continue
                                    elif college == "28": 
                                        print("The college has a famous choir that performs at various events and \
has a tradition of May Ball, an extravagant end-of-year celebration.")
                                        continue
                                    elif college == "29":
                                        print("At Trinity, where genius blooms in the shadows of Sir Isaac Newton, \
the pursuit of knowledge is as grand as the college's historic stature.")
                                        continue
                                    elif college == "30":
                                        print("Trinity Hall has a beautiful riverside location along the River Cam.")
                                        continue
                                    elif college == "31":
                                        print("Wolfson, the graduate hub where modernity meets academic brilliance, \
and the annual 'Gaudy' forms a bridge across generations of achievement.")
                                        continue
                                    else:
                                        print("College not found! Please try again")                         
                                except ValueError: 
                                        print("Invalid input.Please try again")
                            break
                    else:
                        print("Invalid input! Enter 'Uni' or 'Museum' for more information: ")
                        break
                except ValueError:
                    print("Invalid input! Try again.")

        elif 0 < float(budget) <= 20: # when the budget is less than 20 pounds
            print("There are some historical pubs, like Eagle, souvenir shops \
you can visit in Cambridge! And you can sign up for shared punting!")
            continue
        elif 20 < float(budget) <= 50: # when the budget is more than 20 pounds but less than 50 pounds
            print("You can book a ticket to have a musical feast in King's College Chapel, \
which costs between 20 and 50 pounds depending on the occassion!")
            continue

        elif 50 < float(budget) <=100: # when the budget is more than between 50 but less than 100 pounds
            print("You can hire a punt and punt with your friends, getting a \
glimpse into the prestigious private gardens and a sample of some of the local wildlife – predominantly ducks and swans!")
            continue
        else: # when the budget is outside the range 0-100 pounds
            print("Sorry, I don't have any recommendation for your budget!")
            
    except ValueError: # when the entry is not a number
        print("Invalid input! Please enter a valid number.")

