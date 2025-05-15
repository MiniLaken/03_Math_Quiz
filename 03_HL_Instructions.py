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
