from morse3 import Morse as m


def convert_to_morse(text_to_convert):
    return m(text_to_convert).stringToMorse()


def convert_to_text(morse_to_convert):
    return m(morse_to_convert).morseToString()


def morse_code_program():
    continue_app = True
    while continue_app:
        action_type = input("Enter 'E' to encrypt from text to morse code or 'D' to decrypt from morse code to text: ")
        if action_type == 'E' or action_type == 'e':
            text_to_encrypt_to_morse_code = input("Enter the text you'd like to convert to morse code: ")
            morse_text = convert_to_morse(text_to_encrypt_to_morse_code)
            print(morse_text)
        elif action_type == 'D' or action_type == 'd':
            text_to_decrypt_to_text = input("Enter the morse code you'd like to convert to text: ")
            decrypted_morse = convert_to_text(text_to_decrypt_to_text)
            print(decrypted_morse)
        continue_using_app = input("Do you want to continue? Y/N: ")
        if continue_using_app == 'N' or continue_using_app == 'n':
            continue_app = False


morse_code_program()