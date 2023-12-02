import re

DATA = open('day2.txt').read()
CONSTRAINTS = {'red': 12, 'green': 13, 'blue': 14}

part1 = part2 = 0
for line in DATA.splitlines():
    game_id, content = re.match(r'Game (\d+):(.*)', line).groups()
    valid = True
    power = 1
    for color, max_color in CONSTRAINTS.items():
        num_color = max(map(int, re.findall(rf' (\d+) {color}', content)))
        if num_color > max_color:
            valid = False
        power *= num_color
    if valid:
        part1 += int(game_id)
    part2 += power

print(part1)
assert (part1 == 2149)

print(part2)
assert (part2 == 71274)
