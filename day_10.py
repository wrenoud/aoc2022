from util import Test, Answer, ReadPuzzle, ReadExamplePuzzle


class Machine:
    def __init__(self, commands):
        self.commands = commands
        self.cycle = 0
        self.register = 1
        self.command_index = -1
        self.remaining_command_cycles = 0

    def reset(self):
        self.cycle = 0
        self.register = 1
        self.command_index = -1
        self.remaining_command_cycles = 0

    def advance(self):
        assert not self.eop
        if self.remaining_command_cycles == 0:
            command, *args = self.commands[self.command_index].split(' ')
            if command == 'addx':
                self.register += int(args[0])

        self.cycle += 1
        if self.remaining_command_cycles == 0:
            self.command_index += 1
            command, *args = self.commands[self.command_index].split(' ')
            if command == 'addx':
                self.remaining_command_cycles = 2
            else:
                self.remaining_command_cycles = 1
        self.remaining_command_cycles -= 1

    @property
    def signal_strength(self):
        return self.register * self.cycle

    @property
    def eop(self):
        return self.command_index == len(self.commands) - 1 and self.remaining_command_cycles == 0


def part1(data):
    total = 0
    for _ in range(20):
        data.advance()
    total += data.signal_strength
    for _ in range(40):
        data.advance()
    total += data.signal_strength
    for _ in range(40):
        data.advance()
    total += data.signal_strength
    for _ in range(40):
        data.advance()
    total += data.signal_strength
    for _ in range(40):
        data.advance()
    total += data.signal_strength
    for _ in range(40):
        data.advance()
    total += data.signal_strength
    return total


def part2(data):
    data.reset()

    crt = []
    while not data.eop:
        data.advance()
        if (data.cycle % 40) - 1 <= data.register + 1 <= (data.cycle % 40) + 1:
            crt.append('#')
        else:
            crt.append('.')

    for i in range(0, 240, 40):
        print("".join(crt[i:i+40]))

    return None


def preprocess_data(data):
    """Do any additional parsing to the data to prep for answers"""
    return Machine(data)


if __name__ == "__main__":
    # test answer on example data
    test_data, test_answer1 = ReadExamplePuzzle()
    test_data = preprocess_data(test_data)

    data = preprocess_data(ReadPuzzle())

    if Test(1, part1(test_data), 13140):
        Answer(1, part1(data))

    #if Test(2, part2(test_data), None):
    Answer(2, part2(data))
