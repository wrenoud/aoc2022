from util import Test, Answer, ReadPuzzle, ReadExamplePuzzle


def points(l, r):
    pl = 0
    pr = 0
    if l == 'A':
        pl = 1
    elif l == 'B':
        pl = 2
    else:
        pl = 3

    if r == 'X':
        pr = 1
    elif r == 'Y':
        pr = 2
    else:
        pr = 3

    if pl == pr:
        pl += 3
        pr += 3
    elif (pl == 1 and pr == 3) \
            or (pl == 2 and pr == 1) \
            or (pl == 3 and pr == 2):
        pl += 6
    else:
        pr += 6

    return pl, pr


def part1(data):
    return sum(points(*g)[1] for g in data)


def points_b(l, r):
    pl = 0
    pr = 0
    if l == 'A':
        pl = 1
    elif l == 'B':
        pl = 2
    else:
        pl = 3

    if r == 'X':
        if pl == 1:
            return 3
        elif pl == 2:
            return 1
        else:
            return 2
    elif r == 'Y':
        return pl + 3
    else:
        if pl == 1:
            return 2 + 6
        elif pl == 2:
            return 3 + 6
        else:
            return 1 + 6

    return pr


def part2(data):
    return sum(points_b(*g) for g in data)


def preprocess_data(data):
    """Do any additional parsing to the data to prep for answers"""
    return list(v.split() for v in data)


if __name__ == "__main__":
    # test answer on example data
    test_data, test_answer1 = ReadExamplePuzzle()
    test_data = preprocess_data(test_data)

    data = preprocess_data(ReadPuzzle())

    for v in test_data:
        print(v)

    if Test(1, part1(test_data), test_answer1):
        Answer(1, part1(data))

    if Test(2, part2(test_data), 12):
        Answer(2, part2(data))
