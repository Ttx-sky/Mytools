import hashlib
import time


class HashTimeCipher:
    def __init__(self, secret_key):
        self.secret_key = secret_key

    def encrypt(self, message):

        timestamp = str(time.time())
        message_with_timestamp = message + "&" + timestamp
        hash_object = hashlib.sha256(self.secret_key.encode())
        hashed_key = hash_object.digest()
        cipher_text = ''
        for i in range(len(message_with_timestamp)):
            char = message_with_timestamp[i]
            char_int = ord(char)
            key_int = hashed_key[i % len(hashed_key)]
            cipher_int = (char_int + key_int) % 256
            cipher_text += chr(cipher_int)
        return cipher_text

    def decrypt(self, cipher_text):
        hash_object = hashlib.sha256(self.secret_key.encode())
        hashed_key = hash_object.digest()
        message_with_timestamp = ''
        for i in range(len(cipher_text)):
            char = cipher_text[i]
            char_int = ord(char)
            key_int = hashed_key[i % len(hashed_key)]
            message_int = (char_int - key_int) % 256
            message_with_timestamp += chr(message_int)
        message = message_with_timestamp[:-10]
        message = message.split("&")[0]
        return message


if __name__ == '__main__':
    cipher = HashTimeCipher('mysecretkey')
    encrypted_text = cipher.encrypt('Hello, world!')
    print('Encrypted text:', encrypted_text)
    decrypted_text = cipher.decrypt(encrypted_text)
    print('Decrypted text:', decrypted_text)
    time.sleep(10)
