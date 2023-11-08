import glob

class Robot:
    def __init__(self, map):
        self.map = map
        self.rows = len(map)
        self.cols = len(map[0])
        self.cleaned = set()
        self.directions = {'N': (-1, 0), 'S': (1, 0), 'W': (0, -1), 'E': (0, 1)}
        self.x, self.y = self.find_starting_point()

    def find_starting_point(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.map[i][j] != 'X':
                    return i, j

    def move(self, instruction):
        if instruction in self.directions:
            dx, dy = self.directions[instruction]
            new_x = (self.x + dx) % self.rows
            new_y = (self.y + dy) % self.cols
            if self.map[new_x][new_y] != 'X':
                self.x, self.y = new_x, new_y
                if self.map[new_x][new_y] == ' ':
                    self.cleaned.add((self.x, self.y))

    def count_uncleaned(self):
        uncleaned = sum(row.count(' ') for row in self.map) - len(self.cleaned)
        positions = [(i, j) for i in range(self.rows) for j in range(self.cols) if self.map[i][j] == ' ' and (i, j) not in self.cleaned]
        return uncleaned, positions


def process_file(input_path, output_path):
    with open(input_path, 'r') as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines[1:] if line.strip()]
        instructions = lines[0]
        map = lines[1:]

    robot = Robot(map)

    for instruction in instructions:
        robot.move(instruction)

    uncleaned, positions = robot.count_uncleaned()

    with open(output_path, 'w') as output_file:
        if uncleaned > 0:
            output_file.write(f"There are {uncleaned} spaces left uncleaned:\n")
            for position in positions:
                output_file.write(f"{position[0]} {position[1]}\n")
        else:
            output_file.write("GOOD PLAN\n")

def main():
    input_files = glob.glob('C:/Users/rider/Desktop/MsAI/Projects/AISys Examples/assignment-main/assignment-main/example-problems/problem_*.txt')
    for input_path in input_files:
        output_path = input_path.replace('example-problems', 'testing').replace('problem_', 'solution_')
        process_file(input_path, output_path)

if __name__ == '__main__':
    main()
