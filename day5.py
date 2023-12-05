from bisect import bisect
from collections import namedtuple
import re

DATA = open('day5.txt').read()

IntervalData = namedtuple('IntervalData', ['source', 'length', 'dest'])
Interval = namedtuple('Interval', ['source', 'dest'])


class Map:
    def __init__(self, map_intervals):
        map_intervals = sorted(map_intervals, key=lambda i: i.source)
        intervals = []

        intervals.append(Interval(float('-inf'), None))
        previous_end = map_intervals[0].source
        for interval in map_intervals:
            if interval.source > previous_end + 1:
                intervals.append(Interval(previous_end + 1, None))
            intervals.append(Interval(interval.source, interval.dest))
            previous_end = interval.source + interval.length - 1
        intervals.append(Interval(previous_end + 1, None))

        self._intervals = intervals
        self._sources = [i.source for i in intervals]

    def _value(self, i, n):
        if self._intervals[i].dest is None:
            return n
        return self._intervals[i].dest + (n - self._intervals[i].source)

    def convert(self, n):
        return self._value(bisect(self._sources, n) - 1, n)

    def convert_interval(self, start, end):
        initial = bisect(self._sources, start) - 1
        result = []
        current_start = start
        for i in range(initial, len(self._intervals)):
            if i == len(self._intervals) - 1:
                next_end = float('+inf')
            else: 
                next_end = self._intervals[i + 1].source
            if end < next_end:
                result.append(
                    (self._value(i, current_start), self._value(i, end)))
                break
            result.append((self._value(i, current_start),
                          self._value(i, next_end - 1)))
            current_start = next_end
        return result


def merge(intervals):
    intervals = sorted(intervals, key=lambda i: i[0])
    current_start, current_end = intervals[0]
    result = []
    for start, end in intervals[1:]:
        if start <= current_start:
            current_end = max(current_end, end)
        else:
            result.append((current_start, current_end))
            current_start, current_end = start, end
    result.append((current_start, current_end))
    return result


map_data = []
seeds = None
for line in DATA.splitlines():
    if line.startswith('seeds:'):
        seeds = list(map(int, re.findall(r'\d+', line)))
    elif line.endswith('map:'):
        map_data.append([])
    elif map_entry := re.match(r'(\d+)\s+(\d+)\s+(\d+)', line):
        map_data[-1].append(
            IntervalData(int(map_entry.group(2)), int(map_entry.group(3)), int(map_entry.group(1))))
maps = list(map(Map, map_data))


part1 = float('+inf')
for value in seeds:
    for m in maps:
        value = m.convert(value)
    part1 = min(part1, value)
print(part1)
assert (part1 == 525792406)


intervals = [(start, start + length - 1)
             for start, length in zip(seeds[:-1:2], seeds[1::2])]
for m in maps:
    intervals = merge(interval
                      for start, end in intervals
                      for interval in m.convert_interval(start, end))
part2 = min(i for i, _ in intervals)
print(part2)
assert (part2 == 79004094)
