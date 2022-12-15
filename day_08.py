from typing import List
from util import Test, Answer, ReadPuzzle, ReadExamplePuzzle, Point


class Forest:
    def __init__(self, data: List[str]):
        self.trees = []
        for line in data:
            self.trees.append(list(int(c) for c in line))

    def __getitem__(self, item):
        if isinstance(item, tuple):
            return self.trees[item[0]][item[1]]
        if isinstance(item, Point):
            return self.trees[item.row][item.col]

    @property
    def dims(self):
        return len(self.trees), len(self.trees[0])


def part1(data):
    res = []
    rows, cols = data.dims
    for _ in range(rows):
        res.append([False] * cols)

    def inspect_ns(south: bool):
        for c in range(cols):
            max_h = -1
            for r in (range(rows - 1) if south else range(rows - 1, 0, -1)):
                h = int(data[r, c])
                if h > max_h:
                    res[r][c] = True
                max_h = max(h, max_h)

    inspect_ns(True)
    inspect_ns(False)

    def inspect_we(east: bool):
        for r in range(rows):
            max_h = -1
            for c in (range(cols - 1) if east else range(cols - 1, 0, -1)):
                h = int(data[r, c])
                if h > max_h:
                    res[r][c] = True
                max_h = max(h, max_h)

    inspect_we(True)
    inspect_we(False)

    for row in res:
        print("".join(('.' if v else '#') for v in row))

    return sum(sum(c for c in row) for row in res)


def part2(data):
    return None


def preprocess_data(data):
    """Do any additional parsing to the data to prep for answers"""
    return Forest(data)


if __name__ == "__main__":
    # test answer on example data
    test_data, test_answer1 = ReadExamplePuzzle()
    test_data = preprocess_data(test_data)

    data = preprocess_data(ReadPuzzle())

    if Test(1, part1(test_data), test_answer1):
        Answer(1, part1(data))

    if Test(2, part2(test_data), 8):
        Answer(2, part2(data))
