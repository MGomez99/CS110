import cipher


def main():
    print("***Everything is case sensitive***")
    message = ''
    while message != 'q':
        message = input("What is your message? To quit enter 'q': ")
        if message == 'q':  # solely used for the first iteration, if input is q then end loop
            break
        encryption = cipher.encrypt(message)
        print('Encrypted message:\n', encryption[0], "\nCipher Dictionary:\n", encryption[1])
        response = input("Would you like to decrypt? y/n: ")
        if response == 'y':  # Asks if user wants to decrypt
            decryption = cipher.decrypt(encryption[0], encryption[1])
            print("Decrypted message:", decryption)
    print("'q' detected! Terminating sequence.")


main()
