from util import Test, Answer, ReadPuzzle, ReadExamplePuzzle


def make_elves(data):
		elves = [[]]
		for calories in data:
			if calories == '':
				elves.append([])
			else:
				elves[-1].append(int(calories))
		return list(sum(v) for v in elves)

def part1(data):
		return max(make_elves(data))


def part2(data):
		return sum(sorted(make_elves(data))[-3:])


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

    if Test(1, part1(test_data), 24000):
        Answer(1, part1(data))

    if Test(2, part2(test_data), 45000):
        Answer(2, part2(data))
