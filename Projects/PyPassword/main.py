# Password Generator Project
import random

letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))


# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91

ez_pass = ""

for num_letters in range(1, nr_letters + 1):
    random_int = random.randint(0, len(letters) - 1)
    ez_pass += letters[random_int]

for num_int in range(1, nr_numbers + 1):
    random_int = random.randint(0, len(numbers) - 1)
    ez_pass += numbers[random_int]

for num_symbols in range(1, nr_symbols + 1):
    random_int = random.randint(0, len(symbols) - 1)
    ez_pass += symbols[random_int]

print(ez_pass)


# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

pass_list = list(ez_pass)

random.shuffle(pass_list)

hd_pass = ""

for char in pass_list:
    hd_pass += char

print(hd_pass)
