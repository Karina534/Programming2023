import multiprocessing
import pathlib
import time
import typing as tp
import numpy as np
import multiprocessing
import time

import numpy as np

T = tp.TypeVar("T")


def read_sudoku(path: tp.Union[str, pathlib.Path]) -> tp.List[tp.List[str]]:
    """Прочитать Судоку из указанного файла"""
    path = pathlib.Path(path)
    with path.open() as f:
        puzzle = f.read()
    return create_grid(puzzle)


def create_grid(puzzle: str) -> tp.List[tp.List[str]]:
    digits = [c for c in puzzle if c in "123456789."]
    grid = group(digits, 9)
    return grid


def display(grid: tp.List[tp.List[str]]) -> None:
    """Вывод Судоку"""
    width = 2
    line = "+".join(["-" * (width * 3)] * 3)
    for row in range(9):
        print("".join(grid[row][col].center(width) + ("|" if str(col) in "25" else "") for col in range(9)))
        if str(row) in "25":
            print(line)
    print()


def group(values: tp.List[T], n: int) -> tp.List[tp.List[T]]:
    """
    параметры:
        values: tp.List[T] - Массив из различных данных, будущий Судоку
        n: int - целочисленное чсло, которое показывает на массивы какойй длинны должен быть разделен массив
    результат:
        tp.List[tp.List[T]] - Массив из подмассивов длинны n - Судоку

    Сгруппировать значения values в список, состоящий из списков по n элементов
    >>> group([1,2,3,4], 2)
    [[1, 2], [3, 4]]
    >>> group([1,2,3,4,5,6,7,8,9], 3)
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    """
    result = []
    if n > len(values):
        return [[]]
    else:
        for i in range(0, len(values), n):
            result.append(values[i:i + n])
    return result


def get_row(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    """
    параметры:
        grid: tp.List[tp.List[str]] - Двойной массив со строками - Судоку
        pos: tp.Tuple[int, int] - позиция (строка, столбец) элемента для котрого ищем строку
    результат:
        tp.List[str] - массив строк. Все элементы в строке с элементом на позиции pos

    Возвращает все значения для номера строки, указанной в pos
    >>> get_row([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']], (0, 0))
    ['1', '2', '.']
    >>> get_row([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']], (1, 0))
    ['4', '.', '6']
    >>> get_row([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']], (2, 0))
    ['.', '8', '9']
    """
    return grid[pos[0]]


def get_col(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    """
    параметры:
        grid: tp.List[tp.List[str]] - Двойной массив со строками - Судоку
        pos: tp.Tuple[int, int] - позиция (строка, столбец) элемента для котрого ищем столбец
    результат:
        tp.List[str] - массив строк. Все элементы в столбце с элементом на позиции pos

    Возвращает все значения для номера столбца, указанного в pos
    >>> get_col([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']], (0, 0))
    ['1', '4', '7']
    >>> get_col([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']], (0, 1))
    ['2', '.', '8']
    >>> get_col([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']], (0, 2))
    ['3', '6', '9']
    """
    to_find = []
    for i in range(len(grid)):
        to_find.append(grid[i][pos[1]])
    return to_find


def get_block(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    """
    параметры:
        grid: tp.List[tp.List[str]] - Двойной массив со строками - Судоку
        pos: tp.Tuple[int, int] - позиция (строка, столбец) элемента для котрого ищем квадрат
    результат:
        tp.List[str] - массив строк. Все элементы в квадрате с элементом на позиции pos

    Возвращает все значения из квадрата, в который попадает позиция pos
    >>> grid = read_sudoku('puzzle1.txt')
    >>> get_block(grid, (0, 1))
    ['5', '3', '.', '6', '.', '.', '.', '9', '8']
    >>> get_block(grid, (4, 7))
    ['.', '.', '3', '.', '.', '1', '.', '.', '6']
    >>> get_block(grid, (8, 8))
    ['2', '8', '.', '.', '.', '5', '.', '7', '9']
    """
    row, col = pos
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    return [grid[i][j] for i in range(start_row, start_row + 3) for j in range(start_col, start_col + 3)]


def find_empty_positions(grid: tp.List[tp.List[str]]) -> tp.Optional[tp.Tuple[int, int]]:
    """
    параметры:
        grid: tp.List[tp.List[str]] - Двойной массив со строками - Судоку
    результат:
        tp.Optional[tp.Tuple[int, int]] - кортэж со строкой и столбцом в котором находится пустая позиция Судоку

    Найти первую свободную позицию в пазле
    >>> find_empty_positions([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']])
    (0, 2)
    >>> find_empty_positions([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']])
    (1, 1)
    >>> find_empty_positions([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']])
    (2, 0)
    """
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '.':
                return (i, j)
    return None


def find_possible_values(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.Set[str]:
    """
    параметры:
        grid: tp.List[tp.List[str]] - Двойной массив со строками - Судоку
        pos: tp.Tuple[int, int] - индексы строки и столбца пропуска, для которого ищем все возможные значения
    результат:
        tp.Set[str] - множество, в котором все возможные варианты для пропущенной позиции, основанные на заполненных ячейках Судоку

    Вернуть множество возможных значения для указанной позиции
    >>> grid = read_sudoku('puzzle1.txt')
    >>> values = find_possible_values(grid, (0,2))
    >>> values == {'1', '2', '4'}
    True
    >>> values = find_possible_values(grid, (4,7))
    >>> values == {'2', '5', '9'}
    True
    """
    in_row = set(get_row(grid, pos))
    in_col = set(get_col(grid, pos))
    in_block = set(get_block(grid, pos))
    return set(str(i) for i in range(1, 10)) - in_block - in_col - in_row


def solve(grid: tp.List[tp.List[str]]) -> tp.Optional[tp.List[tp.List[str]]]:
    """
    параметры:
        grid: tp.List[tp.List[str]] - Двойной массив со строками - Судоку
    результат:
        tp.Optional[tp.List[tp.List[str]] - Двойной массив со строками - решенный Судоку

    Решение пазла, заданного в grid """
    """ Как решать Судоку?
        1. Найти свободную позицию
        2. Найти все возможные значения, которые могут находиться на этой позиции
        3. Для каждого возможного значения:
            3.1. Поместить это значение на эту позицию
            3.2. Продолжить решать оставшуюся часть пазла
    >>> grid = read_sudoku('puzzle1.txt')
    >>> solve(grid)
    [['5', '3', '4', '6', '7', '8', '9', '1', '2'], ['6', '7', '2', '1', '9', '5', '3', '4', '8'], ['1', '9', '8', '3', '4', '2', '5', '6', '7'], ['8', '5', '9', '7', '6', '1', '4', '2', '3'], ['4', '2', '6', '8', '5', '3', '7', '9', '1'], ['7', '1', '3', '9', '2', '4', '8', '5', '6'], ['9', '6', '1', '5', '3', '7', '2', '8', '4'], ['2', '8', '7', '4', '1', '9', '6', '3', '5'], ['3', '4', '5', '2', '8', '6', '1', '7', '9']]
    """
    empty_position = find_empty_positions(grid)
    if not empty_position:
        return grid
    else:
        row, col = empty_position
        values = find_possible_values(grid, empty_position)
        for element in values:
            grid[row][col] = element
            solution = solve(grid)
            if solution:
                return solution
            grid[row][col] = '.'
    return None


def check_solution(solution: tp.List[tp.List[str]]) -> bool:
    """
    параметры:
        solution: tp.List[tp.List[str]] - Двойной массив со строками - решенный Судоку
    результат:
        bool - True если решение правильное, False если решение не правильное

    Если решение solution верно, то вернуть True, в противном случае False """

    # TODO: Add doctests with bad puzzles
    for row in solution:
        if len(set(row)) != 9 or '.' in row:
            return False

    for col in range(9):
        col_values = [solution[row][col] for row in range(9)]
        if len(set(col_values)) != 9 or '.' in col_values:
            return False

    for block in range(0, 9, 3):
        block_values = [solution[row][col] for row in range(block, block+3) for col in range(block, block+3)]
        if len(set(block_values)) != 9 or '.' in block_values:
            return False
    return True


def generate_sudoku(N: int) -> tp.List[tp.List[str]]:
    """
    параметры:
        N: int - число характеризующее заполненность Судоку (Количество заполненных элементов)
    результат:
        tp.List[tp.List[str] - Двойной массив со строками - Судоку

    Генерация судоку заполненного на N элементов
    >>> grid = generate_sudoku(40)
    >>> sum(1 for row in grid for e in row if e == '.')
    41
    >>> solution = solve(grid)
    >>> check_solution(solution)
    True
    >>> grid = generate_sudoku(1000)
    >>> sum(1 for row in grid for e in row if e == '.')
    0
    >>> solution = solve(grid)
    >>> check_solution(solution)
    True
    >>> grid = generate_sudoku(0)
    >>> sum(1 for row in grid for e in row if e == '.')
    81
    >>> solution = solve(grid)
    >>> check_solution(solution)
    True
    """

    grid = [['.' for _ in range(9)] for _ in range(9)]
    solve(grid)

    position = [(i, j) for i in range(9) for j in range(9)]
    np.random.shuffle(position)

    for i, j in position[:len(grid) * len(grid[0]) - N]:
        grid[i][j] = '.'
    return grid

def run_solve(filename: str) -> None:
    grid = read_sudoku(filename)
    start = time.time()
    solve(grid)
    end = time.time()
    print(f"{filename}: {end-start}")

if __name__ == "__main__":
    for fname in ["puzzle1.txt", "puzzle2.txt", "puzzle3.txt"]:
        p = multiprocessing.Process(target=run_solve, args=(fname,))
        p.start()
