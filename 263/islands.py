from typing import NamedTuple, List

# Constants to denote squares we've already processed.
UNMARKED_ISLAND_SQUARE = 1
UNMARKED_EMPTY_SQUARE = 0
MARKED_ISLAND_SQUARE = '#'
MARKED_EMPTY_SQUARE = 'X'


class GridLocation(NamedTuple):
    row: int
    column: int


def list_connected_island_squares(grid_location: GridLocation, grid: List[GridLocation]):
    """
    This functions checks above, below, to the left and to the right of the supplied
    grid square for unmarked island squares, returning each as a tuple of row, column coordinates.
    grid_location -- named tuple with fields row, column.
    """

    above_index = grid_location.row - 1
    below_index = grid_location.row + 1
    left_index = grid_location.column - 1
    right_index = grid_location.column + 1
    grid_bottom = len(grid) - 1

    connected_island_squares: List[GridLocation] = []

    if (below_index < grid_bottom) and (grid[below_index][grid_location.column] == UNMARKED_ISLAND_SQUARE):
        connected_island_squares.append((GridLocation(below_index, grid_location.column)))

    if (above_index > 0) and (grid[above_index][grid_location.column] == UNMARKED_ISLAND_SQUARE):
        connected_island_squares.append((GridLocation(above_index, grid_location.column)))

    if left_index > 1 and (grid[grid_location.row][left_index] == UNMARKED_ISLAND_SQUARE):
        connected_island_squares.append((GridLocation(grid_location.row, left_index)))

    if right_index < len(grid[grid_location.row]) and grid[grid_location.row][right_index] == UNMARKED_ISLAND_SQUARE:
        connected_island_squares.append((GridLocation(grid_location.row, right_index)))

    return connected_island_squares


def count_islands(grid):
    """
    Input: 2D matrix, each item is [x, y] -> row, col.
    Output: number of islands, or 0 if found none.
    Notes: island is denoted by 1, ocean by 0 islands is counted by continuously
        connected vertically or horizontally  by '1's.
    It's also preferred to check/mark the visited islands:
    - eg. using the helper function - mark_islands().
    ----
    grid = [[1, 0, 0, 1],
            [1, 0, 1, 0],
            [0, 1, 0, 0],
            [1, 0, 0, 1]]
    """
    islands: int = 0  # var. for the counts

    for row_index in range(len(grid)):
        for column_index in range(len(grid[row_index])):
            if grid[row_index][column_index] == UNMARKED_EMPTY_SQUARE:
                mark_empty(row_index, column_index, grid)
            elif grid[row_index][column_index] == UNMARKED_ISLAND_SQUARE:
                mark_islands(row_index, column_index, grid)
                connected_island_squares = list_connected_island_squares(GridLocation(row_index, column_index), grid)
                while connected_island_squares:
                    found_connected_island_squares: List[GridLocation] = []
                    for connected_island_square in connected_island_squares:
                        mark_islands(connected_island_square.row, connected_island_square.column, grid)
                        found_connected_island_squares.extend(list_connected_island_squares(connected_island_square,
                                                                                            grid))

                    connected_island_squares = found_connected_island_squares

                # We've run out of connected island squares to process. So that's an island.
                islands += 1

            elif grid[row_index][column_index] == MARKED_ISLAND_SQUARE or \
                    grid[row_index][column_index] == MARKED_EMPTY_SQUARE:
                # The square has been marked and counted as searched already elsewhere.
                continue

    return islands


def mark_empty(row, column, grid):
    """
    Input: the row, column and grid
    Output: None. Just mark the visited islands as in-place operation.
    """
    grid[row][column] = 'X'  # one way to mark visited ones - suggestion.


def mark_islands(row, column, grid):
    """
    Input: the row, column and grid
    Output: None. Just mark the visited islands as in-place operation.
    """
    grid[row][column] = '#'  # one way to mark visited ones - suggestion.
