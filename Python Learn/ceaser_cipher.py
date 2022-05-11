alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
            "u", "v", "w", "x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o",
            "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


def ceaser(text, shift_amount, direction):
    """Takes the text and shifts it by the shift_amount in the right direction"""
    message = []
    if direction == "decode":
        shift_amount *= -1
    for char in text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            shifted_letter = alphabet[new_position]
            message.append(shifted_letter)
        else:
           message.append(char)
    final_message = "".join(message)
    print(f"Your {direction}d is {final_message}")


should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt,type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift = shift % 26
    ceaser(text=text, shift_amount=shift, direction=direction)

    restart = input("Type 'yes' if you want to go again, Otherwise type 'no'\n")
    if restart == "no":
        should_continue = False
        print("Goodbye")

# def encrypt(plain_text, shift_amount):
#     message = []
#     for letter in plain_text:
#         if letter in alphabet:
#             position = alphabet.index(letter)
#             new_position = shift_amount + position
#             shifted_letter = alphabet[new_position]
#             message.append(shifted_letter)
#         else:
#             message.append(letter)
#     cipher_text = "".join(message)
#     print(f"The encoded text is {cipher_text}")
#
#
# def decrypt(cipher_text, shift_amount):
#     message = []
#     for letter in cipher_text:
#         if letter in alphabet:
#             position = alphabet.index(letter) + 26
#             new_position = position - shift_amount
#             shifted_letter = alphabet[new_position]
#             message.append(shifted_letter)
#         else:
#             message.append(letter)
#     plain_text = "".join(message)
#     print(f"The decoded text is {plain_text}")


# if direction == "encode":
#     encrypt(plain_text=text, shift_amount=shift)
# elif direction == "decode":
#     decrypt(cipher_text=text, shift_amount=shift)
