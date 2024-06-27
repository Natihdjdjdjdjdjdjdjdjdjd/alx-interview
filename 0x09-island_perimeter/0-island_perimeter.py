#!/usr/bin/python3
"""the finction that defines island perimeter finding function."""


def island_perimeter(grid):
    """Returns the perimeter of the island describe
    """
    # Determine the number of rows and columns in the grid
    my_rows = len(grid)
    my_cols = len(grid[0])

    # Initialize the perimeter variable to 0
    peri_meter = 0

    # Loop through each cell in the grid
    for i in range(my_rows):
        for j in range(my_cols):
            if grid[i][j] == 1:
                if i == 0 or grid[i-1][j] == 0:
                    peri_meter += 1
                if i == my_rows-1 or grid[i+1][j] == 0:
                    peri_meter += 1
                if j == 0 or grid[i][j-1] == 0:
                    peri_meter += 1
                if j == my_cols-1 or grid[i][j+1] == 0:
                    peri_meter += 1

    # Return the total perimeter
    return peri_meter
