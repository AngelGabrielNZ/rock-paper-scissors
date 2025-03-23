
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


# check for integer more 0 (allows <enter>)
def int_check(to_check):
    while True:
        error = "Please enter an integer that is 1 or more."

        # check for infinite mode
        if to_check == "":
            return "infinite"

        try:
            response = int(to_check)

            # checks that the number is more than / equal to 13
            if response < 1:
                # print(error)
                return "invalid"
            else:
                return response

        except ValueError:
            # print(error)
            return "invalid"

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



# Automated testing is below in the form (test_case, expected_value)
to_test = [
    ('xlii', 'invalid'),
    ('0.5', 'invalid'),
    ('0', 'invalid'),
    (1, 1),
    (2, 2),
    ('', 'infinite'),
]

# run tests!
for item in to_test:
    # retrieve test case and expected value
    case = item[0]
    expected = item[1]

    # get actual value (ie: test ticket function)
    actual = int_check(case)

    # compare actual and expected and output pass / fail
    if actual == expected:
        print(f" ✅✅✅Passed! Case: {case}, expected: {expected}, received: {actual} ✅✅✅")
    else:
        print(f"❌❌❌ Failed! Case: {case}, expected: {expected}, received: {actual} ❌❌❌")



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

print("program continues")
