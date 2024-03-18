import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """Класс для управления снарядами, выпущенными кораблём."""
    def __init__(self, ai_game):
        """Создаёт объект снарядов в текущей позиции корабля."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rectangle = ai_game.screen.get_rect()

        # Создание снаряда в позиции (0,0) и назначение правильной позиции.
        self.image = pygame.image.load('images/bullet.bmp')
        self.rectangle = self.image.get_rect()
        self.rectangle.midtop = ai_game.ship.rectangle.midtop

        # Позиция снаряда хранится в вещественном формате.
        self.y = float(self.rectangle.y)
