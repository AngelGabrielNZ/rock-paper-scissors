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

print("🪨📃✂️ Rock / Paper / scissors game ✂️📃🪨")
print()

# Instructions

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
    user_choice = input("Choose: ")

    #  if user choice is the exit code, break the loop
    if user_choice == "xxx":
        break

    rounds_played += 1

    # if user are in infinite mode, increase number of rounds!
    if mode == "infinite":
        num_rounds += 1


# Game loop ends here

# game history / statistics area
