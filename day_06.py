from util import Test, Answer, ReadPuzzle, ReadExamplePuzzle


def find(data, count):
    for i in range(len(data)-count):
    	unique = True
    	for j in range(count-1):
    		unique &= data[i+j] not in data[i+j+1:i+count]
    	if unique:
    		return i + count
    return None

def part1(data):
    return find(data, 4)

def part2(data):
    return find(data, 14)


def preprocess_data(data):
    """Do any additional parsing to the data to prep for answers"""
    return data[0]


if __name__ == "__main__":
    # test answer on example data
    test_data, test_answer1 = ReadExamplePuzzle()
    test_data = preprocess_data(test_data)

    data = preprocess_data(ReadPuzzle())

    for v in test_data:
        print(v)

    if Test(1, part1(test_data), test_answer1):
        Answer(1, part1(data))

    if Test(2, part2(test_data), 19):
        Answer(2, part2(data))
