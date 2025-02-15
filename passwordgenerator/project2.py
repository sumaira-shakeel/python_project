# Password Generator
import random
import string

def generate_password(length=12):  # Fixed function name
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))  # Fixed loop syntax
    return password

# User input
length = int(input("Enter the length of your desired password: "))

password = generate_password(length)
print("Generated password:", password)
