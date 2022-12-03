from util import Test, Answer, ReadPuzzle, ReadExamplePuzzle


def part1(data):
    return None


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
