import art

alphabet = [
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
]

def caesar(start_text, shift_amount, cipher_direction):

    encode = ""
    decode = ""
    for letter in start_text:
        if cipher_direction.lower() == "encode":
            if letter in alphabet:
                letter_index = alphabet.index(letter)
                encode += alphabet[(letter_index + shift_amount) % (len(alphabet))]
            else:
                encode += letter
        elif cipher_direction.lower() == "decode":
            if letter in alphabet:
                letter_index = alphabet.index(letter)
                decode += alphabet[(letter_index - shift_amount) % (len(alphabet))]
            else:
                decode += letter

    if cipher_direction.lower() == "encode":
        print(f"Your encrypted message is {encode}")
    elif cipher_direction.lower() == "decode":
        print(f"Your decrypted message is {decode}")

print(art.logo)

should_continue = True

while should_continue:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    repeat_ques = input("Would you like to restart the cipher? Y/N \n").lower()

    if repeat_ques == "y" or repeat_ques == "yes":
        continue
    else:
        print("Have a good day!")
        should_continue = False
