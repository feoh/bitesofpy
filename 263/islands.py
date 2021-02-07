# Constants to denote squares we've already processed.
UNMARKED_ISLAND_SQUARE = 1
UNMARKED_EMPTY_SQUARE = 0
MARKED_ISLAND_SQUARE = '#'
MARKED_EMPTY_SQUARE = 'X'


def get_grid_square_count(grid):
    return sum([len(row) for row in grid])


def check_same_island(row_index, column_index, grid):
    """
    This method returns True if a grid square above, below, left or right
    from the one we were passed is a marked island grid square.
    """
    above_index = row_index - 1
    below_index = row_index + 1
    left_index = column_index - 1
    right_index = column_index + 1

    if (below_index < (len(grid) - 1)) and (grid[below_index][column_index] == UNMARKED_ISLAND_SQUARE):
        return True

    if (above_index > 0) and (grid[above_index][column_index] == UNMARKED_ISLAND_SQUARE):
        return True

    if left_index > 1 and (grid[row_index][left_index] == UNMARKED_ISLAND_SQUARE):
        return True

    if right_index < len(grid[row_index]) and grid[row_index][right_index] == UNMARKED_ISLAND_SQUARE:
        return True

    return False


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
    islands = 0  # var. for the counts

    for row_index in range(len(grid)):
        for column_index in range(len(grid[row_index])):
            if grid[row_index][column_index] == UNMARKED_EMPTY_SQUARE:
                mark_empty(row_index, column_index, grid)
            elif grid[row_index][column_index] == UNMARKED_ISLAND_SQUARE:
                mark_islands(row_index, column_index, grid)
                if not check_same_island(row_index, column_index, grid):
                    islands += 1

            elif grid[row_index][column_index] == MARKED_ISLAND_SQUARE or grid[row_index][
                column_index] == MARKED_EMPTY_SQUARE:
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
