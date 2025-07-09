def get_choices():
    """
       Beginning of the program, validating the users response to the question.
    """

    while True:
        try:
            user_input = input("Pick a number between 1 and 5: ")
            choice = int(user_input)
            if 1 <= choice <= 5:
                return choice
            else:
                raise ValueError("Out of range.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")


def tell_fortune(decisions):
    """
      taking in the fortune input of the user and determining there fortune.
    """


    fortunes = {
        1: "Your best is in front of you! You will become a successful business owner",
        2: "A surprise is waiting for you around the corner. You will become a parent",
        3: "Today is your lucky day, you are going to win a million dollars",
        4: "Be cautious, something unexpected is approaching and will cause obstacles.",
        5: "You knowing did something wicked, now you will feel the wrath"
    }

    print("Your fortune: ", fortunes.get(choice, "Invalid choice."))


def main():

    """
    Main function to run the Program
    """

    print("Are you ready to find out your fortune?")

    decisions = get_choices()
    tell_fortune(decisions)

    if __name__ == "__main__":
        main()