# This programme was built to help customers create a tailor made fruit list.

import random

def add_fruit():
        add_fruit = input("Please enter the fruit you want to add : ").capitalize()
        fruit_list.append(add_fruit)
        print("The fruit list after addition is", fruit_list)
        
def remove_fruit():
    drop_fruit = input("Please enter the fruit you want to remove : ").capitalize()
    if len(fruit_list)>0:
        if drop_fruit in fruit_list:
              fruit_list.remove(drop_fruit)
              print("The fruit list after the removal is", fruit_list)
        else:
              print("Fruit not in the list. Try again.")
    else:
        print("The list is empty. Nothing to remove.")

def user_interface():
      print('''Here is what you can do to the list\n
              1. add more fruit\n
              2. remove a fruit\n
              3. display all the fruit\n
              4. display the number of fruit\n
              5. display a random fruit\n
              6. quit\n''')
      

print('''We present to you the most popular fruit list. You are more than welcome 
to make changes to it so that we can provide you with fruits that you like!''')

fruit_list = ["Apples", "Oranges", "Bananas", "Tomatoes", "Pears", "Grapes"]
print("The most popular fruit list in our store is as follows",fruit_list)


while True:
        user_interface()
        user_input = int(input("Choose what you want to do(Enter the number) : "))

        try:
                
                if user_input== 1:
                    add_fruit()
                    
                elif user_input== 2:
                    remove_fruit()
                    
                elif user_input == 3:
                        print("The updated fruit list is", fruit_list)
                        
                elif user_input== 4:
                    print("The length of the list is ", len(fruit_list))
                    
                elif user_input == 5:
                    print("A random choice from the fruit list :", random.choice(fruit_list))
                    
                elif user_input == 6:
                    print("Your menu is finalised as follows")
                    for fruit in fruit_list:
                          print(fruit)
                    break
                else:
                        print("Invalid input! Please enter a number between 1 and 6.")
        except ValueError as e:
                print("Value Error:", e)
        





