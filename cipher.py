import string

def vigenere_cipher_encrypt(plain_text, key):
    '''Encrypts text using the Vigenere cipher given a key.'''
    result_encrypted = ""
    key_length = len(key)
    for index, char in enumerate(plain_text):
        if char.isalpha():
            shift_amount = (ord(key[index % key_length]) - ord('a')) % 26
            result_encrypted += chr((ord(char) - ord('a') + shift_amount) % 26 + ord('a'))
    return result_encrypted

def vigenere_cipher_decrypt(encrypted_text, key):
    '''Decrypts text that was encrypted using the Vigenere cipher given a key.'''
    result_decrypted = ""
    key_length = len(key)
    for index, char in enumerate(encrypted_text):
        if char.isalpha():
            shift_amount = (ord(key[index % key_length]) - ord('a')) % 26
            result_decrypted += chr((ord(char) - ord('a') - shift_amount + 26) % 26 + ord('a'))
    return result_decrypted
