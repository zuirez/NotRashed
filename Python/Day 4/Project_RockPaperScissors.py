import random

print("WELCOME TO THE GREATED CHALLENGE EVER, HUMAN VS COMPUTER!!!")
print("Game name : Rock Paper Scissors!!!")
human = int(input("What do you choose? 0=rock, 1=paper, 2=scissors : "))

computer = random.randint(0,2)

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

if human>=0 and human<=2:
    if human == 0:
        print(f"You chose : {rock}")
    elif human == 1:
        print(f"You chose : {paper}")
    elif human == 2:
        print(f"You chose : {scissors}")

    if computer == 0:
        print(f"Computer chose : {rock}")
    elif computer == 1:
        print(f"Computer chose : {paper}")
    elif computer == 2:
        print(f"Computer chose : {scissors}")

    if human == computer:
        print("Draw")
    elif (human == 0 and computer == 1) or (human == 1 and computer == 2) or (human == 2 and computer == 0):
        print("Computer Wins!!!")
    else:
        print("Human wins!!!")

else:
    print("Invalid number!")