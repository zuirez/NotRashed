alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def encrypt(original_text, shift_amount):
    encrypted_text = ""

    for letter in original_text:
        indexAtAlphabet = (alphabet.index(letter) + shift_amount) % 26
        encrypted_text = encrypted_text + alphabet[indexAtAlphabet]
    print(f"Encrypted text : {encrypted_text}")

def decrypt(original_text, shift_amount):
    decrypted_text = ""

    for letter in original_text:
        indexAtAlphabet = (alphabet.index(letter) - shift_amount) % 26
        decrypted_text = decrypted_text + alphabet[indexAtAlphabet]
    print(f"Decrypted text : {decrypted_text}")

def decision():
    decision = input("Type 'yes' if you want to go again, type 'no' if you want to exit the program.").lower()

    if decision == "yes":
        return True
    elif decision == "no":
        print("Exiting program...")
        return False
    else:
        print("Exiting program...")
        return False

one_more = True

while one_more:
    action = input("Type 'encode' to encrypt, type 'decode' to decrypt : ").lower()

    if action == "encode":
        original_text = input("Enter text to encrypt : ").upper()
        shift_amount = int(input("Enter shift amount : "))
        encrypt(original_text, shift_amount)
        one_more = decision()

    elif action == "decode":
        original_text = input("Enter text to encrypt : ").upper()
        shift_amount = int(input("Enter shift amount : "))
        decrypt(original_text, shift_amount)
        one_more = decision()
    else:
        print("Unknown command!!!")