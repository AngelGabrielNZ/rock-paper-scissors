# functions go here

def yes_no(question):
    """checks the user response to a question is yes / no (y/n), returns 'yes' or 'no' """

    while True:

        response = input(question).lower()

        # check the user says yes / no
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("please enter yes / no")


def instructions():
    """Prints instructions"""

    print("""
**** Instructions ****

Choose from rock / paper / scissors and hope to win.

- rock beats scissors
- scissors beats paper
- paper beats rock

Good luck.
    """)


# Main routine


# ask the user if they want instructions (check they say yes / no)
want_instructions = yes_no("Do you want to see the instructions? ")

# display the instruction if user wants to see them...
if want_instructions == "yes":
    instructions()

print()

