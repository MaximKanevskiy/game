import sys
import pygame
import time

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien


class AlienInvasion:
    """Класс для управления ресурсами и поведением игры."""
    def __init__(self):
        """Инициализирует игру и создает игровые ресурсы."""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)

        self.bullets = pygame.sprite.Group()
        self.bullet_charge = 0
        self.is_charging = False
        self.is_bullet_alive = False
        self.start_charge_time = 0
        self.charge_time = 0

        self.aliens = pygame.sprite.Group()

        self._create_fleet()

    def run_game(self) -> None:
        """Запуск основного цикла игры."""
        while True:
            self._check_events()
            self.ship.update()
            self.bullets.update()
            self._update_bullets()
            self._update_aliens()
            self._check_aliens_on_screen()
            self._update_screen()

    def _check_events(self) -> None:
        """Обрабатывает нажатия клавиш и события мыши."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event) -> None:
        """Реагирует на нажатие клавиш."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE and not self.is_bullet_alive:
            self.is_charging = True
            self.start_charge_time = time.time()
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event) -> None:
        """Реагирует на отпускание клавиш."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_SPACE and not self.is_bullet_alive:
            self.is_charging = False
            self.charge_time = time.time() - self.start_charge_time
            self._fire_bullet()

    def _fire_bullet(self):
        """Создание нового снаряда и включение его в группу bullets."""
        self._calculate_charges()

        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.is_bullet_alive = True
            self.bullets.add(new_bullet)

    def _calculate_charges(self):
        """Определение зарядов пули."""
        if self.charge_time < 2:
            self.bullet_charge = 1
        else:
            self.bullet_charge = 2

        # Обновление счётчика времени, когда пуля накапливала заряд
        self.charge_time = 0

    def _update_bullets(self):
        """Обновляет позиции снарядов и уничтожает старые снаряды."""
        # Обновление позиций снарядов.
        self.bullets.update()

        # Удаление снарядов, вышедших за край экрана.
        for bullet in self.bullets.copy():
            if not self.bullet_charge or bullet.rectangle.bottom <= 0:
                self.bullets.remove(bullet)
                self.is_bullet_alive = False

            # Проверка попаданий в пришельцев.
            # При обнаружении попадания удалить снаряд и пришельца.
            for alien in self.aliens.sprites():
                if bullet.rectangle.colliderect(alien.rect):
                    self.bullet_charge -= 1
                    self.aliens.remove(alien)
                    break

    def _create_fleet(self) -> None:
        """Создание флота вторжения."""
        # Создание пришельца и вычисление количества пришельцев в ряду
        # Интервал между соседними пришельцами равен ширине пришельца.
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        """Определяет количество рядов, помещающихся на экране."""
        ship_height = self.ship.rectangle.height
        available_space_y = (self.settings.screen_height - (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)

        # Создание флота вторжения.
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _check_fleet_edges(self) -> None:
        """Реагирует на достижение пришельцем края экрана."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self) -> None:
        """Опускает весь флот и меняет направление флота."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _create_alien(self, alien_number: int, row_number: int) -> None:
        """Создание пришельца и размещение его в ряду."""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x

        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _update_aliens(self) -> None:
        """Обновляет позиции всех пришельцев."""
        self._check_fleet_edges()
        self.aliens.update()

    def _update_screen(self) -> None:
        """Обновляет изображение на экране и отображает новый экран."""
        self.screen.fill(self.settings.background_color)
        self.ship.blit_me()
        for bullet in self.bullets:
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        pygame.display.flip()

    def _check_aliens_on_screen(self) -> None:
        if len(self.aliens) == 0:
            self._create_fleet()


if __name__ == '__main__':
    # Создание экземпляра и запуск игры.
    ai = AlienInvasion()
    ai.run_game()
