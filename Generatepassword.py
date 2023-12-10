import random
import string

def generate(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    pass1 = ''.join(random.choice(characters) for _ in range(length))
    return pass1


try:
    password_len = int(input("Enter correct length of the password "))
except ValueError:
    print(" Please enter a valid integer for password length.")
    exit()

if password_len > 0:
    generated_pass = generate(password_len)
    print("Generated Password:", generated_pass)
else:
    print(" Please enter a positive integer.")
