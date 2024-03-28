import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """Класс для управления снарядами, выпущенными кораблём."""
    def __init__(self, ai_game):
        """Создаёт объект снарядов в текущей позиции корабля."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.image = pygame.image.load('images/bullet.bmp')  # Загрузка изображения снаряда
        self.image = pygame.transform.scale(
            self.image, (self.image.get_width() // 2, self.image.get_height() // 2))
        self.rectangle = self.image.get_rect()
        self.rectangle.midtop = ai_game.ship.rect.midtop

        # Позиция снаряда хранится в вещественном формате.
        self.y = float(self.rectangle.y)

    def update(self):
        """Перемещает снаряд вверх."""
        self.y -= self.settings.bullet_speed
        self.rectangle.y = self.y

    def draw_bullet(self):
        """Вывод снаряда на экран."""
        self.screen.blit(self.image, self.rectangle)
