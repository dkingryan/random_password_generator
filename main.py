import random
import string

def generate_password (min_Length,letter = True, numbers = True, special_characters = True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = ""
    if letter:
        characters += letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special

    password = ""
    meets_criteria = True
    has_letters = False
    has_number = False
    has_special = False

    while not meets_criteria or len(password) < min_Length:
        new_char = random.choice(characters)
        password += new_char

        if new_char in letters:
            has_letters = True
        elif new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True

        meets_criteria = True
        if letter:
            meets_criteria = has_letters
        if numbers:
            meets_criteria = meets_criteria and has_number
        if special_characters:
            meets_criteria = meets_criteria and has_special and has_number

    return password

min_length = int(input ("Enter the minimum length of your password: "))
has_letter = input("Do you want to have letters (yes/no)? ").lower() == "yes"
has_number = input("Do you want to have numbers (yes/no)? ").lower() == "yes"
has_special = input("Do you want to have special characters (yes/no)? ").lower() == "yes"
password = generate_password(min_length, has_letter, has_number, has_special)
print("The generated password is: " + password)

