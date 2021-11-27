from typing import List


class Map:
    def __init__(self, raw_map: List[list]):
        self.map = raw_map

    def next_generation(self):
        new_gen_map = [[] for _ in range(len(self.map))]
        for row in range(len(self.map)):
            for col in range(len(self.map[row])):
                is_alive = self.map[row][col]
                neighbors = sum(
                    [
                        self.get_cell(row - 1, col - 1),
                        self.get_cell(row - 1, col),
                        self.get_cell(row - 1, col + 1),
                        self.get_cell(row, col - 1),
                        self.get_cell(row, col + 1),
                        self.get_cell(row + 1, col - 1),
                        self.get_cell(row + 1, col),
                        self.get_cell(row + 1, col + 1),
                    ]
                )

                new_state = 0
                if is_alive:
                    if neighbors < 2:
                        new_state = 0
                    elif neighbors > 3:
                        new_state = 0
                    else:
                        new_state = 1
                else:
                    if neighbors == 3:
                        new_state = 1
                new_gen_map[row].append(new_state)
        self.map = new_gen_map

    def print(self):
        for row in self.map:
            for cell in row:
                print("\u25A0", end="  ") if cell else print("\u25A1", end="  ")
            print("\n")
        print("\n\n")

    def get_cell(self, row, col):
        if row < 0 or col < 0:
            return 0
        try:
            return self.map[row][col]
        except IndexError:
            return 0
