import random
import string

def generate_password(length):
    if length < 4:
        return "Password should be at least 4 characters long for security."

    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    symbols = string.punctuation

    base = [
        random.choice(uppercase),
        random.choice(lowercase),
        random.choice(digits),
        random.choice(symbols)
    ]

    all_chars = uppercase + lowercase + digits + symbols
    remaining = length - 4
    base += random.choices(all_chars, k=remaining)

    random.shuffle(base)
    return ''.join(base)

try:
    user_length = int(input("Enter the desired password length: "))
    password = generate_password(user_length)
    print("Generated Password:", password)
except ValueError:
    print("Please enter a valid number.")
