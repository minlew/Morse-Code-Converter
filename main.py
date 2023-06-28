# TODO. Import

import resources
import os


# TODO. Define clearing function

def clear():
    os.system('clear')


# TODO. Define morse conversion function

program_running = True


def morse_converter():

    # TODO. Set program loop

    while program_running:

        clear()

        # TODO. Display art

        print(resources.logo)

        # TODO. Take an input from user and capitalize

        user_input = input("Type text to be converted to morse.\n").upper()

        # TODO. Iterate though characters in user input and find corresponding morse code

        morse_output = ""

        for element in user_input:
            morse_output = morse_output + resources.MORSE_CODE_DICT[element]

        # TODO. Print final result

        print(f"Your input converted to morse code is:\n{morse_output}")

        continue_input = input("Type 'Y' to run program again. Type anything else to end program.\n").upper()

        if continue_input == "Y":
            pass
        else:
            break


# TODO. Call function

morse_converter()
