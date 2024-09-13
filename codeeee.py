import string

def strip_text(file_path):
    '''Removes spaces, newlines, tabs, punctuation, and digits from the content of the given file, leaving only lowercase letters.'''
    with open(file_path, 'r') as file_handle:
        content = file_handle.read().lower()
        content = content.translate(str.maketrans('', '', string.whitespace + string.punctuation + string.digits))
    return content

def count_character_frequency(input_string):
    '''Counts the frequency of each character in a string and returns a dictionary with these counts.'''
    frequency_dict = {}
    for char in input_string:
        if char in frequency_dict:
            frequency_dict[char] += 1
        else:
            frequency_dict[char] = 1
    return frequency_dict

def encrypt_by_substitution(plain_text, mapping_dict):
    '''Uses a dictionary mapping for substitution to encrypt a string.'''
    encrypted_result = ""
    for char in plain_text:
        encrypted_result += mapping_dict.get(char, char)
    return encrypted_result

def decrypt_by_substitution(cipher_text, mapping_dict):
    '''Uses a dictionary mapping for substitution to decrypt a string.'''
    reversed_mapping = {value: key for key, value in mapping_dict.items()}
    decrypted_result = ""
    for char in cipher_text:
        decrypted_result += reversed_mapping.get(char, char)
    return decrypted_result

def predict_substitution_mapping(cipher_text):
    '''Predicts the substitution cipher mapping used to encrypt the text by analyzing letter frequency.'''
    freq_dict = count_character_frequency(cipher_text)
    freq_sorted = sorted(freq_dict.items(), key=lambda item: item[1], reverse=True)
    typical_freq = "etaoinshrdlcumwfgypbvkjxqz"
    predicted_mapping = {}
    for i, letter in enumerate(typical_freq):
        predicted_mapping[letter] = freq_sorted[i][0]
    return predicted_mapping

def vigenere_cipher_encrypt(plain_text, key):
    '''Encrypts text using the Vigenere cipher given a key.'''
    result_encrypted = ""
    key_length = len(key)
    for index, char in enumerate(plain_text):
        shift_amount = (ord(key[index % key_length]) - ord('a')) % 26
        result_encrypted += chr((ord(char) - ord('a') + shift_amount) % 26 + ord('a'))
    return result_encrypted

def vigenere_cipher_decrypt(encrypted_text, key):
    '''Decrypts text that was encrypted using the Vigenere cipher given a key.'''
    result_decrypted = ""
    key_length = len(key)
    for index, char in enumerate(encrypted_text):
        shift_amount = (ord(key[index % key_length]) - ord('a')) % 26
        result_decrypted += chr((ord(char) - ord('a') - shift_amount + 26) % 26 + ord('a'))
    return result_decrypted

def analyze_and_predict_vigenere_key(encrypted_text, key_length):
    '''Given the encrypted text and the key length, predicts the Vigenere cipher key.'''
    freq_dict = count_character_frequency(encrypted_text)
    freq_sorted = sorted(freq_dict.items(), key=lambda item: item[1], reverse=True)
    typical_freq = "etaoinshrdlcumwfgypbvkjxqz"
    key_predicted = ""
    for i in range(key_length):
        key_predicted += typical_freq[i]
    return key_predicted

def find_vigenere_key_length(encrypted_text):
    '''Analyzes the encrypted text to predict the length of the Vigenere cipher key.'''
    freq_dict = count_character_frequency(encrypted_text)
    freq_sorted = sorted(freq_dict.items(), key=lambda item: item[1], reverse=True)
    typical_freq = "etaoinshrdlcumwfgypbvkjxqz"
    for index, letter in enumerate(typical_freq):
        if letter == 'e':
            return index
    return None

def cryptanalysis_vigenere(encrypted_text):
    '''Performs a complete cryptanalysis of the Vigenere cipher to find the key and decrypt the text.'''
    key_length = find_vigenere_key_length(encrypted_text)
    key = analyze_and_predict_vigenere_key(encrypted_text, key_length)
    decrypted_text = vigenere_cipher_decrypt(encrypted_text, key)
    return key, decrypted_text

def user_interface():
    print("Select an encryption/decryption method:")
    print("1. Encrypt using Substitution Cipher")
    print("2. Decrypt using Substitution Cipher")
    print("3. Encrypt using Vigenère Cipher")
    print("4. Decrypt using Vigenère Cipher")
    print("5. Analyze Substitution Cipher")
    print("6. Analyze Vigenère Cipher")
    
    user_choice = int(input("Enter your choice (1-6): "))
    file_path = input("Enter the file path: ")
    content = strip_text(file_path)

    if user_choice == 1:
        substitution_map = {}
        print("Define your substitution map (26 letters):")
        for i in range(26):
            original_char = chr(97 + i)
            substituted_char = input(f"Replace {original_char} with: ")
            substitution_map[original_char] = substituted_char
        encrypted_text = encrypt_by_substitution(content, substitution_map)
        print("Encrypted Text:", encrypted_text)
    elif user_choice == 2:
        substitution_map = {}
        print("Define your substitution map (26 letters):")
        for i in range(26):
            original_char = chr(97 + i)
            substituted_char = input(f"Replace {original_char} with: ")
            substitution_map[original_char] = substituted_char
        decrypted_text = decrypt_by_substitution(content, substitution_map)
        print("Decrypted Text:", decrypted_text)
    elif user_choice == 3:
        key = input("Enter the Vigenère key: ")
        encrypted_text = vigenere_cipher_encrypt(content, key)
        print("Encrypted Text:", encrypted_text)
    elif user_choice == 4:
        key = input("Enter the Vigenère key: ")
        decrypted_text = vigenere_cipher_decrypt(content, key)
        print("Decrypted Text:", decrypted_text)
    elif user_choice == 5:
        predicted_map = predict_substitution_mapping(content)
        print("Predicted Substitution Map:")
        for original, prediction in predicted_map.items():
            print(f"{original} -> {prediction}")
    elif user_choice == 6:
        key, decrypted_text = cryptanalysis_vigenere(content)
        print("Predicted Key:", key)
        print("Decrypted Text:", decrypted_text)
    else:
        print("Invalid choice selected.")

if __name__ == "__main__":
    user_interface()
