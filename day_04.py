from util import Test, Answer, ReadPuzzle, ReadExamplePuzzle


class Range(object):
    def __init__(self, str_repr):
        self.min, self.max = str_repr.split("-")
        self.min = int(self.min)
        self.max = int(self.max)

    def __contains__(self, item):
        if isinstance(item, self.__class__):
            return self.min <= item.min and self.max >= item.max
        elif isinstance(item, int):
            return self.min <= item <= self.max

    def overlap(self, other):
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
        if left.overlap(right):
            overlap += 1
    return overlap


def preprocess_data(data):
    """Do any additional parsing to the data to prep for answers"""
    return list((Range(left), Range(right)) for left, right in (d.split(",") for d in data))


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
