from util import Test, Answer, ReadPuzzle, ReadExamplePuzzle, Point


def part1(data):
    h = Point(0,0)
    t = Point(0,0)
    trail = set((t,))
    for line in data:
        dir, count = line.split()
        if dir == 'R': step = Point(1,0)
        elif dir == 'L': step = Point(-1,0)
        elif dir == 'U': step = Point(0,1)
        elif dir == 'D': step = Point(0,-1)
        for i in range(int(count)):
            next_h = h + step
            if h != t and next_h != t:
                delta = next_h-t
                if delta.x == 0 or delta.y == 0:
                    t += step
                elif abs(delta.x) == 2 or abs(delta.y) == 2:
                    t=h
            trail.add(t)
            h = next_h
            print(h,t)
    return len(trail)


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
