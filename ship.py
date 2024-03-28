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
        self.rect = self.image.get_rect()

        # Каждый новый корабль появляется у нижнего края экрана.
        self.rect.midbottom = self.screen_rectangle.midbottom

        # Флаги перемещения по горизонтали
        self.moving_right = False
        self.moving_left = False

        self.x = float(self.rect.x)

    def update(self) -> None:
        """Обновляет позицию корабля с учётом флага."""
        if self.moving_right and self.rect.right < self.screen_rectangle.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Обновление атрибута rectangle на основании self.x
        self.rect.x = self.x

    def blit_me(self) -> None:
        """Рисует корабль в текущей позиции."""
        self.screen.blit(self.image, self.rect)

    def center_ship(self) -> None:
        """Размещает корабль в центре нижней стороны."""
        self.rect.midbottom = self.screen_rectangle.midbottom
        self.x = float(self.rect.x)
