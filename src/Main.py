from LogicControl import LogicControl
import pygame
from Storage import Storage
from Renderer import Renderer
from Memory import Memory
from GameLogic import GameLogic


class Main:

    def start(self):
        while True:
            self.storage.get_logic_class().handle_key(self.pygame)
            self.storage.get_renderer_class().render()
            pygame.display.flip()

    def __init__(self):
        pygame.init()
        self.storage = Storage()
        self.storage.memoryClass = Memory()
        self.storage.gameLogicClass = GameLogic(self.storage)
        self.pygame = pygame
        self.screen = self.pygame.display.set_mode((self.storage.get_memory_class().WIN_W_F,
                                                    self.storage.get_memory_class().WIN_H_F))
        self.storage.logicClass = LogicControl(self.storage)
        self.storage.rendererClass = Renderer(self.storage, self.pygame, self.screen)

        self.storage.gameLogicClass.init_lvl()
        self.start()


if __name__ == "__main__":
    main_instance = Main()
