import pygame


class Ship:
    """管理飞机的类"""

    def __init__(self, ai_game):
        """初始化飞机并设置其初始化位置"""
        self.settings = ai_game.settings
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        # 加载飞机图像并获取其外接矩形
        self.image = pygame.image.load("../images/ship.bmp")
        self.rect = self.image.get_rect()

        # 对于每部新飞机，都将其放在屏幕底部中央
        self.rect.midbottom = self.screen_rect.midbottom

        # 在飞机的属性x、y中存储小数值
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # 按键标志
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        # self.moving_space = False

    def blitme(self):
        """在指定位置绘制飞机"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """ 根据移动标志调整飞机位置 """
        # 更新飞机而不是rect对象x值
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed

        # 根据self.x 更新rect对象
        self.rect.x = self.x
        self.rect.y = self.y

    def center_ship(self):
        """ 让飞船在屏幕底端居中 """
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)