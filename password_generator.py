import random
import string

def generate_password(length):
    characters = (
        string.ascii_letters +
        string.digits +
        string.punctuation
    )

    password = ''.join(
        random.choice(characters)
        for _ in range(length)
    )

    return password

try:
    length = int(input("Enter password length: "))

    if length < 4:
        print("Password must be at least 4 characters.")
    else:
        password = generate_password(length)

        print("\nGenerated Password:")
        print(password)

except ValueError:
    print("Please enter a valid number.")