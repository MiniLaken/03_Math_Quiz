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

def instruction():
    print()

# Instructions

# to begin, decide on a score goal (eg: The first one to get a
#  score of 50 wins).

# For each round of the game, you win points by rolling dice.
# The winner of the round is the one who gets 13 (or slightly less).

# If you win the round, then your score will increase by the 
# number of points that you earned. If your first roll of two dice is a double (eg: both dice show a three), then your score will be DOUBLE the 
# number of points.
