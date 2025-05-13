import random

# checks user enter yes (y) or no (no)
def yes_no(question):
    while True:

        response = input(question).lower()

        # check the user says yes/no / y / n
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("please enter yes / no")
            
print("How many rounds do you want?")
response = 5

