import random

# checks for an integer more than 0 (allows <enter>)
def int_checker(question):
    while True:
        error = " Please enter an integer that is 1 or more."

        to_check = input(question)

        # check for infinte mode
        if to_check == "":
            return "infinite"

        try:
            response = int(to_check)

            # checks that the number is more than / equal to 1
            if response < 1:
                print(error)
            else:
                return response

        except ValueError:
            print(error)

# Check that users have entered a valid
# option based on a list
def string_checker(question, valid_ans):
    while True:

        # Get  user response and make sure it's lowercase
        user_response =input(question) . lower()


        for item in valid_ans:
            # check if the user response is a word in the list
            if item == user_response:
                return item
            
# Main routine start here

# Intialise game variables
mode = "regular"

rounds_player = 0
rounds_right = 0
rounds_wrong = 0

print("Round 1 / Round 2 / Round 3")
            
# ask user if they want to see the instruction and display
# them if requested
want_instruction = string_checker("Do you want to read the instruction? ", ('yes', 'no'))

# checks user enter yes (y) or no(n)
if want_instruction == "yes":
    print("instructions go here")      

 # Ask user for number of rounds / infinite mode
num_rounds = int_checker("How many rounds would you like? Push <enter> for infinite mode: ")

if num_rounds == "infinite":
    mode = "infinite"
    num_rounds = 3

# Game loop starts here
while rounds_player < num_rounds:

    # Rounds headings (based on mode)
    if mode == "infinite":
        rounds_heading = f"\n Round {rounds_player + 1} (Infinite Mode) "
        num_rounds += 1
    else:
        rounds_heading = f"\n💿💿💿 Round {rounds_player + 1} of {num_rounds}💿💿💿"

    print(rounds_heading)

    # get user choice
    user_choice = int_checker("Choose...:",1-10)
    # print("you chose", user_choice)

    # If user choice is the exit code , break the loop
    if user_choice == "xxx":
        break


      

    










 



