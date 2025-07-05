import random

print("WELCOME TO RANDOM PASSWORD GENERATOR!")

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = [0,1,2,3,4,5,6,7,8,9]

symbols = ['!', '@', '#', '$', '%', '(', ')', '*', '+']

user_letter = int(input("How many letters would you like to have in your password?\n"))

user_number = int(input("How many number would you like to have in your password?\n"))

user_symbol = int(input("How many symbol would you like to have in your password?\n"))

combination = ""

for n in range(0, user_letter):
    combination = combination + str(random.choice(letters))
for m in range(0, user_number):
    combination = combination + str(random.choice(numbers))
for o in range(0, user_symbol):
    combination = combination + str(random.choice(symbols))

combination_list = list(combination)
random.shuffle(combination_list)
password = ''.join(combination_list)

print(f"Your random password is : {password}")