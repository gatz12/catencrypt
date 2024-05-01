import string
import random

class process:
    def a(char, shift):
        if char.isdigit():
            nuovo_numero = (int(char) + shift) % 10
            return str(nuovo_numero)
        elif char.isalpha():
            codice_ascii = ord(char)
            if 65 <= codice_ascii <= 90:
                nuovo_codice_ascii = ((codice_ascii - 65 + shift) % 26) + 65
            elif 97 <= codice_ascii <= 122:
                nuovo_codice_ascii = ((codice_ascii - 97 + shift) % 26) + 97
            else:
                return char
            return chr(nuovo_codice_ascii)
        else:
            return char
        

def decrypt(text, key):
    decrypted_text = ""
    key = key * -1
    for char in text:
        if char.isalpha() or char.isdigit():
            decrypted_text += process.a(char, key)
        else:
            decrypted_text += char
    return decrypted_text

def encrypt(text, key):
    encrypted_text = ""
    key = int(key)  # Converte la chiave in un intero
    for char in text:
        if char.isalpha() or char.isdigit():
            encrypted_text += process.a(char, key)
        else:
            encrypted_text += char
    return encrypted_text

def generate():
    num = string.digits
    return ''.join(random.choices(num, k=36))