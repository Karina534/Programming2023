import unittest
from src.lab2.vigenre import encrypt_vigenere, decrypt_vigenere
class vigenre_test(unittest.TestCase):
    def test_encrypt(self):
        self.assertEqual(encrypt_vigenere('python', 'a'), 'python')
        self.assertEqual(encrypt_vigenere('PYTHON', 'A'), 'PYTHON')
        self.assertEqual(encrypt_vigenere('ATTACKATDAWN', 'LEMON'), 'LXFOPVEFRNHR')
        self.assertEqual(encrypt_vigenere('24', 'LEMON'), '24')
        self.assertEqual(encrypt_vigenere('№:', 'LEMON'), '№:')
        self.assertEqual(encrypt_vigenere('python', '4'), 'Your key doesnt a word')

    def test_decrypt(self):
        self.assertEqual(decrypt_vigenere('python', 'a'), 'python')
        self.assertEqual(decrypt_vigenere('PYTHON', 'A'), 'PYTHON')
        self.assertEqual(decrypt_vigenere('LXFOPVEFRNHR', 'LEMON'), 'ATTACKATDAWN')
        self.assertEqual(decrypt_vigenere('24', 'LEMON'), '24')
        self.assertEqual(decrypt_vigenere('№:', 'LEMON'), '№:')
        self.assertEqual(decrypt_vigenere('python', '4'), 'Your key doesnt a word')
