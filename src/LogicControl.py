import sys
from Storage import Storage
import math


class LogicControl:
    def __init__(self, storage: Storage):
        self.storage = storage

    def handle_key(self, pygame) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:

                x, y = pygame.mouse.get_pos()
                x = math.floor(x / self.storage.get_memory_class().BLOCK_SIZE)
                y = math.floor(y / self.storage.get_memory_class().BLOCK_SIZE)

                if event.button == pygame.BUTTON_RIGHT:
                    self.mouse_btn_right(x, y)

                if event.button == pygame.BUTTON_LEFT:
                    try:
                        self.mouse_btn_left(x, y)
                    except:
                        return

    def mouse_btn_right(self, x: int, y: int) -> None:
        if x >= len(self.storage.get_memory_class().field[0]):
            return
        if not x in self.storage.get_memory_class().flags:
            self.storage.get_memory_class().flags[x] = []
        if not y in self.storage.get_memory_class().flags[x]:
            self.storage.get_memory_class().flags[x].append(y)
        else:
            self.storage.get_memory_class().flags[x].remove(y)

    def mouse_btn_left(self, x: int, y: int) -> None:
        if self.storage.get_memory_class().field[x][y] == 1:
            self.storage.get_memory_class().lose = True
            return
        if not x in self.storage.get_memory_class().opens:
            self.storage.get_memory_class().opens[x] = []
        if not y in self.storage.get_memory_class().opens[x]:
            self.storage.get_memory_class().opens[x].append(y)
        if self.storage.get_memory_class().mines[x][y] == 0:
            self.storage.getGameLogicClass().bfs_mines((x, y))
