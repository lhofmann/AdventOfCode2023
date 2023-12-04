import re

DATA = open('day4.txt').read()

cards = DATA.splitlines()
counts = [1] * len(cards)
part1 = 0
for line in cards:
    card_id, winning, numbers = re.match(
        r'Card\s+(\d+):(.*)\|(.*)', line).groups()
    card_id = int(card_id) - 1
    winners = set(map(int, re.findall(r'\d+', winning)))
    numbers = set(map(int, re.findall(r'\d+', numbers)))
    num_won = len(winners & numbers)
    if num_won > 0:
        part1 += 2**(num_won - 1)
    for i in range(card_id + 1, min(card_id + 1 + num_won, len(counts))):
        counts[i] += counts[card_id]

print(part1)
assert (part1 == 22674)

part2 = sum(counts)
print(part2)
assert (part2 == 5747443)
