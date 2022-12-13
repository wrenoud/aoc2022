from util import Test, Answer, ReadPuzzle, ReadExamplePuzzle
from copy import deepcopy

class Movement(object):
	def __init__(self, line):
		_, self.count, _, self._from,_,self.to=line.split()
		self.count = int(self.count)
		self._from = int(self._from)-1
		self.to = int(self.to)-1
	def __repr__(self):
		return f"{self.count},{self._from},{self.to}"

class Stacks(object):
	def __init__(self, lines):
		self.stacks = []
		for line in lines[-2::-1]:
			for i,c in enumerate(line[1::4]):
				if len(self.stacks) <= i:
					self.stacks.append([])
				if c != " ":
					self.stacks[i].append(c)

	def move(self, m):
		for _ in range(m.count):
			if len(self.stacks[m._from]) > 0:
				self.stacks[m.to].append(self.stacks[m._from][-1])
				del self.stacks[m._from][-1]
	def move2(self, m):
		if len(self.stacks[m._from]) > 0:
			self.stacks[m.to]+=self.stacks[m._from][-m.count:]
			del self.stacks[m._from][-m.count:]
	def tops(self):
		return "".join(l[-1] for l in self.stacks)
	def __repr__(self):
		return "\n".join(" ".join(s) for s in self.stacks)


def part1(data):
    s = deepcopy(data[0])
    for m in data[1]:
    	s.move(m)
    return s.tops()


def part2(data):
    s = deepcopy(data[0])
    for m in data[1]:
    	s.move2(m)
    return s.tops()


def preprocess_data(data):
    """Do any additional parsing to the data to prep for answers"""
    stacklines = []
    movements = None
    for line in data:
    	if movements is None and line != "":
    		stacklines.append(line)
    	elif line == "":
    		movements = []
    	else:
    		movements.append(Movement(line))
    return (Stacks(stacklines), movements)


if __name__ == "__main__":
    # test answer on example data
    test_data, test_answer1 = ReadExamplePuzzle()
    test_data = preprocess_data(test_data)

    data = preprocess_data(ReadPuzzle())

    for v in test_data:
        print(v)

    if Test(1, part1(test_data), "CMZ"):
        Answer(1, part1(data))

    if Test(2, part2(test_data), "MCD"):
        Answer(2, part2(data))
