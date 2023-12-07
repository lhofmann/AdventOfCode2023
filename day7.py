from collections import defaultdict
from functools import cmp_to_key

DATA = open('day7.txt').read()
CARDS = list(reversed('AKQJT9876543210'))
CARDS_JOKER = list(reversed('AKQT987654321J'))
JOKER = 0
type_cache_joker = {}


def hand_type(h):
    counts = defaultdict(int)
    for c in h:
        counts[c] += 1
    counts = sorted(list(counts.values()))
    if len(counts) == 1:
        return 7
    if len(counts) == 2:
        return 6 if counts[0] == 1 else 5
    if len(counts) == 3:
        return 4 if counts[1] == 1 else 3
    if len(counts) == 4:
        return 2
    return 1


def hand_type_joker(h):
    cache_key = tuple(sorted(h))
    if cache_key in type_cache_joker:
        return type_cache_joker[cache_key]

    if JOKER not in h:
        return hand_type(h)

    choices = set(c for c in h if c != JOKER)
    if not choices:
        return hand_type('AAAAA')

    best_type = 1
    i = h.index(JOKER)
    for choice in choices:
        h_next = list(h)
        h_next[i] = choice
        best_type = max(best_type, hand_type_joker(tuple(h_next)))

    type_cache_joker[cache_key] = best_type
    return best_type


def cmp(a, b, get_type):
    if a == b:
        return 0
    return -1 if (get_type(a),) + a < (get_type(b),) + b else 1


def solve(enable_joker=False):
    card_to_value = CARDS_JOKER if enable_joker else CARDS
    hands = [(tuple(map(lambda c: card_to_value.index(c), hand)), int(value))
             for hand, value in map(str.split, DATA.splitlines())]

    get_type = hand_type_joker if enable_joker else hand_type
    def compare(a, b): return cmp(a, b, get_type)
    hands.sort(key=lambda x: cmp_to_key(compare)(x[0]))

    return sum((i + 1) * h for i, (_, h) in enumerate(hands))


print(part1 := solve())
assert (part1 == 253603890)

print(part1 := solve(enable_joker=True))
assert (part1 == 253630098)
