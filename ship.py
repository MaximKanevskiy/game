import pygame


class Ship:
    def __init__(self, ai_game):
        """Инициализирует корабль и задаёт его начальную позицию."""
        self.screen = ai_game.screen
        self.screen_rectangle = ai_game.screen.get_rect()
        # Загружает изображение корабля и получает прямоугольник.

        self.image = pygame.image.load('images/ship.bmp')
        self.image = pygame.transform.scale(
            self.image, (self.image.get_width() // 3, self.image.get_height() // 3))
        self.rectangle = self.image.get_rect()

        # Каждый новый корабль появляется у нижнего края экрана.
        self.rectangle.midbottom = self.screen_rectangle.midbottom

    def blit_me(self):
        """Рисует корабль в текущей позиции."""
        self.screen.blit(self.image, self.rectangle)
