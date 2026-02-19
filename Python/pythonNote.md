# Python  Note

### Printing
``` python
print("Hello World!")
```
### Next Line
``` python
# To print in next line, \n is used. Note that there is no gap between n and the text.

print("Hello World!\nHi")
```

```
output:

Hello World!
Hi
```

### Input
``` python
# This line will just take input, but its not a variable, so to store the value inputed we have to declear a variable

input("What is your name?")


# Storing the input 

name = input("What is your name?")
print(name)


# Here at first the text inside input function will be visible in terminal, and take the value and then Hello! (value)! will be printed

print("Hello! " + input("what is your name?") + "!")
```

```
input : Rashed

output: Hello! Rashed!
```

>[!Note]
>This input function will take the input in same line. <br>
>In order to enter the value in next line we have to use `\n`

### Length 

``` python
# len() is used to get length

# 1
name = input("What is your name?")
print(len(name)) #inout Rashed; output 6

# 2
print(len(input("Enter your name : ")))

# 3
name = input("What is your name?")
length = len(name)
print(length)

```


### Subscripting
``` python
# Prints a specific character from a string

print("Hello World!"[0]) # Outputs H
print("Hello World!"[1]) # Outputs e
print("Hello World!"[2]) # Outputs l
print("Hello World!"[11]) # Outputs ! 


# Negative indices prints backward

print("Hello World!"[-4]) # Outputs r
print("Hello World!"[-3]) # Outputs l
print("Hello World!"[-2]) # Outputs d
print("Hello World!"[-1]) # Outputs ! 
```


### Data Types

``` Python
# Integer 
print(123 + 345)

# Large Integer 
print(123_456_789)

# String 
print("123" + "345")

# FLoat 
print(3.1416)

# Boolean 
print(True)
print(False)
```

>[!Note]
>To show the data type of a variable, we can use `type()` function.

```python
print(type("Rashed"))   # Returns : <class 'str'>
print(type(12345))     # Returns : <class 'int'>
print(type(3.1416))   # Returns : <class 'float'>
print(type(True))    # Returns : <class 'bool'>
```
<br>

**All data types in python**

| Example                                           | Data Type   |
|---------------------------------------------------|-------------|
|  x = "Hello World"                                | str         |
|  x = 20                                           | int         |
|  x = 20.5                                         | float       |
|  x = 1j                                           | complex     |
|  x = ["apple", "banana", "cherry"]                | list        |
|  x = ("apple", "banana", "cherry")                | tuple       |
|  x = range(6)                                     | range       |
|  x = {"name": "John", "age": 36}                  | dict        |
|  x = {"apple", "banana", "cherry"}                | set         |
|  x = frozenset({"apple", "banana", "cherry"})     | frozenset   |
|  x = True                                         | bool        |
|  x = b"Hello"                                     | bytes       |
|  x = bytearray(5)                                 | bytearray   |
|  x = memoryview(bytes(5))                         | memoryview  |
|  x = None                                         | NoneType    |

>[!note]
>**Float can also be scientific numbers with an "e" to indicate the power of 10.**
>```python
>x = 35e3
>y = 12E4
>z = -87.7e100
>
>print(type(x))  # Prints : <class 'float'>
>print(type(y))  # Prints : <class 'float'>
>print(type(z))  # Prints : <class 'float'>

### Variables

We dont have to declare a variable in python.
``` python 
x = 5
y = "John"
print(x)
print(y)
```
<br>

Variables do not need to be declared with any particular type, and can even change type after they have been set.

``` python
x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)    # prints Sally
```
<br>

Python allows to assign values to multiple variables in one line:

```python
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
```
<br>

And we can assign the same value to multiple variables in one line:

```python
x = y = z = "Orange"
print(x)
print(y)
print(z)
```
<br>

**Unpack a Collection**

If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.
```python
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)
```
<br>

Printing multiple variable at once

```python
# Separated by comma

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)


# Separated by +

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)
```

<br>

In the ```print()``` function, when you try to combine a string and a number with the + operator, Python will give you an error:

```python
# GIVES ERROR !

x = 5
y = "John"
print(x + y)
```

The best way to output multiple variables in the ```print()``` function is to separate them with commas, which even support different data types:

```python
x = 5
y = "John"
print(x, y) # prints: 5 John
```
<br>

Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.

To create a global variable inside a function, you can use the global keyword.

```python 
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
```
<br>

### Strings

We can assign a multiline string to a variable by using three quotes:
```python
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)


# prints 

Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.
```
<br>

String is nothing but an array. Square brackets can be used to access elements of the string.

```python
a = "Hello, World!"
print(a[1])    # prints : e
```
<br>

To check if a certain phrase or character is present in a string, we can use the keyword in.

To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.

```python
txt = "The best things in life are free!"
print("free" in txt) # prints : True


txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.") 
```
<br>

**Slicing**

We can return a range of characters by using the slice syntax.

Specify the start index and the end index, separated by a colon, to return a part of the string.

```python
b = "Hello, World!"
print(b[2:5]) # prints : llo


# Slices from start
b = "Hello, World!"
print(b[:5]) # prints : Hello


# Slices till end 
b = "Hello, World!"
print(b[2:]) # prints : llo, World!


# Negative indexing 
b = "Hello, World!"
print(b[-5:-2]) # prints : orl
```
<br>

**String modification :**

**Converts to upper or lower case**
```python
.lower() # To lowercase
.upper() # Tp uppercase

size = input("What size pizza do you want? S,M,L : ").lower()
size = input("What size pizza do you want? S,M,L : ").upper()
```
<br>

**Remove whitesapce**

The ```strip()``` method removes any whitespace from the **beginning** or the **end**:
```python
a = " Hello, World! "
print(a.strip()) # prints : "Hello, World!"
```
<br>

**Replace String**

The ```replace()``` method replaces a string with another string:
```python
a = "Hello, World!"
print(a.replace("H", "J")) # prints : Jello, World!

a = "HellO, World!"
print(a.replace("o", "z")) # prints : HellO, Wzrld!

a = "Hello, World!"
print(a.replace("o", "z")) # prints : Hellz, Wzrld!
```
<br>

**Split string**

The split() method splits the string into substrings if it finds instances of the separator:

```python
a = "Hello, World!"
print(a.split(",")) # prints : ['Hello', ' World!']


a = "Hello, World!"
b = a.split("o")
print(b) # prints : ['Hell', ', W', 'rld!']
```
<br>

**Escape Character**

To insert characters that are illegal in a string, use an escape character.

An escape character is a backslash \ followed by the character you want to insert.

An example of an illegal character is a double quote inside a string that is surrounded by double quotes:

```python
# GIVES ERROR!

txt = "We are the so-called "Vikings" from the north."


# USING ESCAPE CHARACTER

txt = "We are the so-called \"Vikings\" from the north."
```
<br>

We can use quotes inside a string, as long as they don't match the quotes surrounding the string:
```python
print("It's alright")           # prints : It's alright
print("He is called 'Johnny'")  # He is called 'Johnny'
print('He is called "Johnny"')  # He is called "Johnny"
```
<br>

**String methods**

Documentation link :
[W3School](https://www.w3schools.com/python/python_strings_methods.asp)


### f-String

We can't concatinate different data types without type casting. <br>To solve this problem we use f-string.

```python
score = 5
height = 5.5
is_wining = True

# We can't concatinate different data types without type casting
print("Your score is : " + str(score), "Your height is : " + str(height), "You are wining : " + str(is_wining))

# To solve this problem we use f-string
print(f"Your score is : {score}, Your height is : {height}, Your are wining : {is_wining}")
```

<br>

### Type Casting

We can get the data type of a variable with the ```type()``` function.

```python
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
```

```python
print("123" + "456")   # Returns : 123456
print(int("123") + int("456"))   # Returns : 579
```

>[!caution]
>Not everything can be type casted. <br>
>For example `abc` can't be typecasted to `int` <br><br>
>We Cant concatinate `str` to `int` 
>``` python 
>print("Number of letters in your name : " + len(input("Enter your name : ")))
>```
>Here, the len function will return and int value. The int value cant be concatinated with the `str`, <br>so we have to type cast the int value to `str`, so that we can concate them.


### Mathematical Operators

``` python
print(123+456) # Addition
print(456-123) # Subtraction
print(5*4) # Multiplicaiton
print(6/3) # Division
print(6//3) # Ignores decimal
print(5/3) # Division
print(5//3) # Ignores decimal
print(5**2) # Power 
```

### Precedence

**PEMDAS** <br>
1. P = Parentheses
2. E = Exponents
3. M = Multiplication
4. D = Division
5. A = Addition
6. S = Subtraction

### Number Manupulation

```python
Bmi = 37.56786
Bmi2 = 37.45254

print(Bmi)             # 37.56786
print(round(Bmi))      # 38
print(round(Bmi, 2))   # 37.57

print(Bmi2)            # 37.45254
print(round(Bmi2))     # 37
print(round(Bmi2, 2))  # 37.45
```

### Assignment Operators

```python
+=
-=
*=
/=

score = 0

score += 1
score -= 1
score *= 2
score /= 3
```

### Comparison Operator

<table>
    <tr>
        <td>></td>
        <td>Greater then</td>
    </tr>
    <tr>
        <td><</td>
        <td>Less then</td>
    </tr>
    <tr>
        <td>>=</td>
        <td>Greater then or equal to</td>
    </tr>
    <tr>
        <td><=</td>
        <td>Less then or equal to</td>
    </tr>
    <tr>
        <td>==</td>
        <td>Equal to</td>
    </tr>
    <tr>
        <td>!=</td>
        <td>Not Equal to</td>
    </tr>
    <tr>
        <td>%</td>
        <td>Modulo Operator</td>
    </tr>
</table>

### Comparison Operator

<table>
    <tr>
        <td>and</td>
        <td>True if both condition is true</td>
    </tr>
    <tr>
        <td>or</td>
        <td>True if any condition is true</td>
    </tr>
    <tr>
        <td>not</td>
        <td>Oppose the condition</td>
    </tr>
</table>

### Conditions

In if else condition, if the conditino is true the if block executes and if not true then the else block executes 

```python
if (condition) :
    do this 
else :
    do this
```
<br>

Example:

```python
age = int(input("Enter your age : "))

if age>=18:
    print("You can vote.")  # if age greater then 18
else:
    print("You can't vote")  # if age less then 18
```
<br>

**Short notation**

This technique is known as Ternary Operators, or Conditional Expressions.

```python
# Short hand if
if a > b: print("a is greater than b")

# Short hand if else
a = 2
b = 330
print("A") if a > b else print("B")

# Multiple if else 
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")
```
<br>

**The pass statement**

if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.

```python
a = 33
b = 200

if b > a:
  pass
```

### Random 

Random is a pre build module in python, to use it we have to import it first

```python
random.randint(0,10)  # prints a random number from given range
random.random() * 10  # prints a random number between 0.0 <= x <1.0
random.uniform(1,10)  # prints a random float numbe from given range
random.choice(fruit)  # prints a random value from list
random.shuffle(fruit) # shuffle the order of fruit list
```

``` python
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
```

### List

Lists are used to store multiple items in a single variable. <br>
In like there could be values of different data types.<br>

 ``` python
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

# Inserting a value in specific index
fruit.insert(1,"pear") # prints : ["apple","pear", "banana", "mango", "pineapple", "jackfruit", "orange"]

# Removing an item from list 
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist) # prints : ['apple', 'cherry']

# Remove from specific index using pop()
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist) # prints : ['apple', 'cherry']

# Remove from specific index using del
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

# Clear a list 
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist) # prints : []
```
<br>

**List Comprehension**

Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.

Without list comprehension you will have to write a for statement with a conditional test inside:
```python
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist) # Prints : ['apple', 'banana', 'mango']
```
<br>

**Sort List Alphanumerically**

List objects have a ```sort()``` method that will sort the list alphanumerically, ascending, by default:
```python
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist) # Prints : ['banana', 'kiwi', 'mango', 'orange', 'pineapple']


thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist) # prints : [23, 50, 65, 82, 100]


# Sort in reverse 
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist) # prints : ['pineapple', 'orange', 'mango', 'kiwi', 'banana']


thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist) # prints : [100, 82, 65, 50, 23]
```

>[!note]
>By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters:

```python
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist) # prints : ['Kiwi', 'Orange', 'banana', 'cherry']


# If we want a case-insensitive sort function, we can use str.lower as a key function:

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist) # prints : ['banana', 'cherry', 'Kiwi', 'Orange']
```
<br>

**Reverse Order list**

The reverse() method reverses the current sorting order of the elements.

```python
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist) # prints : ['cherry', 'Kiwi', 'Orange', 'banana']
```
<br>

**Copy a list**

We cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2.

To copy we have to use ```copy()``` method
```python
# Copying using copy()
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist) # prints : ['apple', 'banana', 'cherry']


# Copying using list()
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist) # prints : ["apple", "banana", "cherry"]


# Copying using slice (:) operator 
thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist) # prints : ["apple", "banana", "cherry"]
```

**Range of Indexes**

```python
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5]) # prints : ['cherry', 'orange', 'kiwi']


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4]) # prints : ['apple', 'banana', 'cherry', 'orange']


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:]) # prints : ['cherry', 'orange', 'kiwi', 'melon', 'mango']


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1]) # prints : ['orange', 'kiwi', 'melon']
```
<br>

**Check if Item Exists**

To determine if a specified item is present in a list use the ```in``` keyword:

```python
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
```
<br>

**list Methods**

| Method     | Description                                                            |
|------------|------------------------------------------------------------------------|
| append()   | Adds an element at the end of the list                                 |
| clear()    | Removes all the elements from the list                                 |
| copy()     | Returns a copy of the list                                             |
| count()    | Returns the number of elements with the specified value                |
| extend()   | Add the elements of a list (or any iterable) to the end of the list    |
| index()    | Returns the index of the first element with the specified value        |
| insert()   | Adds an element at the specified position                              |
| pop()      | Removes the element at the specified position                          |
| remove()   | Removes the item with the specified value                              |
| reverse()  | Reverses the order of the list                                         |
| sort()     | Sorts the list                                                         |

<br>

### Nested List

``` python
fruit = ["apple", "banana", "mango", "orange"]
vegetable = ["Tomato", "Carrot", "Potato"]

food = [fruit, vegetable]

print(food)
```
<br>

### While loop

With the while loop we can execute a set of statements as long as a condition is true.

In while loop we have to define an indexing variable before writing the loop, and make sure to increment the variable.
```python
i = 1
while i < 6:
  print(i)
  i += 1
```
<br>

With the ```break```  statement we can stop the loop even if the while condition is true:
```python
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
```
<Br>

With the continue statement we can stop the current iteration, and continue with the next:
```python
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
```

<br>

With the else statement we can run a block of code once when the condition no longer is true:
```python
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")
```
<br>

### For loop

``` python
marks = [91, 95, 88, 86, 82, 99, 80, 87, 96]

for x in marks: # Here x is name of a variable, marks is the list.
    print(x)


# Looping through a string

for x in "banana":
  print(x)
```
<br>

for loops cannot be empty, but if you for some reason have a for loop with no content, put in the pass statement to avoid getting an error.

```python
for x in [0, 1, 2]:
  pass
```

### Some built in function

```sum()``` finds the sum of a list
``` python
marks = [91, 95, 88, 86, 82, 99, 80, 87, 96]

# Printing sum using built in function
print(sum(marks))
```
<br>

```max()``` finds the max value in a list
``` python
marks = [91, 95, 88, 86, 82, 99, 80, 87, 96]

# Finding max value using max function
print(f"Max value is : {max(marks)}")
```
<br>

```range(x,y,z)```
```python
# range(x,y,z)

# Printing the number from range x to less then y

for number in range(1,11):
    print(number)             # 1,2,3,4,5,6,7,8,9,10


# Printing the number from range x to less then y in steps of z

for number in range(1,11,2):
    print(number)             # 1,3,5,7,9
``` 

### String to list convertion

To convert string to list we use ```list(nameOfTheString)``` <br>
To convert list to string we use ```''.join(nameOfTheList)```

``` python 
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
```
<br>

### Function

A function is a block of code which runs when we call it.

To create a function we have to define it first by writing the keyword ```def``` <br>
then write the name of the function following with ```():```
```python
# Defining a function
def sayMyName():
    print("Rashed")

# Calling the function
sayMyName() # Prints : Rashed
```
<br>

### Dictionary

Dictionaries are used to store data values in ```{key:value}``` pairs.

A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

**Creating a dictionary**

```python
# creating a dictionary
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

#printing a dictionary
print(car)
```
<br>

**Adding a new {key:value} in dictionary**

```python
#Adding a new {key:value} in dictionary
car["price"] = 12999

print(car)
```
<br>

**Edit an item in dictionary**


```python
#Edit an item in dictionary
car["brand"] = "Porsche"

print(car)
```
<br>

**Loop through a dictionary**
```python
#Loop through a dictionary
for thing in car:
    print(thing)    # only prints the key
```
<br>

**Loop through a dictionary with key and value**
```python
#Loop through a dictionary with key and value
for key in car:
    print(key)
    print(car[key])
```
<br>

**Max value from dictionary**

```python
marks = {
    "Rashed" : 99,
    "Shawon" : 95,
    "Anik" : 100,
    "Maruf" : 91,
}

maxMarks = max(marks, key=marks.get)

print(maxMarks)  # Returns Anik
```

**An empty dictionary**
```python
#An empty dictionary
empty_dictionary = {}

#Clearing an entire dictionary
car = {}

#Clearing an entire dictionary using clear()
car.clear()
print(car)
```
<br>

**Getting keys and values**

```python
x = car.keys()  # dict_keys(['brand', 'model', 'year', 'price'])

x = car.values()  # dict_values(['Porsche', 'Mustang', 1964, 12999])

x = car.items()  # dict_items([('brand', 'Porsche'), ('model', 'Mustang'), ('year', 1964), ('price', 12999)])
```
<br>

**Removing item from dictionary**
```python
car.pop("year")
print(car)

car.popitem() # removes last key value from dictionary
```

### Looping through a dictionary

```python
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

#Loop through a dictionary
for thing in car:
    print(thing)    # only prints the key
```
```
brand
model
year
```
<br>

**Loop through a dictionary using keys()**

```python
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

#Loop through a dictionary using keys()
for x in car.keys():
    print(x)
```
```
brand
model
year
```
<br>

**Loop through a dictionary with key and value**

```python
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

#Loop through a dictionary with key and value
for key in car:
    print(key)
    print(car[key])
```
```
brand
Ford
model
Mustang
year
1964
```
<br>

**Loop through a dictionary both key and value using items()**

```python
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

#Loop through a dictionary both key and value using items()
for x,y in car.items():
    print(x,y)
```
```
brand Ford
model Mustang
year 1964
```
<br>

**Loop through a dictionary using values()**

```python
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

#Loop through a dictionary using values()
for x in car.values():
    print(x)
```
```
Ford
Mustang
1964
```
<br>