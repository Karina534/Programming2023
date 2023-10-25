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
    m = 0 if plaintext.islower() else 1
    s = plaintext.upper()
    key = keyword.upper()
    k = generateKey(s, key)
    encrypt_text = []
    for i in range(len(s)):
        if s[i].isalpha():
            x = (ord(s[i]) + ord(k[i])) % 26
            x += ord('A')
            encrypt_text.append(chr(x))
        else:
            encrypt_text.append(s[i])
    ciphertext = "".join(encrypt_text)
    if m == 0:
        return ciphertext.lower()
    else:
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
    m = 0 if ciphertext.islower() else 1
    ci = ciphertext.upper()
    key = keyword.upper()
    k = generateKey(ci, key)
    orig_text = []
    for i in range(len(ci)):
        if ci[i].isalpha():
            x = (ord(ci[i]) - ord(k[i]) + 26) % 26
            x += ord('A')
            orig_text.append(chr(x))
        else:
            orig_text.append(ci[i])
    plaintext = "".join(orig_text)
    if m == 0:
        return plaintext.lower()
    else:
        return plaintext