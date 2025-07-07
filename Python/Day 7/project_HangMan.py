import random

HANGMANPICS = [r''' 
  +---+ 
  |   | 
      | 
      | 
      | 
      | 
=========''', r'''
  +---+ 
  |   | 
  O   | 
      | 
      | 
      | 
=========''', r'''
  +---+ 
  |   | 
  O   | 
  |   | 
      | 
      | 
=========''', r'''
  +---+ 
  |   | 
  O   | 
 /|   | 
      | 
      | 
=========''', r'''
  +---+ 
  |   | 
  O   | 
 /|\  | 
      | 
      | 
=========''', r'''
  +---+ 
  |   | 
  O   | 
 /|\  | 
 /    | 
      | 
=========''', r'''
  +---+ 
  |   | 
  O   | 
 /|\  | 
 / \  | 
      | 
=========''']



word_list = [
    "apple", "banana", "chair", "house", "dog", "cat", "book", "car", "tree", "shoe", 
    "ball", "bat", "cup", "desk", "egg", "fish", "glove", "hat", "jacket", "key", 
    "lamp", "mouse", "notebook", "orange", "pen", "pencil", "plane", "rabbit", "rose", 
    "sun", "table", "tiger", "towel", "window", "zebra", "bread", "cloud", "coin", 
    "fork", "grass", "ice", "jelly", "leaf", "mirror", "piano", "socks", "star", 
    "water", "wave", "yarn", "zoo", "peach", "planet", "shirt", "sock"
]

# word_list = ["apple", "cat", "cube"]


word = random.choice(word_list)
#print(word)

placeholder = ""

for x in word:
    placeholder += "_"
print(f"{placeholder}\n")

is_word_guessed = False
correct_letters = []
life_count = 0

while not is_word_guessed:
    guess = input("Guess a letter : ").lower()

    hint = ""

    for letter in word:
        if letter == guess:
            hint += letter
            correct_letters.append(letter)
            print("You guessed a correct letter!")
        elif letter in correct_letters:
            hint += letter
            print("You gussed the letter already!")
        else:
            hint += "_"

    if guess not in word:
        life_count += 1
        print("You gussed a wrong letter!")
        print(f"{6-life_count}/6 lives left!")

    print(HANGMANPICS[life_count])
    print(hint)

    if hint == word:
        is_word_guessed = True
        print("You guessed the Word...You Won!!!")
    elif life_count == 6:
        print("HANGMAN! You lost!!!")
        is_word_guessed = True