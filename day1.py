from collections import defaultdict

DATA = open('day1.txt').read()
NAMES = ['one', 'two', 'three', 'four',
         'five', 'six', 'seven', 'eight', 'nine']


class Node:
    def __init__(self):
        self.value = None
        self.childs = defaultdict(Node)

    def insert(self, s, value=None):
        node = self
        for c in s:
            node = node.childs[c]
        node.value = value if value else s

    def find(self, s):
        node = self
        for c in s:
            if c not in node.childs:
                return None
            node = node.childs[c]
            if node.value:
                return node.value
        return None


def run(part2=False):
    trie, trie_reversed = Node(), Node()
    for i in range(10):
        trie.insert(str(i + 1))
        trie_reversed.insert(str(i + 1))
    if part2:
        for i, name in enumerate(NAMES):
            trie.insert(name, str(i + 1))
            trie_reversed.insert(reversed(name), str(i + 1))

    result = 0
    for line in DATA.splitlines():
        first_digit = last_digit = None
        for i in range(len(line)):
            first_digit = trie.find(line[i:])
            if first_digit:
                break
        for i in reversed(range(len(line))):
            last_digit = trie_reversed.find(line[i::-1])
            if last_digit:
                break
        result += int(first_digit + last_digit)
    return result


result = run()
print(result)
assert (result == 55017)

result = run(True)
print(result)
assert (result == 53539)
