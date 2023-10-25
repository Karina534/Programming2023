def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.
    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            if char.isupper():
                stert_index = 65
            else:
                stert_index = 97
            encrypted_char = chr((ord(char) - stert_index + shift) % 26 + stert_index)
            ciphertext += encrypted_char
        else:
            ciphertext += char
    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.
    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            if char.isupper():
                start_index = 65
            else:
                start_index = 97
            decrypted_char = chr((ord(char) - start_index - shift) % 26 + start_index)
            plaintext += decrypted_char
        else:
            plaintext += char
    return plaintext