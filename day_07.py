from util import Test, Answer, ReadPuzzle, ReadExamplePuzzle
from typing import Optional, List
from dataclasses import dataclass


@dataclass
class File:
    size: int
    name: str


class Folder:
    def __init__(self, name: str, parent: Optional['Folder'] = None):
        self.name = name
        self.parent = parent
        self.children: List['Folder'] = []
        self.files: List[File] = []

    def add_folder(self, name):
        child = Folder(name, self)
        self.children.append(child)
        return child

    @property
    def size(self):
        return sum(int(file.size) for file in self.files) + sum(child.size for child in self.children)

    def contents(self, depth=1):
        return '|   ' * (depth - 1) + self.name +"\n" + "\n".join(
            folder.contents(depth + 1) for folder in self.children) + "\n" + "\n".join(
            '|   ' * depth + file.name + ": " + file.size for file in self.files)

    def __repr__(self):
        return self.contents()


def part1(data):
    total = 0
    for folder in data:
        if folder.size < 100000:
            total += folder.size
    return total


def part2(data):
    available = 70000000 - data[0].size
    best = data[0]
    for folder in data:
        size = folder.size
        if size + available > 30000000 and size < best.size:
            best = folder

    return best.size


def preprocess_data(data):
    """Do any additional parsing to the data to prep for answers"""
    cwd: Optional[Folder] = None
    folders: List[Folder] = []
    for line in data:
        if line.startswith('$'):
            _, command, *args = line.split(' ')
            if command == 'cd':
                path = args[0]
                if path == '/':
                    cwd = Folder('/')
                    folders.append(cwd)
                elif path == '..':
                    if cwd.parent is not None:
                        cwd = cwd.parent
                else:
                    for child in cwd.children:
                        if child.name == path:
                            cwd = child
                            break
        else:
            info, name = line.split(' ')
            if info == 'dir':
                folders.append(cwd.add_folder(name))
            else:
                cwd.files.append(File(size=info, name=name))

    return folders


if __name__ == "__main__":
    # test answer on example data
    test_data, test_answer1 = ReadExamplePuzzle()
    test_data = preprocess_data(test_data)

    data = preprocess_data(ReadPuzzle())

    print(test_data[0])

    if Test(1, part1(test_data), test_answer1):
        Answer(1, part1(data))

    if Test(2, part2(test_data), 24933642):
        Answer(2, part2(data))
