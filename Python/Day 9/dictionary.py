# creating a dictionary
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

#printing a dictionary
print(car)


#Adding a new {key:value} in dictionary
car["price"] = 12999

print(car)


#Edit an item in dictionary
car["brand"] = "Porsche"

print(car)


#Removing an item from dictionary
car.pop("year")
print(car)


#Getting keys and values and both
x = car.keys()
print(x)

x = car.values()
print(x)

x = car.items()
print(x)


#An empty dictionary
empty_dictionary = {}


#Clearing an entire dictionary
car = {}

print(car)

#Clearing an entire dictionary using clear()
car.clear()
print(car)
