import pygame


class Ship:
    def __init__(self, ai_game):
        """Инициализирует корабль и задаёт его начальную позицию."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rectangle = ai_game.screen.get_rect()
        # Загружает изображение корабля и получает прямоугольник.

        self.image = pygame.image.load('images/ship.bmp')
        self.image = pygame.transform.scale(
            self.image, (self.image.get_width() // 3, self.image.get_height() // 3))
        self.rectangle = self.image.get_rect()

        # Каждый новый корабль появляется у нижнего края экрана.
        self.rectangle.midbottom = self.screen_rectangle.midbottom

        # Флаги перемещения по горизонтали
        self.moving_right = False
        self.moving_left = False

        self.x = float(self.rectangle.x)

    def update(self) -> None:
        """Обновляет позицию корабля с учётом флага."""
        if self.moving_right and self.rectangle.right < self.screen_rectangle.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rectangle.left > 0:
            self.x -= self.settings.ship_speed

        # Обновление атрибута rectangle на основании self.x
        self.rectangle.x = self.x

    def blit_me(self) -> None:
        """Рисует корабль в текущей позиции."""
        self.screen.blit(self.image, self.rectangle)
