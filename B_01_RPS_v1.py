def string_checker(question, valid_ans=('yes', 'no')):
    error = f"Please enter a valid option from the following list: {valid_ans}"

    while True:

        # Get user response and make sure it's lowercase
        user_response = input(question).lower()

        for item in valid_ans:
            # check if the user response is a word in the list
            if item == user_response:
                return item

            # check if the user response is the same as
            # the first Letter of an item in the list
            elif user_response == item[0]:
                return item

        # print error if user does not enter something that is valid
        print(error)
        print()


def int_check(question):
    while True:
        error = "Please enter an integer that is 1 or more."

        response = input(question)

        # check for infinite mode
        if response == "":
            return ""

        try:
            response = int(response)

            # checks that the number            print(error)r is more than / equal to 13
            if response < 1:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


def instructions():
    """Prints instructions"""

    print("""
**** Instructions ****

To begin the number of rounds (or press <enter> for 
infinite mode).

then play against a computer. You need to choose R (rock),
P (paper) or S (scissors).

The rules are as follow:
o Rock beats scissors
o Scissors beats paper
o Paper beats rock

Press <xxx> to end the game anytime.

Good luck.
    """)


# Main routine
print()
print("🪨📃✂️ Rock / Paper / scissors game ✂️📃🪨")
print()

# ask the user if they want instructions and display
# them if requested
want_instructions = string_checker("Do you want to see the instructions? ")

# check users enter yes (y) no (n)
if want_instructions == "yes":
    instructions()

rounds_wanted = int_check("How many rounds? ")
print(f"you chose {rounds_wanted}")
