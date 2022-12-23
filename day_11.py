from util import Test, Answer, ReadPuzzle, ReadExamplePuzzle
from re import findall
from copy import copy


class Monkey:

    def __init__(self, name, items, operation, test, on_true, on_false):
        self.items = list(int(v) for v in items.split(", "))
        self.operation = operation
        self.test = int(test)
        self.on_true = int(on_true)
        self.on_false = int(on_false)
        self.inspections = 0

    def inspectall1(self, monkeys):
        self.inspections += len(self.items)
        for old in self.items:
            new = eval(self.operation, {'old': old})
            new = int(new / 3)
            if new % self.test == 0:
                monkeys[self.on_true].items.append(new)
            else:
                monkeys[self.on_false].items.append(new)
        self.items = []

    def inspectall2(self, monkeys):
        self.inspections += len(self.items)
        for old in self.items:
            new = eval(self.operation, {'old': old})
            if new % self.test == 0:
                monkeys[self.on_true].items.append(new)
            else:
                monkeys[self.on_false].items.append(new)
        self.items = []
    def __repr__(self):
        return str(self.items)


def part1(data):
    for i in range(20):
        for monkey in data:
            monkey.inspectall1(data)
    data.sort(key=lambda self: self.inspections, reverse=True)
    return data[0].inspections * data[1].inspections


def part2(data):
    for i in range(10000):
        for monkey in data:
            monkey.inspectall2(data)
    data.sort(key=lambda self: self.inspections, reverse=True)
    return data[0].inspections * data[1].inspections


def preprocess_data(data):
    """Do any additional parsing to the data to prep for answers"""
    matches = findall(
        r"Monkey (\d+):\s+Starting items: ([\d ,]+)\s+Operation: new = (.+?)\s+Test: divisible by (\d+)\s+If true: throw to monkey (\d+)\s+If false: throw to monkey (\d+)",
        "\n".join(data))
    return list(Monkey(*args) for args in matches)


if __name__ == "__main__":
    # test answer on example data
    test_data, test_answer1 = ReadExamplePuzzle()
    test_data = preprocess_data(test_data)

    data = preprocess_data(ReadPuzzle())

    for v in test_data:
        print(v)

    if Test(1, part1(copy(test_data)), test_answer1):
        Answer(1, part1(copy(data)))

    if Test(2, part2(copy(test_data)), 2713310158):
        Answer(2, part2(copy(data)))
