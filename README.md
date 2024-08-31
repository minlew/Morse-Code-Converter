# Morse Code Converter

## Description
This is a simple Python program that converts text input into Morse code. It provides an interactive command-line interface for users to enter text and receive the corresponding Morse code output.

### Features
- Converts alphanumeric characters and some punctuation marks to Morse code.
- Clears the console screen for a clean user interface.
- Displays ASCII art logo.
- Allows multiple conversions in a single session.

### Technologies
* Python

### Python Libs
* OS

### File Structure
* `main.py`: Contains the main program logic and user interface
* `resources.py`: Contains the ASCII art logo and Morse code dictionary


## Getting Started
1. Clone this repository.
2. Create virtual environment.
3. Run [script](main.py) in Python. 

## How It Works
1. The program imports necessary modules and resources.
2. It sets up the environment for the clear screen function.
3. The `main morse_converter()` function is defined, which:
    1. Clears the screen and displays the logo.
    2. Prompts the user for input.
    3. Converts the input to uppercase.
    4. Iterates through each character, looking up the Morse code equivalent.
    5. Displays the final Morse code output.
    6. Asks if the user wants to continue or exit.

## Customization
You can modify the `MORSE_CODE_DICT` in resources.py to add or change Morse code mappings for different characters.
