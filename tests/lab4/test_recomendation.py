import unittest
from src.lab4.recomendation import recomendation, Films

class RecomendationTestCace(unittest.TestCase):
    def test_recomendation(self):
        self.assertEqual(recomendation([1, 3]), 'KJBf')
        self.assertEqual(recomendation([1, 4]), 'Gef')
        self.assertEqual(recomendation([]), 'KH')
        self.assertEqual(recomendation([6, 7]), 'We can`t recomend you a film')
    def test_Film(self):
        film1 = Films(1, 'Pop')
        self.assertEqual(film1.veuvers, 0)