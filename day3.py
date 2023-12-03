from collections import defaultdict

DATA = open('day3.txt').read()

grid = DATA.splitlines()
width, height = len(grid[0]), len(grid)


def neighbor_indices(row, start_col, end_col):
    for dr, dc in [(-1, -1), (0, -1), (1, -1)]:
        yield row + dr, start_col + dc
    for col in range(start_col, end_col + 1):
        yield row - 1, col
        yield row + 1, col
    for dr, dc in [(-1, 1), (0, 1), (1, 1)]:
        yield row + dr, end_col + dc


def neighbors(row, start_col, end_col):
    for row, col in neighbor_indices(row, start_col, end_col):
        if row < 0 or col < 0 or row >= height or col >= width:
            continue
        yield row, col


part1 = 0
gears = defaultdict(list)
for row in range(height):
    start_cols = (i for i in range(width)
                  if grid[row][i].isdigit() and (i == 0 or not grid[row][i - 1].isdigit()))
    for start_col in start_cols:
        end_col = next(i for i in range(start_col, width)
                       if i == width - 1 or not grid[row][i + 1].isdigit())
        part_number = int(grid[row][start_col:end_col+1])
        adjacent_symbol = False
        for r, c in neighbors(row, start_col, end_col):
            if not grid[r][c].isdigit() and grid[r][c] != '.':
                adjacent_symbol = True
            if grid[r][c] == '*':
                gears[(r, c)].append(part_number)
        if adjacent_symbol:
            part1 += part_number

print(part1)
assert (part1 == 532331)

part2 = sum(v[0]*v[1] for v in gears.values() if len(v) == 2)
print(part2)
assert (part2 == 82301120)
