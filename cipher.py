def vigenere_cipher_encrypt(plain_text, key):
    '''Encrypts text using the Vigenere cipher given a key, while preserving spaces and punctuation.'''
    result_encrypted = ""
    key_length = len(key)
    key_index = 0  # To handle non-alphabetic characters correctly
    for char in plain_text:
        if char.isalpha():  # Only encrypt alphabetic characters
            shift_amount = (ord(key[key_index % key_length]) - ord('a')) % 26
            result_encrypted += chr((ord(char) - ord('a') + shift_amount) % 26 + ord('a'))
            key_index += 1  # Increment only when a letter is encrypted
        else:
            result_encrypted += char  # Keep spaces and punctuation as is
    return result_encrypted


def vigenere_cipher_decrypt(encrypted_text, key):
    '''Decrypts text that was encrypted using the Vigenere cipher, while preserving spaces and punctuation.'''
    result_decrypted = ""
    key_length = len(key)
    key_index = 0  # To handle non-alphabetic characters correctly
    for char in encrypted_text:
        if char.isalpha():  # Only decrypt alphabetic characters
            shift_amount = (ord(key[key_index % key_length]) - ord('a')) % 26
            result_decrypted += chr((ord(char) - ord('a') - shift_amount + 26) % 26 + ord('a'))
            key_index += 1  # Increment only when a letter is decrypted
        else:
            result_decrypted += char  # Keep spaces and punctuation as is
    return result_decrypted
