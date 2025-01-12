#Password Generator Project
import random

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
p_letters = int(input("How many letters would you like in your password?\n"))
p_symbols = int(input(f"How many symbols would you like?\n"))
p_numbers = int(input(f"How many numbers would you like?\n"))

password = []
for char in range(1, p_letters + 1):
    password.append(random.choice(letters))
for char in range(1, p_symbols + 1):
    password += random.choice(symbols)
for char in range(1, p_numbers + 1):
    password += random.choice(numbers)
random.shuffle(password)
final_password = ""
for i in password:
    final_password += i

print(f"Your password is {final_password}")