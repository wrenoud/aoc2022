from util import Test, Answer, ReadPuzzle, ReadExamplePuzzle, Point
import math

def ceil(x):
    if x > 0:
        return int(math.ceil(x))
    else:
        return int(math.floor(x))

def show_map(trail):
    p_min = Point(0,0)
    p_max = Point(5,5)
    for p,_ in trail.items():
        if p.x < p_min.x: p_min.x = p.x
        elif p.x > p_max.x: p_max.x = p.x
        if p.y < p_min.y: p_min.y = p.y
        elif p.y > p_max.y: p_max.y = p.y
    print(">",p_min, p_max)
    for r in range(p_max.y, p_min.y-1, -1):
        row=str(r)
        for c in range(p_min.x, p_max.x+1):
            index = Point(c, r)
            if index in trail:
                row += trail[index]
            else:
                row += "."
        print(row)


class Knot (Point):
    def follow(self, other):
        if self != other:
            delta = other - self
            if abs(delta.x) == 2 or abs(delta.y) == 2:
                self.x += int(ceil(delta.x/2))
                self.y += int(ceil(delta.y/2))
            


def part1(data):
    s = Point(0,0)
    h = Knot(0,0)
    t = Knot(0,0)
    trail = set((Point(0,0),))
    for line in data:
        dir, count = line.split()
        if dir == 'R': step = Point(1,0)
        elif dir == 'L': step = Point(-1,0)
        elif dir == 'U': step = Point(0,1)
        elif dir == 'D': step = Point(0,-1)
        for i in range(int(count)):
            h += step
            t.follow(h)
            trail.add(t+s)
            #show_map({s:'s',t:'t',h:'h'})
    #show_map(dict(zip(list(trail),['#']*len(trail))))
    return len(trail)


def part2(data):
    s = Point(0,0)
    knots = [[Point(0,0),'h'],]
    for i in range(1,10):
        knots.append([Knot(0,0),str(i)])
    trail = set((Point(0,0),))
    for line in data:
        dir, count = line.split()
        if dir == 'R': step = Point(1,0)
        elif dir == 'L': step = Point(-1,0)
        elif dir == 'U': step = Point(0,1)
        elif dir == 'D': step = Point(0,-1)
        for i in range(int(count)):
            knots[0][0] += step
            next = step
            for i in range(1,10):
                knots[i][0].follow(knots[i-1][0])
            trail.add(knots[-1][0]+s)
            #show_map(dict(knots))
    #show_map(dict(zip(list(trail),['#']*len(trail))))
    return len(trail)


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
