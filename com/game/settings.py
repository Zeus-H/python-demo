class Settings:
    """存储游戏中的设置类"""

    def __init__(self):
        """初始化游戏的设置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        # 颜色的RBG值
        self.bg_color = (230, 230, 230)
        # 设置移动的像素 和 飞机的生命
        self.ship_limit = 3
        # 子弹设置 射速、大小、颜色、屏幕中最大子弹数
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 48, 48)
        self.bullets_allowed = 3

        # 外星人设置；设置移动的像素
        self.fleet_drop_speed = 10

        self.speedup_scale = 1.1
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """ 初始化随游戏的进行而变化的设置 """
        self.ship_speed = 1.5
        self.bullet_speed = 1.0
        self.alien_speed = 1.0
        # fleet_direction = 1 表示向右移动，为-1表示向左移动
        self.fleet_direction = 1

    def increase_speed(self):
        """ 提高速度设置 """
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

