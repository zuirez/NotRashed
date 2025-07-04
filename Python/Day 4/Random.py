import random

# We can enter the range in random.randint(x,y) function, where x is the lowest and y is  the heighest range
random_number = random.randint(0,10)

print(random_number)

# random.random() has the range of 0.0 <= x < 1.0
# That means it will never output 1
random_float_number = random.random() * 10
print(random_float_number)

random_float_number_range = random.uniform(1,10)
print(random_float_number_range)


fruit = ["apple", "banana", "mango", "pineapple", "jackfruit", "orange"]

# Chosing a random value from the list
print(random.choice(fruit))