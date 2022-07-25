#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

letter_pass = []
symbol_pass = []
number_pass = []
password_shuffle = []
password = ''

#produces the random characters of each type.
for x in range(nr_letters):
  letter_pass += random.choice(letters)
for y in range(nr_symbols):
  symbol_pass += random.choice(symbols)
for z in range(nr_numbers):
  number_pass += random.choice(numbers)

#concatenates the list ready for password shuffling.
password_shuffle = letter_pass + symbol_pass + number_pass

#shuffles the new concatenated list.
random.shuffle(password_shuffle)

#turns list into a str to be printed w/o spaces.
for z in password_shuffle:
  password += z

print(password)