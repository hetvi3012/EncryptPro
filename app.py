from flask import Flask, render_template, request
from cipher import vigenere_cipher_encrypt, vigenere_cipher_decrypt

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encrypt', methods=['POST'])
def encrypt():
    text = request.form['plain_text']
    key = request.form['key']
    encrypted_text = vigenere_cipher_encrypt(text.lower(), key.lower())
    return render_template('index.html', result=encrypted_text, operation="Encryption")

@app.route('/decrypt', methods=['POST'])
def decrypt():
    text = request.form['cipher_text']
    key = request.form['key']
    decrypted_text = vigenere_cipher_decrypt(text.lower(), key.lower())
    return render_template('index.html', result=decrypted_text, operation="Decryption")

if __name__ == "__main__":
    app.run(debug=True)
