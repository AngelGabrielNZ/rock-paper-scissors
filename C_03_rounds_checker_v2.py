
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


# main routine

how_many = int_check("How many rounds? ")
