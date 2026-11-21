#!/usr/bin/python3

def island_perimeter(grid):
    if not grid or not grid[0]:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                perimeter += 4

                # Check top neighbor for a shared edge
                if r > 0 and grid[r - 1][c] == 1:
                    perimeter -= 2

                # Check left neighbor for a shared edge
                if c > 0 and grid[r][c - 1] == 1:
                    perimeter -= 2

    return perimeter
