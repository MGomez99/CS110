import random


def encrypt(message):
    """
    Encrypts message
    :param message: User's input message
    :return: encrypted message[str], cipher dictionary[dictionary]
    """

    list_of_values = []
    for i in range(32, 127):
        list_of_values += [chr(i)]  # list of values of ASCII 32-126 for values

    cipher = {}  # cipher dictionary

    for i in range(32, 127):
        x = list_of_values.pop(list_of_values.index(random.choice(list_of_values)))  # pops and assigns a random item
        cipher[chr(i)] = x

    encrypted_message = ''
    for c in message:
        if c in cipher:
            encrypted_message += cipher[c]
        else:
            encrypted_message += c

    return encrypted_message, cipher


def decrypt(encrypted_message, cipher):
    """
    Decrypts the encrypted message
    :param encrypted_message: User's message after encryption
    :param cipher: Dictionary to decrypt message
    :return: decrypted message[str]
    """
    decrypted_message = ''
    cipher_decrypter = dict((y, x) for x, y in cipher.items())  # switches key and values to decrypt

    for c in encrypted_message:
        if c in cipher_decrypter:
            decrypted_message += cipher_decrypter[c]
        else:
            decrypted_message += c

    return decrypted_message
