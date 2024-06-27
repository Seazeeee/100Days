"""Module that returns the NATO version of any word based on its letters."""

import pandas

# Read the data inside the CSV
data = pandas.read_csv("Projects/NATO Alphabet/nato_phonetic_alphabet.csv")

# Create a dictionary resulting in {"A": "Alpha", "B": "Bravo"} etc.
data_dict = {code.letter: code.code for (index, code) in data.iterrows()}

# Get the user input.
USER_WORD = str(input("Enter a word: "))

# Grab the letters from USER_WORD.
word_letters = [letters for letters in USER_WORD]

# Verify those letters are in data_dict and then return their value for
# the given key.
in_data = [
    data_dict[letters.upper()]
    for letters in word_letters
    if letters.upper() in data_dict.keys()
]

print(in_data)
