import unittest
from src.lab3.sudoku import get_row, get_col, get_block,find_empty_positions, find_possible_values,solve, read_sudoku, group
class sudokutest(unittest.TestCase):
    def test_group(self):
        self.assertEqual(group([1, 2, 3, 4], 2), [[1, 2], [3, 4]])
        self.assertEqual(group([1, 2, 3, 4], 10), None)
    def test_get_row(self):
        self.assertEqual(get_row([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']], (0, 0)), ['1', '2', '.'])
        self.assertEqual(get_row([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']], (1, 0)), ['4', '.', '6'])
        with self.assertRaises(IndexError):
            get_row([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']], (4, 0))
    def test_get_col(self):
        self.assertEqual(get_col([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']], (0, 1)), ['2', '.', '8'])
        with self.assertRaises(IndexError):
            get_col([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']], (0, 3))
    def test_get_block(self):
        self.assertEqual(get_block([['5', '3', '.', '.', '7', '.' '.', '.', '.'], ['6', '.', '.', '1', '9', '5', '.', '.', '.'], ['.', '9', '8', '.', '.', '.', '.', '6', '.']], (0, 1)),  ['5', '3', '.', '6', '.', '.', '.', '9', '8'])
        with self.assertRaises(IndexError):
            get_block([['5', '3', '.', '.', '7', '.' '.', '.', '.'], ['6', '.', '.', '1', '9', '5', '.', '.', '.'], ['.', '9', '8', '.', '.', '.', '.', '6', '.']], (5, 1))
    def test_find_empty_position(self):
        self.assertEqual(find_empty_positions([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']]), (0,2))
        self.assertEqual(find_empty_positions([['1', '2', '7'], ['4', '5', '6'], ['7', '8', '9']]), None)
    def test_find_possible_values(self):
        self.assertEqual(find_possible_values([['5', '3', '.', '.', '7', '.' '.', '.', '.'], ['6', '.', '.', '1', '9', '5', '.', '.', '.'], ['.', '9', '8', '.', '.', '.', '.', '6', '.']], (0, 2)), {'1', '4', '2'})
    def test_solve(self):
        grid = read_sudoku('puzzle1.txt')
        res = solve(grid)
        tr = [['5', '3', '4', '6', '7', '8', '9', '1', '2'], ['6', '7', '2', '1', '9', '5', '3', '4', '8'], ['1', '9', '8', '3', '4', '2', '5', '6', '7'], ['8', '5', '9', '7', '6', '1', '4', '2', '3'], ['4', '2', '6', '8', '5', '3', '7', '9', '1'], ['7', '1', '3', '9', '2', '4', '8', '5', '6'], ['9', '6', '1', '5', '3', '7', '2', '8', '4'], ['2', '8', '7', '4', '1', '9', '6', '3', '5'], ['3', '4', '5', '2', '8', '6', '1', '7', '9']]
        self.assertEqual(res, tr)
        grid2 = [['1', '2', '.', '3', '4', '5', '6', '7', '8', '9'], ['6' ,'5', '3', '6', '6', '5', '6', '4', '6'], ['8', '7', '4', '4', '5', '6', '7', '8', '9'], ['1', '2', '5', '6', '6', '5', '6', '4', '6'], ['5', '3', '6', '6','5', '3', '6', '6', '5'], ['5', '2', '7', '4', '5', '6', '7', '8', '9'], ['4', '2', '8', '4', '5', '6', '7', '8', '9'], ['5', '3', '9', '4', '5', '6', '7', '8', '9'], ['6', '2', '7', '4', '5', '6', '7', '8', '9']]
        res2 = solve(grid2)
        tr = None
        self.assertEqual(res2, tr)