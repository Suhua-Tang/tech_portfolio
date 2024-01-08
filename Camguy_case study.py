# request information on the user name, and display greeting! 

first_name = input("What's your first name? ").capitalize()

print(first_name, ", welcome to Cambridge! I'm CamGuy, your personal tour guide in Cambridge. \n")


print("If you don't know how to make the most of your stay here. I can make some recommendations for one day tour based on your budget. \n")# make recommendations as a guide

while True: # request information from the user, until a number between 0 and 100 pounds is input
    

    try: 
        budget = float(input("Please enter your budget between 0 to 100 pounds : "))
        
        if budget == 0: # when the budget is equal to 0
            print("There are many places of interest that you can visit for free. Cambridge University and Fitzwilliam Museums are the major tourist attractions in this category.\n")
            
            while True: # request information from the user, until either uni or museum is entered.
                try:
                    free_destination = input("Enter 'Uni' or 'Museum' for more information: ").capitalize()
                    if free_destination == "Museum":
                        print("Housing over half a million objects, the Fitzwilliam has an amazing variety of beautiful artefacts and art from around the world. See everything from Egyptian coffins to Impressionist masterpieces; illuminated manuscripts to Renaissance sculpture; rare coins to Asian arts.")
                        break
                    elif free_destination == "Uni":
                            print("Cambridge is home to the world-renown University of Cambridge.Do you know that the University of Cambridge is composed of 31 colleges: Christ's College, Churchill College, Clare College, Clare Hall, Corpus Christi College, Darwin College, Downing College, Emmanuel College, Fitzwilliam College, Girton College, Gonville and Caius College, Homerton College, Hughes Hall, Jesus College, King's College, Lucy Cavendish College, Magdalene College, Murray Edwards College, Newnham College, Pembroke College, Peterhouse, Queens' College, Robinson College, St Catharine's College, St Edmund's College, St John's College, Selwyn College, Sidney Sussex College, Trinity College, Trinity Hall, Wolfson College")
                            
                            
                            while True: # user might be interested in different colleges, therefore, keep requesting info until until the condition to break is met, in this case, when 'exit' is entered.
                                try:
                                    college = input("Please enter the college you are interested in. Enter 'exit' if not interested : ").lower()
                                    if college == "exit":
                                        break
                                    elif college == "christ's":
                                        print("Christ's College is thought to have the oldest outdoor swimming pool in the UK, dating from the mid 17th century. ")
                                        continue
                                    elif college == "fitzwilliam":
                                        print("Welcome to the 'the Best of the Old and the New' college. Fitzwilliam College is home to a dynamic, welcoming international community!")
                                        continue
                                    elif college == "churchill":
                                        print("Are you a fan of Churchill's speeches? If so, ou can read them first hand in the college, where originals of the great speeches are kept there!")
                                        continue
                                    elif college == "clare hall":
                                        print("Clare Hall maybe Cambridge's most family-friendly college, with group meals held every month!")
                                        continue
                                    elif college == "darwin":
                                        print("Darwin College has the distinction of being the first graduate college, with its students working towards Masters degrees or PhDs.")
                                        continue
                                    elif college == "girton":
                                        print("It was Britain's first residential college for women offering a degree-level education!")
                                        continue
                                    elif college == "queen's":
                                        print("Queen's boasts its unique Mathematical Bridge, spanning the River Cam!")
                                        continue
                                    elif college == "st.john's": 
                                        print("The college has a famous choir that performs at various events and has a tradition of May Ball, an extravagant end-of-year celebration.")
                                        continue
                                    elif college == "king's":
                                        print("King's college is renowned for its Festival of Nine Lessons and Carols, a Christmas Eve service broadcast to millions worldwide.")
                                        continue
                                    elif college == "lucy cavendish": 
                                        print("Lucy Cavendish College has a focus on providing a supportive environment for mature female students returning to education.")
                                        continue
                                    elif college == "newnham":
                                        print("As one of the oldest women's colleges at Cambridge,Newnham College has a beautiful garden known as 'The Pfeiffer.'")
                                        continue
                                    elif college == "corpus christi":
                                        print("The college has a famous clock that chimes 101 times each night, a nod to the original 100 scholars supported by the college")
                                        continue
                                    elif college == "hughes hall":
                                        print("Hughes Hall has a reputation for its inclusive and friendly atmosphere.")
                                        continue
                                    elif college == "homerton":
                                        print("Homerton College has a rich legacy offering high-quality teacher training. It became a full college of the university in 2010.")
                                        continue
                                    elif college == "peterhouse":
                                        print("The college has a beautiful deer park known as \"The Grove.\"")
                                        continue
                                    elif college == "downing":
                                        print("The stunning architecture and gardens at Downing are bound to take your breath away")
                                        continue
                                    elif college == "selwyn":
                                        print("The college has a strong tradition of music and choral performances.")
                                        continue
                                    elif college == "st. catharine's":
                                        print("with a mix of historic and modern buildings, the college is known for its beautiful Fellows' Garden.")
                                        continue
                                    elif college == "trinity hall":
                                        print("Trinity Hall has a beautiful riverside location along the River Cam.")
                                        continue
                                    elif college == "st. edmund's":
                                        print("The postgraduate college is known for its vibrant social life and events with a diverse international community. ")
                                        continue
                                    elif college == "robinson":
                                        print("Robinson College is known for its striking stainless steel sculpture, the \"Millennium Needle.\"")
                                        continue
                                    elif college == "pembroke":
                                        print("Pembroke, where the timeless beauty of its gardens and the echoes of John Maynard Keynes' wisdom create an oasis of academic inspiration.")
                                        continue
                                    elif college == "magdalene":
                                        print("Magdalene, where the riverside tranquility meets the scholarly echoes of Samuel Pepys in the heart of a picturesque haven.")
                                        continue
                                    elif college == "gonville and caius":
                                        print("Gonville and Caius, where the ancient Tree Court stands witness to centuries of academic growth and flourishing traditions")
                                        continue
                                    elif college == "emmanuel":
                                        print("Emmanuel, where the legacy of Sir David Attenborough meets the modern pulse of student life in a dynamic fusion of past and present.")
                                        continue
                                    elif college == "sidney sussex":
                                        print("Sidney Sussex, where the red-brick allure echoes the footsteps of Oliver Cromwell, inviting students to history-rich halls.")
                                        continue
                                    elif college == "murray edwards":
                                        print("Murray Edwards, where sisterhood reigns in a haven of academic pursuit, celebrating the power of women in the scholarly narrative")
                                        continue
                                    elif college == "wolfson":
                                        print("Wolfson, the graduate hub where modernity meets academic brilliance, and the annual 'Gaudy' forms a bridge across generations of achievement.")
                                        continue
                                    elif college == "clare":
                                        print("In Clare’s vibrant courtyard, where the River Cam gracefully flows, students dance through academic pursuits and the lively May Ball")
                                        continue
                                    elif college == "king's":
                                        print("In King's realm, where the majestic chapel whispers tales of tradition, students embark on a harmonious journey of academic brilliance.")
                                        continue
                                    elif college == "trinity":
                                        print("At Trinity, where genius blooms in the shadows of Sir Isaac Newton, the pursuit of knowledge is as grand as the college's historic stature.")
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


        elif 0 < budget <= 20: # when the budget is less than 20 pounds
            print("There are some historical pubs, like Eagle, souvenir shops you can visit in Cambridge! And you can sign up for shared punting!")
            break
        elif 20 < budget <= 50: # when the budget is more than 20 pounds but less than 50 pounds
            print("You can book a ticket to have a musical feast in King's College Chapel, which costs between 20 and 50 pounds depending on the occassion!")
            break

        elif 50 < budget <=100: # when the budget is more than between 50 but less than 100 pounds
            print("You can hire a punt and punt with your friends, getting a glimpse into the prestigious private gardens and a sample of some of the local wildlife – predominantly ducks and swans!")
            break
        else: # when the budget is outside the range 0-100 pounds
            print("Sorry, I don't have any recommendation for your budget!")
            
    except ValueError: # when the entry is not a number
        print("Invalid input! Please enter a valid number.")
