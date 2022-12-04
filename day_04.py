from util import Test, Answer, ReadPuzzle, ReadExamplePuzzle


class Range(object):
    def __init__(self, minimum, maximum):
        self.min = minimum if isinstance(minimum, int) else int(minimum)
        self.max = maximum if isinstance(maximum, int) else int(maximum)

    def __contains__(self, item):
        if isinstance(item, self.__class__):
            return self.min <= item.min and self.max >= item.max
        elif isinstance(item, int):
            return self.min <= item <= self.max

    def overlaps(self, other):
        return other.min in self or \
               other.max in self or \
               self.min in other or \
               self.max in other

    def __repr__(self):
        return f"{self.min}-{self.max}"


def part1(data):
    inside = 0
    for left, right in data:
        if left in right or right in left:
            inside += 1
    return inside


def part2(data):
    overlap = 0
    for left, right in data:
        if left.overlaps(right):
            overlap += 1
    return overlap


def preprocess_data(data):
    """Do any additional parsing to the data to prep for answers"""
    pairs = (d.split(",") for d in data)
    return list((Range(*left.split("-")), Range(*right.split("-"))) for left, right in pairs)


if __name__ == "__main__":
    # test answer on example data
    test_data, test_answer1 = ReadExamplePuzzle()
    test_data = preprocess_data(test_data)

    data = preprocess_data(ReadPuzzle())

    for v in test_data:
        print(v)

    if Test(1, part1(test_data), test_answer1):
        Answer(1, part1(data))

    if Test(2, part2(test_data), 4):
        Answer(2, part2(data))
