dictionary = {}

print( '''
  _______ _             _____ _ _            _                        _   _              
 |__   __| |           / ____(_) |          | |       /\             | | (_)             
    | |  | |__   ___  | (___  _| | ___ _ __ | |_     /  \  _   _  ___| |_ _  ___  _ __  
    | |  | '_ \ / _ \  \___ \| | |/ _ \ '_ \| __|   / /\ \| | | |/ __| __| |/ _ \| '_ \ 
    | |  | | | |  __/  ____) | | |  __/ | | | |_   / ____ \ |_| | (__| |_| | (_) | | | |
    |_|  |_| |_|\___| |_____/|_|_|\___|_| |_|\__| /_/    \_\__,_|\___|\__|_|\___/|_| |_|                                                                                       
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
''')
print("Welcome to the auction program!")

end = True

while end:
    name = input("What is your name? : ")
    bid = int(input("What is your bid? : "))

    dictionary[f"{name}"] = bid
    otherBidders = input("Are there any other bidders? Type 'Yes' or 'no'\n").lower()

    if otherBidders == "yes":
        end = True
    else:
        end = False

max = 0

for x in dictionary:
    if dictionary[x] > max:
        max = dictionary[x]

for x,y in dictionary.items():
    if dictionary[x] == max:
        print(f"The winner is {x} with a bid of {max}")
