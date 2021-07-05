from typing import NamedTuple, List

# Constants to denote squares we've already processed.
UNMARKED_ISLAND_SQUARE = 1
UNMARKED_EMPTY_SQUARE = 0
MARKED_ISLAND_SQUARE = '#'
MARKED_EMPTY_SQUARE = 'X'


class GridLocation(NamedTuple):
    row: int
    column: int

Grid = List[List]


def check_grid_square_above(grid_location: GridLocation, grid: Grid):
    """
    Return true if the grid square above grid_location is an island.

    Return False if it's not, or if we're at the grid border.
    """

    if not(grid_locaation.row - 1):
        return False

    return grid[grid_location.row - 1][grid_location.column] == UNMARKED_ISLAND_SQUARE


def check_grid_square_below(grid_location: GridLocation, grid: Grid):
    """
    Return true if the grid square below grid_location is an island.

    Return False if it's not, or if we're at the grid border.
    """
    if grid_location.row + 1 > get_grid_bottom(grid):
        return False

    return grid[grid_location.row + 1][grid_location.column] == UNMARKED_ISLAND_SQUARE


def check_grid_square_right(grid_location: GridLocation, grid: Grid):
    """
    Return true if the grid square to the right is an island.

    Return False if it's not, or if we're at the grid border.
    """
    if grid_location.column > len(grid[grid_location.row]):
        return False

    return grid_location.column + 1 == UNMARKED_ISLAND_SQUARE


def get_grid_bottom(grid: Grid):
    return len(grid) - 1


def mark_island_column(grid_location: GridLocation, grid: Grid):
    """
    This method marks heretofore unmarked island squares,
    traveling down the column as it goes, until it finds
    no more unmarked island grid squares to mark.
    """

    current_grid_location: GridLocation = grid_location

    mark_island_square(grid_location, grid)

    while check_grid_square_below(current_grid_location, grid):
        current_grid_location = GridLocation(current_grid_location.row + 1, current_grid_location.column)
        mark_island_square(current_grid_location, grid)


def mark_whole_island(grid_location: GridLocation, grid: Grid):
    """
    This function does a depth first search of the graph of as yet unmarked
    island grid squares connected to the initial island grid square passed
    the 'grid_location' parameter.
    """

    mark_island_column(grid_location, grid)
    current_grid_location: GridLocation = grid_location
    while check_grid_square_right(current_grid_location, grid):
        current_grid_location = GridLocation(current_grid_location.row, current_grid_location.column + 1)
        mark_island_column(current_grid_location, grid)


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

    for column_index in range(len(grid[row_index])):
        current_grid_location: GridLocation = GridLocation(row_index, column_index)
        if grid[row_index][column_index] == UNMARKED_EMPTY_SQUARE:
            mark_empty(current_grid_location, grid)
        elif grid[row_index][column_index] == UNMARKED_ISLAND_SQUARE:
            mark_island_square(current_grid_location)
            islands += 1

    return islands


def mark_empty(grid_location: GridLocation, grid: Grid):
    """
    Input: the row, column and grid
    Output: None. Just mark the visited islands as in-place operation.
    """

    grid[grid_location.row][grid_location.column] = MARKED_EMPTY_SQUARE


def mark_island_square(grid_location: GridLocation, grid: Grid):
    """
    Input: the row, column and grid
    Output: None. Just mark the visited islands as in-place operation.
    """

    grid[grid_location.row][grid_location.column] = MARKED_ISLAND_SQUARE
