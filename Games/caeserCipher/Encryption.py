import alphabets

def encrypt(original_text, shift):
    encrypted_string = ""
    for letter in original_text:
        if letter not in alphabets.alphabet:
            encrypted_string += letter
        else:
            encrypted_string += alphabets.alphabet[(alphabets.alphabet.index(letter) + shift)]

    print(f"The encrypted text is: {encrypted_string}")
