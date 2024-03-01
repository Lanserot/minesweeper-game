from Storage import Storage
import random


class GameLogic:
    def __init__(self, storage: Storage):
        self.storage = storage

    def bfs_mines(self, start: ()) -> None:
        queue = [start]
        visited = set()
        while queue:
            current = queue.pop(0)
            visited.add(current)
            if not self.storage.get_memory_class().mines[current[0]][current[1]] == 0:
                continue
            for neighbor in self.get_neighbors(current):
                if neighbor not in visited and neighbor not in queue:
                    queue.append(neighbor)
        return

    def get_neighbors(self, current: []) -> []:
        neighbors = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                neighbor = (current[0] + i, current[1] + j)
                if 0 <= neighbor[0] < len(self.storage.get_memory_class().field) and 0 <= neighbor[1] < len(
                        self.storage.get_memory_class().field[0]):
                    if not current[0] + i in self.storage.get_memory_class().opens:
                        self.storage.get_memory_class().opens[current[0] + i] = []
                    if not current[1] + j in self.storage.get_memory_class().opens[current[0] + i]:
                        self.storage.get_memory_class().opens[current[0] + i].append(current[1] + j)

                    neighbors.append(neighbor)
        return neighbors

    def get_clear_field(self) -> []:
        array = []

        for i in range(int(self.storage.get_memory_class().WIN_W / self.storage.get_memory_class().BLOCK_SIZE)):
            sub_array = []
            for j in range(int(self.storage.get_memory_class().WIN_H / self.storage.get_memory_class().BLOCK_SIZE)):
                sub_array.append(0)
            array.append(sub_array)
        return array

    def create_field_and_mines(self) -> None:
        self.storage.get_memory_class().field = self.get_clear_field()
        self.storage.get_memory_class().mines = self.get_clear_field()

    def set_mines(self) -> None:
        for index, i in enumerate(self.storage.get_memory_class().field):
            for index2, j in enumerate(i):
                if random.randint(0, 5) == 0:
                    self.storage.get_memory_class().field[index][index2] = 1

    def to_count_mines(self) -> None:
        field = self.storage.get_memory_class().field

        for index, row in enumerate(field):
            for index2, cow in enumerate(row):

                if field[index][index2] == 1:
                    continue

                in2more0: bool = index2 - 1 >= 0
                in1more0: bool = index - 1 >= 0
                in1LessLen: bool = index + 1 < len(field)

                count: int = 0

                if in1LessLen and field[index + 1][index2]:
                    count += 1

                if in1LessLen and index2 + 1 < len(field[index + 1]) and field[index + 1][index2 + 1]:
                    count += 1

                if index2 + 1 < len(field[index]) and field[index][index2 + 1]:
                    count += 1

                if in1more0 and field[index - 1][index2]:
                    count += 1

                if in1more0 and in2more0 and field[index - 1][index2 - 1]:
                    count += 1

                if index - 2 >= 0 and field[index][index2 - 1]:
                    count += 1

                if in1LessLen and in2more0 and field[index + 1][index2 - 1]:
                    count += 1

                if in1more0 and index2 + 1 < len(field[index - 1]) and field[index - 1][index2 + 1]:
                    count += 1

                self.storage.get_memory_class().mines[index][index2] = count

    def init_lvl(self) -> None:
        self.create_field_and_mines()
        self.set_mines()
        self.to_count_mines()
