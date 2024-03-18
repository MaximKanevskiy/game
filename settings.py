class Settings:
    """Класс для хранения всех настроек игры."""
    def __init__(self):
        """Инициализирует настройки игры."""
        # Параметры экрана
        self.screen_width = 1200
        self.screen_height = 800
        self.background_color = (230, 230, 230)  # светло-серый фон
        self.ship_speed = 0.75
        self.bullet_speed = 2
