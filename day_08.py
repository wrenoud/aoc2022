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


def search_NS(forest: Forest, tree: Point, south: bool):
    rows, _ = forest.dims
    tree_height = forest[tree]
    count = 0
    step = 1 if south else -1
    r = tree.row + step
    if 0 > r >= rows:
        return 0
    while 0 <= r < rows:
        neighbor = forest[r, tree.col]
        r += step
        count += 1
        if neighbor >= tree_height:
            break
    return count


def search_WE(forest: Forest, tree: Point, east: bool):
    _, cols = forest.dims
    tree_height = forest[tree]
    count = 0
    step = 1 if east else -1
    c = tree.col + step
    if 0 > c >= cols:
        return 0
    while 0 <= c < cols:
        neighbor = forest[tree.row, c]
        c += step
        count += 1
        if neighbor >= tree_height:
            break
    return count


def scenic_score(forest: Forest, tree: Point):
    a = search_NS(forest, tree, True)
    b = search_NS(forest, tree, False)
    c = search_WE(forest, tree, True)
    d = search_WE(forest, tree, False)
    return a * b * c * d

def part2(data):
    rows, cols = data.dims
    best = 0

    for r in range(rows):
        for c in range(cols):
            tree = Point(r, c)
            score = scenic_score(data, tree)
            if score > best:
                best = score
    return best


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

    if Test(2, scenic_score(test_data, Point(3, 2)), 8):
        Answer(2, part2(data))
