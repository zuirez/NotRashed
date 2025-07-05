import random

name = "Rashed"

print(name)

# Converting a string into list
name_list = list(name)

# printing the list
print(name_list)

# shuffling the name list
random.shuffle(name_list)

# printing the shuffled name list
print(name_list)

# converting list into string
shuffled_name = ''.join(name_list)

# printing the shuffled string
print(shuffled_name)