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
    print("you choose infinite")
    num_rounds = 5

# Game loop starts here
while rounds_played < num_rounds:
    user_choice = input("Choose: ")

    if user_choice == "xxx":
        break

    rounds_played += 1
    print("rounds plaed: ", rounds_played)

    # if user are in infinite mode, increase number of rounds!
    if mode == "infinite":
        num_rounds += 1

    print("num rounds: ", num_rounds)

# Game loop ends here

# game history / statistics area
