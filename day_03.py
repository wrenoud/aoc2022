from util import Test, Answer, ReadPuzzle, ReadExamplePuzzle

def priority(c):
    v = ord(c)
    if v >= ord('a'):
        return v - ord('a') + 1
    else:
        return v - ord('A') + 27

def part1(data):
    total = 0
    for sack in data:
        print("-",sack)
        for c in sack[0]:
            if c in sack[1]:
                total += priority(c)
                break
    return total


def part2(data):
    total = 0
    for i in range(0, len(data), 3):
        for c in "".join(data[i]):
            if (c in data[i+1][0] or c in data[i+1][1]) and (c in data[i+2][0] or c in data[i+2][1]):
                total += priority(c)
                break
    return total


def preprocess_data(data):
    """Do any additional parsing to the data to prep for answers"""
    sacks = []
    for d in data:
        count = int(len(d) / 2)
        sacks.append([d[:count], d[count:]])
    return sacks


if __name__ == "__main__":
    # test answer on example data
    test_data, _ = ReadExamplePuzzle()
    test_data = preprocess_data(test_data)

    data = preprocess_data(ReadPuzzle())

    for v in test_data:
        print(v)

    if Test(1, part1(test_data), 157):
        Answer(1, part1(data))

    if Test(2, part2(test_data), 70):
        Answer(2, part2(data))
