#Island Code
import time
import random

time.sleep(2)

print("       __..-----')")
time.sleep(0.07)
print("      ,.--._ .-'_..--...-'")
time.sleep(0.07)
print("     '-\"'. _/_ /  ..--''\"\"'-.")
time.sleep(0.07)
print("     _.--\"\"...:._:(_ ..:\":: \\")
time.sleep(0.07)
print("  .-' ..::--\"\"_(##)#)\"':. \\ \\)  ")
time.sleep(0.07)
print(" /_:-:'/  :__(##)##)    ): )   '-.")
time.sleep(0.07)
print('"  / |  :\' :/""\\\\///)  /:.\'  ')
time.sleep(0.07)
print("  / :( :( :(   (#//)  \"       .-\'\\.")
time.sleep(0.07)
print(" / :/|\\ :\\_:\\   \\#//\\/  |  \\")
time.sleep(0.07)
print("|:/ | \"\"--\':\\   (#//)      \ \  '")
time.sleep(0.07)
print(" \\/  \\ :|  \\ :\\  (#//)")
time.sleep(0.07)
print("      \\:\\   \'.\':. \\#//\\")
time.sleep(0.07)
print("       ':|    \"--\'(#///)")
time.sleep(0.07)
print("                  (#///)")
time.sleep(0.07)
print("                  (#///)")
time.sleep(0.07)
print("                   \\#///\\")
time.sleep(0.07)
print("                   (##///)")
time.sleep(0.07)
print("                   (##///)")
time.sleep(0.07)
print("                   (##///)")
time.sleep(0.07)
print("                   (##///)")
time.sleep(0.07)
print("                    \\##///\\")
time.sleep(0.07)
print("                    (###///)")
time.sleep(0.07)
print("                    (sjw////)__...-----....__")
time.sleep(0.07)
print("                    (#/::'''                 \"\"--.._")
time.sleep(0.07)
print("               __..-'''                             \"-._")
time.sleep(0.07)
print("       __..--\"\"                                         '\"._")
time.sleep(0.07)
print("___..--\"\"                                                    \"-..____")
time.sleep(0.07)
print("  (_ \"\"---....___                                     __...--\"\" _)")
time.sleep(0.07)
print('    """--...  ___"""""-----......._______......----"""     --"""')
time.sleep(1)
print("")

print("$$$$$$\  $$$$$$\  $$\        $$$$$$\  $$\   $$\ $$$$$$$\         $$$$$$\   $$$$$$\  $$$$$$$\  $$$$$$$$\ ")
time.sleep(0.1)
print("\_$$  _|$$  __$$\ $$ |      $$  __$$\ $$$\  $$ |$$  __$$\       $$  __$$\ $$  __$$\ $$  __$$\ $$  _____|")
time.sleep(0.1)
print("  $$ |  $$ /  \__|$$ |      $$ /  $$ |$$$$\ $$ |$$ |  $$ |      $$ /  \__|$$ /  $$ |$$ |  $$ |$$ |      ")
time.sleep(0.1)
print("  $$ |  \$$$$$$\  $$ |      $$$$$$$$ |$$ $$\$$ |$$ |  $$ |      $$ |      $$ |  $$ |$$ |  $$ |$$$$$\    ")
time.sleep(0.1)
print("  $$ |   \____$$\ $$ |      $$  __$$ |$$ \$$$$ |$$ |  $$ |      $$ |      $$ |  $$ |$$ |  $$ |$$  __|   ")
time.sleep(0.1)
print("  $$ |  $$\   $$ |$$ |      $$ |  $$ |$$ |\$$$ |$$ |  $$ |      $$ |  $$\ $$ |  $$ |$$ |  $$ |$$ |      ")
time.sleep(0.1)
print("$$$$$$\ \$$$$$$  |$$$$$$$$\ $$ |  $$ |$$ | \$$ |$$$$$$$  |      \$$$$$$  | $$$$$$  |$$$$$$$  |$$$$$$$$\ ")
time.sleep(0.1)
print("\______| \______/ \________|\__|  \__|\__|  \__|\_______/        \______/  \______/ \_______/ \________|")
time.sleep(0.1)
print("")
time.sleep(0.1) 
print("                                  ISLAND CODE ENCRYPTOR TERMINAL VERSION")
time.sleep(0.1)
print("                                                By ropzFaZe")
time.sleep(0.1)
print("                                                   v1.0")
time.sleep(0.1)
print("=========================================================================================================")
time.sleep(1)

print("Functions: 1. Cipher Code, 2. ASCII Code, 2. Binary Code")

while True:
    time.sleep(2)
    ask = input("Input Number For Function: ")

    if ask == "1":
        print("Loading Cipher encryptor...")
        time.sleep(1)
        print("Cipher Encryptor v1.3")
        time.sleep(0.5)
        def encode(message, shift):
            encoded_message = ""
            for char in message:
                if char.isalpha():
                    ascii_offset = 65 if char.isupper() else 97
                    encoded_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
                    encoded_message += encoded_char
                else:
                    encoded_message += char
            return encoded_message

        def decode(message, shift):
            return encode(message, -shift)

        
        message = input("Message: ")
        shift = int(input("Shift value: "))
        num = 0
        selections = input("'1' for encode and '2' for decode: ")

        if selections == "2":
            num = shift
            shift = shift - num - num
            encoded_message = encode(message, shift)
            print("Decoded message:", encoded_message)

        elif selections == "1":
            encoded_message = encode(message, shift)
            print("Encoded message:", encoded_message)
        time.sleep(1)
        print("")
        
    elif ask == "2":
        print("Loading ASCII encryptor...")
        time.sleep(1)
        print("ASCII Encryptor v1.0")
        time.sleep(0.5)
        def encode(message):
            encoded_message = ""
            for char in message:
                encoded_char = str(ord(char))
                encoded_message += encoded_char + " "
            return encoded_message.strip()

        def decode(message):
            decoded_message = ""
            encoded_chars = message.split()
            for encoded_char in encoded_chars:
                decoded_char = chr(int(encoded_char))
                decoded_message += decoded_char
            return decoded_message

        selections = input("'1' for encode and '2' for decode: ")

        if selections == "1":
            message = input("Message: ")
            encoded_message = encode(message)
            print("Encoded message:", encoded_message)

        elif selections == "2":
            message = input("Message: ")
            decoded_message = decode(message)
            print("Decoded message:", decoded_message)
        time.sleep(1)
        print("")
    
    elif ask == "3":
        print("Loading Binary encryptor...")
        time.sleep(1)
        print("Binary Encryptor v1.0")
        time.sleep(0.5)
        def encrypt_sentence(sentence):
            encrypted_sentence = ""
            
            for char in sentence:
                binary_char = bin(ord(char))[2:]  
                encrypted_sentence += binary_char + " "  
            
            return encrypted_sentence.strip()  

        def decrypt_sentence(encrypted_sentence):
                decrypted_sentence = ""
                
                binary_chars = encrypted_sentence.split()  
                
                for binary_char in binary_chars:
                    decimal_char = int(binary_char, 2) 
                    decrypted_char = chr(decimal_char)  
                    decrypted_sentence += decrypted_char
                
                return decrypted_sentence

        select = input("'1' for encode and '2' for decode: ")

        if select == "1":
            sentence = input("Enter a sentence to encrypt: ")
            encrypted_sentence = encrypt_sentence(sentence)
            print("Encrypted sentence:", encrypted_sentence)

        elif select == "2":
            encrypted_sentence = input("Enter the encrypted sentence: ")
            decrypted_sentence = decrypt_sentence(encrypted_sentence)
            print("Decrypted sentence:", decrypted_sentence)
        time.sleep(1)
        print("")
