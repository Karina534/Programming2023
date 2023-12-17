import unittest
from os.path import  dirname, join
from src.lab4.list_of_respondents import Groups, Respondent

current_dir = dirname(__file__)
l = join(current_dir, './respondents.txt')


class RespondentsTestCase(unittest.TestCase):
    def test_add_respondent(self):
        group = Groups()
        group.add_respondent("Li", 3)
        group.add_respondent("Po", 35)
        self.assertTrue(group.respondents_0_18[0], ("Li", 3))
        self.assertTrue(group.respondents_26_35, ("Po", 35))

    def test_sorting(self):
        group = Groups()
        group.add_respondent("Li", 5)
        group.add_respondent("Po", 3)
        group.sorting()
        self.assertTrue(group.respondents_0_18, (("Po", 3), ("Li", 5)))

    def test_get_str_mas(self):
        group = Groups()
        group.add_respondent("Li", 5)
        group.add_respondent("Po", 3)
        self.assertTrue(group.get_str_mas(group.respondents_0_18), "Li, 5; Po, 3;")
