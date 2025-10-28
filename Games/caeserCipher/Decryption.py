import alphabets
import main

def decrypt(original_text, shift):
    decrypted_string = ""
    for letter in original_text:
        if letter not in alphabets.alphabet:
            decrypted_string += letter
        else:
            decrypted_string += alphabets.alphabet[(alphabets.alphabet.index(letter) - shift)]

    print(f"The encrypted text is: {decrypted_string}")
