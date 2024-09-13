# EncryptPro: Vigenère Cipher Application

**Jan 2024 - Feb 2024**

EncryptPro is a web-based tool developed to perform encryption and decryption using the Vigenère cipher. This project allows users to securely communicate through key-based cryptanalysis while providing a simple and responsive interface for real-time processing.

## Tech Stack

- **Flask (Python)**: Backend framework for handling encryption/decryption logic.
- **HTML/CSS**: Structure and styling of the web interface.
- **JavaScript (jQuery)**: Dynamic interactivity on the client side.
- **Bootstrap**: For responsive and modern UI design.

## Features

- **Encryption and Decryption**: Allows users to input text and a key to encrypt or decrypt messages using the Vigenère cipher.
- **Responsive UI**: Built with Flask and Bootstrap to ensure a seamless experience across different devices.
- **Real-time Processing**: Provides instant encryption/decryption as the user inputs data.
- **Secure Communication**: Enhances message security by using a key-based cipher mechanism.

## Vigenère Cipher Overview

The Vigenère cipher is a method of encrypting alphabetic text by using a series of interwoven Caesar ciphers based on the letters of a keyword. It’s known for its resistance to frequency analysis, making it a strong cipher for secure communication.

### How it Works

1. **Encryption**: Each letter in the plaintext is shifted along the alphabet based on the corresponding letter in the key.
2. **Decryption**: The process is reversed by shifting the encrypted text based on the key to reveal the original message.

## Getting Started

### Prerequisites

- Python 3.x
- Flask

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/encryptpro.git
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the application:
    ```bash
    flask run
    ```

4. Open your browser and navigate to `http://127.0.0.1:5000/` to use the application.

## Usage

- Enter your **text** and **key** in the respective fields.
- Choose whether to **Encrypt** or **Decrypt**.
- View the result in real-time below the input fields.


## Future Improvements

- Adding support for more cipher techniques.
- Implementing key length validation for enhanced security.
- Expanding cryptanalysis options for breaking weak keys.

---

**Contributors**:  
Hetvi Bagdai (https://github.com/hetvi3012)

