class Settings():
    """Класс для хранения всех настроек игры Alien Invasion."""

    def __init__(self):
        """Инициализирует настройки игры"""
        # Параметры экрана
        self.screen_width = 1900
        self.screen_height = 1000
        self.bg_color = (0, 47, 85)

        # Настройка корабля
        self.ship_speed = 1.5

        # параметры снаряда
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 255, 0)
        self.bullets_allowed = 3