# Constants to denote squares we've already processed.
UNMARKED_ISLAND_SQUARE=1
UNMARKED_EMPTY_SQUARE=0
MARKED_ISLAND_SQUARE='#'
MARKED_EMPTY_SQUARE='X'


def get_grid_square_count(grid):
    return sum([len(row) for row in grid])


def check_around(row, column, grid):
    """
    This method checks the squares to the left, right, above and below the current
    already marked island grid square to see if there are any other connecting island
    grid squares. If such are found they are returned as a list of row, column tuples.
    """

    connected_island_grid_squares = []

    # Left
    if column > 0 and grid[row][column - 1] == UNMARKED_ISLAND_SQUARE:
        connected_island_grid_squares.append((row, column - 1))

    # Right
    if column < (len(grid[row] - 1)) and grid[row][column + 1] == UNMARKED_ISLAND_SQUARE:
        connected_island_grid_squares.append((row, column + 1))

    # Above
    if row > 0 and grid[row - 1][column] == UNMARKED_ISLAND_SQUARE:
        connected_island_grid_squares.append((row - 1, column))

    # Below
    if row < (len(grid) - 1) and grid[row + 1][column] == UNMARKED_ISLAND_SQUARE:
        connected_island_grid_squares.append((row + 1, column))

    return connected_island_grid_squares


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
    islands = 0         # var. for the counts

    current_row = 0
    current_column = 0
    grid_squares_searched = 0

    grid_square_count = get_grid_square_count(grid)

    while grid_squares_searched <= grid_square_count:
        if grid[current_row][current_column] == UNMARKED_EMPTY_SQUARE:
            mark_empty(current_row, current_column, grid)
            grid_squares_searched += 1
        elif grid[current_row][current_column] == UNMARKED_ISLAND_SQUARE:
            mark_islands(current_row, current_column, grid)
            grid_squares_searched += 1
            islands += 1
            connected_grid_squares = check_around(current_row, current_column, grid)
            for connected_grid_square in connected_grid_squares:
                mark_islands(connected_grid_square[0], connected_grid_square[1], grid)
                grid_squares_searched += 1

        elif grid[current_row][current_column] == MARKED_ISLAND_SQUARE or grid[current_row][current_column] == MARKED_EMPTY_SQUARE:
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


