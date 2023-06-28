import resources
import os

# Set environment variable in order to use clear function
os.environ["TERM"] = "xterm-color"


# Define clearing function
def clear():
    os.system('clear')


# Define morse conversion function

program_running = True


def morse_converter():

    # Set program loop

    while program_running:

        clear()

        # Display art

        print(resources.logo)

        # Take an input from user and capitalize

        user_input = input("Type text to be converted to morse.\n").upper()

        # Iterate though characters in user input and find corresponding morse code

        morse_output = ""

        for element in user_input:
            morse_output = morse_output + resources.MORSE_CODE_DICT[element]

        # Print final result

        print(f"Your input converted to morse code is:\n{morse_output}")

        continue_input = input("Type 'Y' to run program again. Type anything else to end program.\n").upper()

        if continue_input == "Y":
            pass
        else:
            break


# Call function

morse_converter()
