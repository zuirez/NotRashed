# Python Notes


## Table of Contents
- [1. Printing and Input](#1-printing-and-input)
- [2. Strings and Text Processing](#2-strings-and-text-processing)
- [3. Data Types and Variables](#3-data-types-and-variables)
- [4. Type Casting and Math](#4-type-casting-and-math)
- [5. Conditions and Logic](#5-conditions-and-logic)
- [6. Random Module](#6-random-module)
- [7. Lists](#7-lists)
- [8. Loops](#8-loops)
- [9. Built-in Functions](#9-built-in-functions)
- [10. Functions](#10-functions)
- [11. Dictionaries](#11-dictionaries)

---

## 1. Printing and Input

### Printing
```python
print("Hello World!")
```

**Output**
```text
Hello World!
```

### Next Line (`\n`)
```python
# To print in next line, \n is used. Note that there is no gap between n and the text.
print("Hello World!\nHi")
```

**Output**
```text
Hello World!
Hi
```

### Input
```python
# This line will just take input, but its not a variable, so to store the value inputted we have to declare a variable
input("What is your name?")

# Storing the input
name = input("What is your name?")
print(name)

# Here at first the text inside input function will be visible in terminal,
# and take the value and then Hello! (value)! will be printed
print("Hello! " + input("what is your name?") + "!")
```

**Sample Input / Output**
```text
input: Rashed
output: Hello! Rashed!
```

> [!NOTE]
> The `input()` function takes input on the same line.
> To start from a new line, use `\n` in the prompt string.

### Length (`len`)
```python
# len() is used to get length

# 1
name = input("What is your name?")
print(len(name)) # input Rashed; output 6

# 2
print(len(input("Enter your name : ")))

# 3
name = input("What is your name?")
length = len(name)
print(length)
```

**Sample Output**
```text
(If input is Rashed)
6
```

---

## 2. Strings and Text Processing

### Subscripting
```python
# Prints a specific character from a string
print("Hello World!"[0])  # Outputs H
print("Hello World!"[1])  # Outputs e
print("Hello World!"[2])  # Outputs l
print("Hello World!"[11]) # Outputs !

# Negative indices prints backward
print("Hello World!"[-4]) # Outputs r
print("Hello World!"[-3]) # Outputs l
print("Hello World!"[-2]) # Outputs d
print("Hello World!"[-1]) # Outputs !
```

**Output**
```text
H
e
l
!
r
l
d
!
```

### Strings (Basics)
```python
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
```

**Output**
```text
Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.
```

```python
a = "Hello, World!"
print(a[1])    # prints : e
```


### Check Content (`in`, `not in`)
```python
txt = "The best things in life are free!"
print("free" in txt) # prints : True

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")
```

**Output**
```text
True
No, 'expensive' is NOT present.
```

### Slicing
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

**Output**
```text
llo
Hello
llo, World!
orl
```

### String Modification

#### Convert Case
```python
.lower() # To lowercase
.upper() # To uppercase

size = input("What size pizza do you want? S,M,L : ").lower()
size = input("What size pizza do you want? S,M,L : ").upper()
```

**Output**
```text
(No direct output unless printed)
```

#### Remove Whitespace (`strip`)
```python
a = " Hello, World! "
print(a.strip()) # prints : "Hello, World!"
```

**Output**
```text
Hello, World!
```

#### Replace String (`replace`)
```python
a = "Hello, World!"
print(a.replace("H", "J")) # prints : Jello, World!

a = "HellO, World!"
print(a.replace("o", "z")) # prints : HellO, Wzrld!

a = "Hello, World!"
print(a.replace("o", "z")) # prints : Hellz, Wzrld!
```

**Output**
```text
Jello, World!
HellO, Wzrld!
Hellz, Wzrld!
```

#### Split String (`split`)
```python
a = "Hello, World!"
print(a.split(",")) # prints : ['Hello', ' World!']

a = "Hello, World!"
b = a.split("o")
print(b) # prints : ['Hell', ', W', 'rld!']
```

**Output**
```text
['Hello', ' World!']
['Hell', ', W', 'rld!']
```

### Escape Character
```python
# GIVES ERROR!
# txt = "We are the so-called "Vikings" from the north."

# USING ESCAPE CHARACTER
txt = "We are the so-called \"Vikings\" from the north."
print(txt)
```

**Output**
```text
We are the so-called "Vikings" from the north.
```

```python
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')
```

**Output**
```text
It's alright
He is called 'Johnny'
He is called "Johnny"
```

### String Methods Reference
Documentation:
[W3School](https://www.w3schools.com/python/python_strings_methods.asp)

### f-String
```python
score = 90
height = 5.9
is_wining = True

print("Your score is : " + str(score), "Your height is : " + str(height), "You are wining : " + str(is_wining))

# To solve this problem we use f-string
print(f"Your score is : {score}, Your height is : {height}, Your are wining : {is_wining}")
```

**Output**
```text
Your score is : 90 Your height is : 5.9 You are wining : True
Your score is : 90, Your height is : 5.9, Your are wining : True
```

### String to List Conversion
To convert string to list we use `list(nameOfTheString)`.
To convert list to string we use `''.join(nameOfTheList)`.

```python
import random

name = "Rashed"
print(name)

# Converting a string into list
name_list = list(name)
print(name_list)

# shuffling the name list
random.shuffle(name_list)
print(name_list)

# converting list into string
shuffled_name = ''.join(name_list)
print(shuffled_name)
```

**Sample Output**
```text
Rashed
['R', 'a', 's', 'h', 'e', 'd']
['h', 'a', 'R', 'e', 'd', 's']
haReds
```

> [!NOTE]
> The shuffled order is random, so output will vary.

---

## 3. Data Types and Variables

### Data Types
```python
# Integer
print(123 + 345)

# Large Integer
print(123_456_789)

# String
print("123" + "345")

# Float
print(3.1416)

# Boolean
print(True)
print(False)
```

**Output**
```text
468
123456789
123345
3.1416
True
False
```

> [!NOTE]
> To show the data type of a variable, use `type()`.

```python
print(type("Rashed"))   # Returns : <class 'str'>
print(type(12345))      # Returns : <class 'int'>
print(type(3.1416))     # Returns : <class 'float'>
print(type(True))       # Returns : <class 'bool'>
```

**Output**
```text
<class 'str'>
<class 'int'>
<class 'float'>
<class 'bool'>
```

### All Data Types in Python

| Example                                           | Data Type   |
|---------------------------------------------------|-------------|
| x = "Hello World"                                | str         |
| x = 20                                            | int         |
| x = 20.5                                          | float       |
| x = 1j                                            | complex     |
| x = ["apple", "banana", "cherry"]                | list        |
| x = ("apple", "banana", "cherry")                | tuple       |
| x = range(6)                                      | range       |
| x = {"name": "John", "age": 36}                  | dict        |
| x = {"apple", "banana", "cherry"}                | set         |
| x = frozenset({"apple", "banana", "cherry"})     | frozenset   |
| x = True                                          | bool        |
| x = b"Hello"                                     | bytes       |
| x = bytearray(5)                                  | bytearray   |
| x = memoryview(bytes(5))                          | memoryview  |
| x = None                                          | NoneType    |

> [!NOTE]
> Float can also be scientific numbers with an `e` to indicate the power of 10.

```python
x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))
```

**Output**
```text
<class 'float'>
<class 'float'>
<class 'float'>
```

### Variables
We dont have to declare a variable in python.

```python
x = 5
y = "John"
print(x)
print(y)
```

**Output**
```text
5
John
```

Variables do not need to be declared with any particular type, and can even change type after they have been set.

```python
x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)    # prints Sally
```

**Output**
```text
Sally
```

Python allows assigning values to multiple variables in one line:

```python
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
```

**Output**
```text
Orange
Banana
Cherry
```

And we can assign the same value to multiple variables in one line:

```python
x = y = z = "Orange"
print(x)
print(y)
print(z)
```

**Output**
```text
Orange
Orange
Orange
```

#### Unpack a Collection
```python
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)
```

**Output**
```text
apple
banana
cherry
```

#### Print Multiple Variables
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

**Output**
```text
Python is awesome
Python is awesome
```

```python
# GIVES ERROR!
x = 5
y = "John"
print(x + y)
```

**Output**
```text
TypeError: unsupported operand type(s) for +: 'int' and 'str'
```

```python
x = 5
y = "John"
print(x, y)
```

**Output**
```text
5 John
```

#### Global Variable
```python
def myfunc():
  global x
  x = "fantastic"

myfunc()
print("Python is " + x)
```

**Output**
```text
Python is fantastic
```

---

## 4. Type Casting and Math

### Type Casting
```python
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
print(x, y, z)
```

**Output**
```text
3 3 3.0
```

```python
print("123" + "456")
print(int("123") + int("456"))
```

**Output**
```text
123456
579
```

> [!CAUTION]
> Not everything can be type casted.
> Example: `abc` cannot be cast to `int`.
>
> Also, we cant concatinate `str` with `int` directly:

```python
# print("Number of letters in your name : " + len(input("Enter your name : ")))
print("Number of letters in your name : " + str(len(input("Enter your name : "))))
```

### Mathematical Operators
```python
print(123 + 456) # Addition
print(456 - 123) # Subtraction
print(5 * 4)     # Multiplicaiton
print(6 / 3)     # Division
print(6 // 3)    # Ignores decimal
print(5 / 3)     # Division
print(5 // 3)    # Ignores decimal
print(5 ** 2)    # Power
print(5 * 4)     # Multiplication
```

**Output**
```text
579
333
20
2.0
2
1.6666666666666667
1
25
20
```

### Precedence
**PEMDAS**
1. P = Parentheses
2. E = Exponents
3. M = Multiplication
4. D = Division
5. A = Addition
6. S = Subtraction

### Number Manipulation
```python
Bmi = 37.56786
Bmi2 = 37.45254

print(round(Bmi))      # 38
print(round(Bmi, 2))   # 37.57

print(Bmi2)            # 37.45254
print(round(Bmi2))     # 37
print(round(Bmi2, 2))  # 37.45
```

**Output**
```text
38
37.57
37.45254
37
37.45
```

### Assignment Operators
```python
score = 0

score += 1
score -= 1
score *= 2
score /= 3

print(score)
```

**Output**
```text
0.0
```

---

## 5. Conditions and Logic

### Comparison Operators

| Operator | Meaning |
|----------|---------|
| `>`      | Greater than |
| `<`      | Less than |
| `>=`     | Greater than or equal to |
| `<=`     | Less than or equal to |
| `==`     | Equal to |
| `!=`     | Not equal to |
| `%`      | Modulo operator |

### Logical Operators

| Operator | Meaning |
|----------|---------|
| `and`    | True if both conditions are true |
| `or`     | True if any condition is true |
| `not`    | Opposite the condition |

### Conditions (`if-else`)
In if else condition, if the condition is true the if block executes and if not true then the else block executes.

```python
if condition:
    do_this
else:
    do_that
```

Example:

```python
age = int(input("Enter your age : "))

if age >= 18:
    print("You can vote.")
else:
    print("You can't vote")
```

**Sample Output**
```text
(If input is 19)
You can vote.
```

### Short Notation (Ternary)
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

**Output**
```text
B
=
```

### The `pass` Statement
```python
a = 33
b = 200

if b > a:
  pass
```

**Output**
```text
(No output)
```

---

## 6. Random Module

Random is a pre build module in python, to use it we have to import it first.

```python
import random

print(random.randint(0,10))
print(random.random() * 10)
print(random.uniform(1,10))

fruit = ["apple", "banana", "mango", "pineapple", "jackfruit", "orange"]
print(random.choice(fruit))
random.shuffle(fruit)
print(fruit)
```

**Sample Output**
```text
7
3.2184421
8.639122
banana
['orange', 'mango', 'apple', 'jackfruit', 'banana', 'pineapple']
```

> [!NOTE]
> Values from random functions will change each run.

```python
import random

random_number = random.randint(0,10)
print(random_number)

random_float_number = random.random() * 10
print(random_float_number)

random_float_number_range = random.uniform(1,10)
print(random_float_number_range)

fruit = ["apple", "banana", "mango", "pineapple", "jackfruit", "orange"]
print(random.choice(fruit))
```

**Sample Output**
```text
4
6.908244
9.122773
mango
```

---

## 7. Lists

Lists are used to store multiple items in a single variable.
In list there could be values of different data types.

```python
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
fruit.insert(1, "pear")

# Removing an item from list
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

# Remove from specific index using pop()
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

# Remove from specific index using del
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

# Clear a list
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)
```

**Output**
```text
apple
banana
mango
orange
jackfruit
pineapple
['apple', 'banana', 'mangooo', 'pineapple', 'jackfruit', 'orange']
['apple', 'cherry']
['apple', 'cherry']
['banana', 'cherry']
[]
```

### List Comprehension
```python
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)
```

**Output**
```text
['apple', 'banana', 'mango']
```

### Sort List Alphanumerically
```python
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

# Sort in reverse
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse=True)
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse=True)
print(thislist)
```

**Output**
```text
['banana', 'kiwi', 'mango', 'orange', 'pineapple']
[23, 50, 65, 82, 100]
['pineapple', 'orange', 'mango', 'kiwi', 'banana']
[100, 82, 65, 50, 23]
```

> [!NOTE]
> By default `sort()` is case-sensitive.

```python
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key=str.lower)
print(thislist)
```

**Output**
```text
['Kiwi', 'Orange', 'banana', 'cherry']
['banana', 'cherry', 'Kiwi', 'Orange']
```

### Reverse Order List
```python
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)
```

**Output**
```text
['cherry', 'Kiwi', 'Orange', 'banana']
```

### Copy a List
```python
# Copying using copy()
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

# Copying using list()
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

# Copying using slice (:) operator
thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)
```

**Output**
```text
['apple', 'banana', 'cherry']
['apple', 'banana', 'cherry']
['apple', 'banana', 'cherry']
```

### Range of Indexes
```python
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])
```

**Output**
```text
['cherry', 'orange', 'kiwi']
['apple', 'banana', 'cherry', 'orange']
['cherry', 'orange', 'kiwi', 'melon', 'mango']
['orange', 'kiwi', 'melon']
```

### Check if Item Exists
```python
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
```

**Output**
```text
Yes, 'apple' is in the fruits list
```

### List Methods

| Method    | Description |
|-----------|-------------|
| `append()` | Adds an element at the end of the list |
| `clear()`  | Removes all elements from the list |
| `copy()`   | Returns a copy of the list |
| `count()`  | Returns the number of elements with the specified value |
| `extend()` | Adds elements of another iterable to the end of list |
| `index()`  | Returns index of first element with specified value |
| `insert()` | Adds an element at the specified position |
| `pop()`    | Removes element at the specified position |
| `remove()` | Removes item with the specified value |
| `reverse()`| Reverses order of the list |
| `sort()`   | Sorts the list |

### Nested List
```python
fruit = ["apple", "banana", "mango", "orange"]
vegetable = ["Tomato", "Carrot", "Potato"]

food = [fruit, vegetable]
print(food)
```

**Output**
```text
[['apple', 'banana', 'mango', 'orange'], ['Tomato', 'Carrot', 'Potato']]
```

---

## 8. Loops

### While Loop
```python
i = 1
while i < 6:
  print(i)
  i += 1
```

**Output**
```text
1
2
3
4
5
```

#### `break`
```python
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
```

**Output**
```text
1
2
3
```

#### `continue`
```python
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
```

**Output**
```text
1
2
4
5
6
```

#### `else` with `while`
```python
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")
```

**Output**
```text
1
2
3
4
5
i is no longer less than 6
```

### For Loop
```python
marks = [91, 95, 88, 86, 82, 99, 80, 87, 96]

for x in marks:
    print(x)

# Looping through a string
for x in "banana":
  print(x)
```

**Output**
```text
91
95
88
86
82
99
80
87
96
b
a
n
a
n
a
```

```python
for x in [0, 1, 2]:
  pass
```

**Output**
```text
(No output)
```

---

## 9. Built-in Functions

### `sum()`
```python
marks = [91, 95, 88, 86, 82, 99, 80, 87, 96]
print(sum(marks))
```

**Output**
```text
818
```

### `max()`
```python
marks = [91, 95, 88, 86, 82, 99, 80, 87, 96]
print(f"Max value is : {max(marks)}")
```

**Output**
```text
Max value is : 99
```

### `range(x, y, z)`
```python
# Printing number from x to less than y
for number in range(1, 11):
    print(number)

# Printing number in steps of z
for number in range(1, 11, 2):
    print(number)
```

**Output**
```text
1
2
3
4
5
6
7
8
9
10
1
3
5
7
9
```

---

## 10. Functions

### Function Basics
```python
# Defining a function
def sayMyName():
    print("Rashed")

# Calling the function
sayMyName()
```

**Output**
```text
Rashed
```

---

## 11. Dictionaries

Dictionaries are used to store data values in `{key:value}` pairs.
A dictionary is a collection which is ordered*, changeable and does not allow duplicates.

### Creating a Dictionary
```python
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(car)
```

**Output**
```text
{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
```

### Add New Key-Value Pair
```python
car["price"] = 12999
print(car)
```

**Output**
```text
{'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'price': 12999}
```

### Edit Item
```python
car["brand"] = "Porsche"
print(car)
```

**Output**
```text
{'brand': 'Porsche', 'model': 'Mustang', 'year': 1964, 'price': 12999}
```

### Loop Through a Dictionary (Keys)
```python
for thing in car:
    print(thing)
```

**Output**
```text
brand
model
year
price
```

### Loop Through Dictionary (Key + Value)
```python
for key in car:
    print(key)
    print(car[key])
```

**Output**
```text
brand
Porsche
model
Mustang
year
1964
price
12999
```

### Max Value from Dictionary
```python
marks = {
    "Rashed": 99,
    "Shawon": 95,
    "Anik": 100,
    "Maruf": 91,
}

maxMarks = max(marks, key=marks.get)
print(maxMarks)
```

**Output**
```text
Anik
```

### Empty / Clear Dictionary
```python
empty_dictionary = {}

car = {}
car.clear()
print(car)
```

**Output**
```text
{}
```

### Getting Keys and Values
```python
car = {
  "brand": "Porsche",
  "model": "Mustang",
  "year": 1964,
  "price": 12999
}

x = car.keys()
print(x)

x = car.values()
print(x)

x = car.items()
print(x)
```

**Output**
```text
dict_keys(['brand', 'model', 'year', 'price'])
dict_values(['Porsche', 'Mustang', 1964, 12999])
dict_items([('brand', 'Porsche'), ('model', 'Mustang'), ('year', 1964), ('price', 12999)])
```

### Removing Items
```python
car.pop("year")
print(car)

car.popitem() # removes last key value from dictionary
print(car)
```

**Output**
```text
{'brand': 'Porsche', 'model': 'Mustang', 'price': 12999}
{'brand': 'Porsche', 'model': 'Mustang'}
```

### Looping Examples (Detailed)

#### Loop using dictionary directly
```python
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

for thing in car:
    print(thing)
```

**Output**
```text
brand
model
year
```

#### Loop using `keys()`
```python
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

for x in car.keys():
    print(x)
```

**Output**
```text
brand
model
year
```

#### Loop using key and value
```python
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

for key in car:
    print(key)
    print(car[key])
```

**Output**
```text
brand
Ford
model
Mustang
year
1964
```

#### Loop using `items()`
```python
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

for x, y in car.items():
    print(x, y)
```

**Output**
```text
brand Ford
model Mustang
year 1964
```

#### Loop using `values()`
```python
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

for x in car.values():
    print(x)
```

**Output**
```text
Ford
Mustang
1964
```
