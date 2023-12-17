import unittest
from src.lab2.caesar import encrypt_caesar, decrypt_caesar

class testencrypt(unittest.TestCase):
    def test_encrypt_caesar(self):
        plaintext = 'PYTHON'
        shift = 3
        expect_caphertext = 'SBWKRQ'
        caphertext = encrypt_caesar(plaintext, shift)
        self.assertEqual(caphertext, expect_caphertext)
        self.assertEqual(encrypt_caesar('12', 3), '12')
        self.assertEqual(encrypt_caesar('', 3), '')
        self.assertEqual(encrypt_caesar('%^', 3), '%^')

    def test_decrypt_caesar(self):
        caphertext = 'SBWKRQ'
        shift = 3
        expect_plaintext = 'PYTHON'
        plaintext = decrypt_caesar(caphertext, shift)
        self.assertEqual(plaintext, expect_plaintext)
        self.assertEqual(decrypt_caesar('12', 3), '12')
        self.assertEqual(decrypt_caesar('', 3), '')
        self.assertEqual(decrypt_caesar('%^', 3), '%^')


if __name__=='__main__':
    unittest.main()