import Decryption
import Encryption
import alphabets
print(alphabets.art)
should_continue = True
while should_continue:
    original_text = input("Enter the text : ")
    shift = int(input("Enter the shift of the letters: "))
    direction = input("Enter the direction of the shift , L or R: \n")
    if direction == "L":
        Decryption.decrypt(original_text, shift)
    elif direction == "R":
        Encryption.encrypt(original_text, shift)
    else:
        print("Invalid direction")

    restart= input("Do you want to continue? (yes/no) \n").lower()
    if restart == "no":
        should_continue = False
        print("Thank you for using CeaserCipher")
