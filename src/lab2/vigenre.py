def generateKey(string, key):
    key = list(key)
    if len(string) == len(key):
        return (key)
    else:
        for i in range(len(string) - len(key)):
            key.append(key[i % len(key)])
    return ("".join(key))

def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    if keyword.isalpha() == False:
        return 'Your key doesnt a word'
    k = generateKey(plaintext, keyword)
    encrypt_text = []
    for i in range(len(plaintext)):
        if plaintext[i].isalpha():
            if plaintext[i].isupper():
                t = ord('A')
                x = (ord(plaintext[i]) + ord(k[i])) % 26
                x += t
                encrypt_text.append(chr(x))
            else:
                t = ord('a')
                x = (ord(plaintext[i]) + ord(k[i])) % 97
                x += t
                encrypt_text.append(chr(x))
        else:
            encrypt_text.append(plaintext[i])
    ciphertext = "".join(encrypt_text)
    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    if keyword.isalpha() == False:
        return 'Your key doesnt a word'
    k = generateKey(ciphertext, keyword)
    orig_text = []
    for i in range(len(ciphertext)):
        if ciphertext[i].isalpha():
            if ciphertext[i].isupper():
                t = ord('A')
                x = (ord(ciphertext[i]) - ord(k[i]) + 26) % 26
                x += t
                orig_text.append(chr(x))
            else:
                t = ord('a')
                x = (ord(ciphertext[i]) - ord(k[i]) + 26) % 26
                x += t
                orig_text.append(chr(x))
        else:
            orig_text.append(ciphertext[i])
    plaintext = "".join(orig_text)
    return plaintext
