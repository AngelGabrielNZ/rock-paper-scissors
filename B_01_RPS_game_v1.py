# Check that users have entered a valid
# option based on a list
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


def instructions():
    print("""

**** Instructions ****

To begin, choose the number of rounds (or press <enter> for 
infinite mode).

Then play against the computer. you need to pick between R (rock),
P (paper) or S (scissors).

The rules are as follow:
o   Paper beats rock
o   Rock beats scissors
o   Scissors beats paper

Press <xxx> to end game at anytime.

Good luck!
    """)


# checks for integer more than 0 (allows <enter>)
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


# Main routine Starts here

# Initialise game variables
mode = "regular"
rounds_played = 0

rps_list = ["rock", "paper", "scissors", "xxx"]

print("🪨📃✂️ Rock / Paper / scissors game ✂️📃🪨")
print()

# ask the user if they want instructions (check they say yes / no)
# them if requested
want_instructions = string_checker("Do you want to see the instructions? ")

# check user enter yes (y) or no (n)
if want_instructions == "yes":
    instructions()

# Ask user for numbers of rounds / infinite mode
num_rounds = int_check("How many rounds do would like to play? Push <enter> for infinite mode: ")

if num_rounds == "":
    mode = "infinite"
    num_rounds = 5

# Game loop starts here
while rounds_played < num_rounds:

    # Rounds headings (based on mode)
    if mode == "infinite":
        rounds_heading = f"\n♾️♾️♾️ Rounds {rounds_played + 1} (infinite mode) ♾️♾️♾️"
    else:
        rounds_heading = f"\n💿💿💿Rounds {rounds_played + 1} of {num_rounds}💿💿💿"

    print(rounds_heading)
    print()

    # get user choice
    user_choice = string_checker("Chose: ", rps_list)
    print("you choose", user_choice)

    #  if user choice is the exit code, break the loop
    if user_choice == "xxx":
        break

    rounds_played += 1

    # if user are in infinite mode, increase number of rounds!
    if mode == "infinite":
        num_rounds += 1

# Game loop ends here

# game history / statistics area
