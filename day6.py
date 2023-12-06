from functools import reduce
import operator
import math
import re

DATA = open('day6.txt').read()


def num_win(time, distance):
    lo, hi = map(int, sorted([time / 2 + math.sqrt(time**2 / 4 - distance),
                              time / 2 - math.sqrt(time**2 / 4 - distance)]))
    lo = min(k for k in range(lo - 1, lo + 2) if (time - k) * k > distance)
    hi = max(k for k in range(hi - 1, hi + 2) if (time - k) * k > distance)
    return hi - lo + 1


times, distances = list(
    map(lambda s: map(int, re.findall(r'\d+', s)), DATA.splitlines()))
part1 = reduce(operator.mul,
               map(lambda x: num_win(*x), zip(times, distances)), 1)
print(part1)
assert (part1 == 220320)

time, distance = list(
    map(lambda s: int(''.join(re.findall(r'\d+', s))), DATA.splitlines()))
part2 = num_win(time, distance)
print(part2)
assert (part2 == 34454850)
