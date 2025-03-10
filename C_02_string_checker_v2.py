# Check that users have entered a valid
# option based on a list
def string_checker(user_response, valid_ans):
    while True:

        user_response = user_response.lower()

        for item in valid_ans:
            # check if the user response is a word in the list
            if item == user_response:
                return item

            # check if the user response is the same as
            # the first Letter of an item in the list
            elif user_response == item[0]:
                return item

        return "invalid"


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
            return "invalid"


# Automated testing is below in the form (test_case, expected_value)
to_test = [
    ('Rock', 'rock'),
    ('Paper', 'paper'),
    ('Scissors', 'scissors'),
    ('R', 'rock'),
    ('P', "paper"),
    ('S', "scissors"),
    ('XXX', 'xxx'),
    ('x', 'xxx'),
    ('random', 'invalid'),
]

# run tests!
for item in to_test:
    # retrieve test case and expected value
    case = item[0]
    expected = item[1]

    # get actual value (ie: test ticket function)
    actual = string_checker(case, valid_ans=["rock", "paper", "scissors", "xxx"])

    # compare actual and expected and output pass / fail
    if actual == expected:
        print(f" ✅✅✅Passed! Case: {case}, expected: {expected}, received: {actual} ✅✅✅")
    else:
        print(f"❌❌❌ Failed! Case: {case}, expected: {expected}, received: {actual} ❌❌❌")


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
