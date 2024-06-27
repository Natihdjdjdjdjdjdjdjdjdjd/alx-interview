#!/usr/bin/python3
"""the finction that defines island perimeter finding function."""


def island_perimeter(grid):
    """Return the perimiter of an island.
    """
    w = len(grid[0])
    h = len(grid)
    edges = 0
    size = 0

    for x in range(h):
        for y in range(w):
            if grid[x][y] == 1:
                size += 1
                if (y > 0 and grid[x][x - 1] == 1):
                    edges += 1
                if (x > 0 and grid[x - 1][y] == 1):
                    edges += 1
    return size * 4 - edges * 2
