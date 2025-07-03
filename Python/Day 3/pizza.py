# Small = 15
# Medium = 20
# Large = 25

# pepperoni small = 2
# pepperoni medium or large = 3

# extra cheese of any = 1

print("Welcome to Python Pizza")

size = input("What size pizza do you want? S,M,L : ").lower()
pepperoni = input("Do you want pepperoni on your pizza? Y or N : ").lower()
cheese = input("Do you want extra cheese? Y or N : ").lower()

bill = 0 

if size == "s":
    bill = 15
    if pepperoni == "y":
        bill += 2
    if cheese == "y":
        bill += 1
        print(f"Your bill is : {bill}")

elif size == "m":
    bill = 20
    if pepperoni == "y":
        bill += 3
    if cheese == "y":
        bill += 1
        print(f"Your bill is : {bill}")
else:
    bill = 25
    if pepperoni == "y":
        bill += 3
    if cheese == "y":
        bill += 1
        print(f"Your bill is : {bill}")