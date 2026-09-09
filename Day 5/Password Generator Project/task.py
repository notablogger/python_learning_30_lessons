import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

easy_password = ""
hard_password_list = []

for i in range(0,nr_letters):
    easy_password+=random.choice(letters)
    hard_password_list.append(random.choice(letters))
for i in range(0,nr_symbols):
    easy_password+=random.choice(symbols)
    hard_password_list.append(random.choice(symbols))
for i in range(0,nr_numbers):
    easy_password+=random.choice(numbers)
    hard_password_list.append(random.choice(numbers))

#easy
print(f"Your easy password is: {easy_password}")

#hard
print(f"Your hard password chars before shuffle are: {hard_password_list}")
random.shuffle(hard_password_list)
print(f"Your hard password chars are: {hard_password_list}")
#join function
hard_password = "".join(hard_password_list)
print(f"Your hard password is: {hard_password}")