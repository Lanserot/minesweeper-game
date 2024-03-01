import math
from Storage import Storage


class Renderer:
    WHITE_COLOR = (255, 255, 255)
    LITE_GREY_COLOR = (200, 200, 200)
    GREY_COLOR = (150, 150, 150)
    BLACK_COLOR = (0, 0, 0)
    RED_COLOR = (255, 0, 0)

    def render(self) -> None:

        self.draw_field()
        self.draw_mouse_pos()
        self.draw_flags_blocks()
        self.draw_open_blocks()

        if self.storage.get_memory_class().lose:
            self.draw_lose_text()

    def draw_lose_text(self):
        text_color = self.RED_COLOR
        font = self.pygame.font.Font(None, 56)
        text = font.render("ПРОИГРАЛ", True, text_color)
        text_rect = text.get_rect()
        text_rect.topleft = (200, 200)
        self.screen.blit(text, text_rect)

    def draw_flags_blocks(self) -> None:
        for k, v in self.storage.get_memory_class().flags.items():
            for j in v:
                self.pygame.draw.rect(self.screen, self.RED_COLOR,
                                      (int(k) * self.get_block_size_memory(),
                                       int(j) * self.get_block_size_memory(),
                                       self.get_block_size_memory(),
                                       self.get_block_size_memory()))

    def get_block_size_memory(self) -> int:
        return self.storage.get_memory_class().BLOCK_SIZE

    def draw_mouse_pos(self) -> None:
        x, y = self.pygame.mouse.get_pos()
        x = math.floor(x / self.get_block_size_memory())
        y = math.floor(y / self.get_block_size_memory())

        if x < len(self.storage.get_memory_class().field[0]):
            self.draw_rect(self.GREY_COLOR, x * self.get_block_size_memory(),
                           y * self.get_block_size_memory(),
                           self.get_block_size_memory(),
                           self.get_block_size_memory())

    def draw_open_blocks(self) -> None:
        text_color = self.BLACK_COLOR
        font = self.pygame.font.Font(None, 24)

        for k, v in self.storage.get_memory_class().opens.items():
            for j in v:
                if self.storage.get_memory_class().field[k][j]:
                    continue

                self.draw_rect(self.WHITE_COLOR, k * self.get_block_size_memory(),
                               j * self.get_block_size_memory(),
                               self.get_block_size_memory(), self.get_block_size_memory())

                text = font.render(str(self.storage.get_memory_class().mines[k][j]), True, text_color)
                text_rect = text.get_rect()
                text_rect.topleft = (k * 20, j * 20)
                self.screen.blit(text, text_rect)

    def draw_rect(self, color, x, y, h, w) -> None:
        self.pygame.draw.rect(self.screen, color, (x, y, h, w))

    def draw_field(self) -> None:
        for index, i in enumerate(self.storage.get_memory_class().field):
            for index2, j in enumerate(i):
                x = index * self.get_block_size_memory()
                y = index2 * self.get_block_size_memory()

                self.draw_rect(self.LITE_GREY_COLOR, x, y, self.get_block_size_memory(), self.get_block_size_memory())
                self.draw_rect(self.GREY_COLOR, x, y, self.get_block_size_memory() - 2, self.get_block_size_memory() - 2)

                if self.storage.get_memory_class().field[index][index2] == 1 and self.storage.get_memory_class().lose:
                    self.draw_rect(self.BLACK_COLOR, x, y, self.get_block_size_memory(), self.get_block_size_memory())

    def __init__(self, storage: Storage, pygame, screen):
        self.storage = storage
        self.pygame = pygame
        self.screen = screen
