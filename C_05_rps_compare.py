import random


# Check that users have entered a valid
# option based on a list
def rps_compare(question, valid_ans=('yes', 'no')):
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


# Automated testing is below in the form (test_case, espected_value)
to_test = [
    ('rock', 'rock', 'tie'),
    ('rock', 'paper', 'lose'),
    ('rock', 'scissors', 'win'),
    ('paper', 'paper', 'tie'),
    ('paper', 'rock', 'win'),
    ('paper', 'scissors', 'lose'),
    ('scissors', 'scissors', 'tie'),
    ('scissors', 'rock', 'lose'),
    ('scissors', 'paper', 'win'),
]

# Run for test!
for item in to_test:
    # retrieve test case and expected value
    user = item[0]
    comp = item[1]
    expected = item[2]

    # get actual value (ie: test ticket function)
    actual = rps_compare(user, comp)

    # compare actual and expected and output pass / fail
    if actual == expected:
        print(f" ✔️✔️✔️Passed! case: {user} vs {comp}, expected: {expected}, received: {actual} ✔️✔️✔️")
    else:
        print(f" ❌❌❌Failed! case: {user} vs {comp}, expected: {expected}, received: {actual} ❌❌❌")


