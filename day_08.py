from util import Test, Answer, ReadPuzzle, ReadExamplePuzzle


def part1(data):
    res = []
    rows = len(data)
    cols = len(data[0])
    for _ in range(rows):
        res.append([False] * cols)

    # down
    for c in range(cols):
        for r in range(rows - 1):
            if int(data[r][c]) < int(data[r + 1][c]):
                res[r][c] = True
    # up
    for c in range(cols):
        for r in range(rows - 1, 0, -1):
            if int(data[r][c]) < int(data[r - 1][c]):
                res[r][c] = True

    # left
    for r in range(rows):
        for c in range(cols - 1)

    return sum(sum(c for c in row) for row in res)


def part2(data):
    return None


def preprocess_data(data):
    """Do any additional parsing to the data to prep for answers"""
    return data


if __name__ == "__main__":
    # test answer on example data
    test_data, test_answer1 = ReadExamplePuzzle()
    test_data = preprocess_data(test_data)

    data = preprocess_data(ReadPuzzle())

    for v in test_data:
        print(v)

    if Test(1, part1(test_data), test_answer1):
        Answer(1, part1(data))

    if Test(2, part2(test_data), None):
        Answer(2, part2(data))
