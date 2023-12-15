import unittest
from src.lab2.rsa import encrypt, decrypt, is_prime, gcd, multiplicative_inverse, generate_keypair


class testrsa(unittest.TestCase):
    def test_is_prime(self):
        self.assertEqual(is_prime(3), True)
        self.assertEqual(is_prime(8), False)
    def test_gcd(self):
        self.assertEqual(gcd(12, 15), 3)
        self.assertEqual(gcd(11, 15), 1)
        self.assertEqual(gcd(11, 0), 11)
    def test_multiplication(self):
        self.assertEqual(multiplicative_inverse(7, 40), 23)
        self.assertEqual(multiplicative_inverse(13, 45), 7)
    def test_key(self):
        with self.assertRaisesRegexp(ValueError, "Both numbers must be prime."):
            generate_keypair(4, 7)
        with self.assertRaisesRegexp(ValueError, "p and q cannot be equal"):
            generate_keypair(5, 5)


    def test_encrypt(self):
        self.assertEqual(encrypt((161, 455), 'He'), [102, 446])
        self.assertEqual(encrypt((143, 355), 'F'), [70])
    def test_decrypt(self):
        self.assertEqual(decrypt((161, 455), [102, 446]), 'He')
        self.assertEqual(decrypt((47, 355), [70]), 'F')
