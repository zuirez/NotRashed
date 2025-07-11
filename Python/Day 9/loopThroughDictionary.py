car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

#Loop through a dictionary
for thing in car:
    print(thing)    # only prints the key


#Loop through a dictionary using keys()
for x in car.keys():
    print(x)


#Loop through a dictionary with key and value
for key in car:
    print(key)
    print(car[key])


#Loop through a dictionary both key and value using items()
for x,y in car.items():
    print(x,y)


#Loop through a dictionary using values()
for x in car.values():
    print(x)