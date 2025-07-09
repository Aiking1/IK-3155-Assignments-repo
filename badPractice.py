# This program works, but it's a mess in terms of good coding practices.

def main():
    # Everything is done inside main, making it full and harder to read.
    print("Wanna see ur fortune?")
    number = input("type a number from 1 to 5: ")  # Not validating

    # Repeating print logic for each number manually, instead of using a dictionary or function
    if number == "1":
        print("you will become rich")
    elif number == "2":
        print("a storm is coming in to your life")
    elif number == "3":
        print("everything is going to be fine")
    elif number == "4":
        print("Prepare yourself to face bad news heading your way")
    elif number == "5":
        print("you next generation is going to struggle because of you")
    else:
        print("bad input")

    # ended with no error handling, program crashes if user inputs something unexpected
    # Bad structure and modularity


#No documenting beside for the mistakes made
# No docstrings explaining what the function does

main()
