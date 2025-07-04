import random

fruit = ["apple", "banana", "mango", "pineapple", "jackfruit", "orange"]

# Printing list using index
print(fruit[0])
print(fruit[1])
print(fruit[2])

# Printing the list in reverse using negative index
print(fruit[-1])
print(fruit[-2])
print(fruit[-3])

# Modifying value
fruit[2] = "mangooo"

# Printing the whole list
print(fruit)

# Adding a new value in list 
fruit.append("Cherry")

# Adding a new list in list 
fruit.extend(["pear", "melon"])

# Chosing a random value from the list
print(random.choice(fruit))