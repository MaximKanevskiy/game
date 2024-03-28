class Settings:
    """Класс для хранения всех настроек игры."""
    def __init__(self):
        """Инициализирует настройки игры."""
        # Параметры экрана
        self.screen_width = 1200
        self.screen_height = 800
        self.background_color = (230, 230, 230)  # светло-серый фон

        self.ship_speed = 0.75
        self.ship_limit = 2

        self.bullet_speed = 0.5
        self.bullets_allowed = 1

        self.alien_speed = 1
        self.alien_width = 76
        self.alien_height = 80
        self.fleet_drop_speed = 10
        self.fleet_direction = 1
