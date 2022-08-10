import sys
from time import sleep

import pygame

from alien import Alien
from bullet import Bullet
from settings import Settings
from ship import Ship
from game_stats import GameStats
from button import Button


class AlienInvasion:
    """ 管理游戏资源和行为的类 """

    """ 初始化游戏并创建游戏资源 """
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        # 设置大小的屏幕
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        # 全屏模式运行游戏
        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")

        # 创建一个用于存储游戏统计信息的实例
        self.stats = GameStats(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()
        self.play_button = Button(self, "-- Play --")

    """ 开始游戏的主循环 """
    def run_game(self):
        while True:
            self._check_events()

            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()

            self._update_screen()

    """ 响应按键和鼠标事件 """
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # 关闭按钮 X，退出进程
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                # 常按按钮后 持续移动
                self._check_keyup_events(event, True)
            elif event.type == pygame.KEYUP:
                # 松开按钮后 停止移动
                self._check_keyup_events(event, False)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    """ 更新屏幕上的图像，并切换到新屏幕 """
    def _update_screen(self):
        # 每次循环时都重新绘制屏幕
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        # 如果游戏处于非活跃状态就会绘制 开始按钮
        if not self.stats.game_active:
            self.play_button.draw_button()

        # 让最近绘制的屏幕可见
        pygame.display.flip()

    """ whether?True 移动:False 停止 """
    def _check_keyup_events(self, event, whether):
        if event.key == pygame.K_RIGHT:
            # 右
            self.ship.moving_right = whether
        elif event.key == pygame.K_LEFT:
            # 左
            self.ship.moving_left = whether
        elif event.key == pygame.K_UP:
            # 上
            self.ship.moving_up = whether
        elif event.key == pygame.K_DOWN:
            # 下
            self.ship.moving_down = whether
        elif event.key == pygame.K_SPACE:
            # 空格射击
            self._fire_bullet()
        elif event.key == pygame.K_q:
            sys.exit()

    """ 创建子弹并将其加入编组bullets 中 """
    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    """ 更新子弹的位置并删除消失的子弹 """
    def _update_bullets(self):
        # 更新子弹的位置
        self.bullets.update()

        # 删除消失的子弹
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._check_bullet_alien_collisions()

    """ 创建外星人群 """
    def _create_fleet(self):
        # 创建一个外星人
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        # 存储屏幕的宽度，为了确认一行可以容纳多少外星人
        available_space_x = self.settings.screen_width - (2 * alien_width)
        # 给外星人预留空间，给外星人右边留空白区域， // 整除，丢弃余数
        number_aliens_x = available_space_x // (2 * alien_width)

        # 计算屏幕可以容纳多少行外星人
        ship_height = self.ship.rect.height
        available_space_y = self.settings.screen_height - (3 * alien_height) - ship_height
        number_aliens_y = available_space_y // (2 * alien_height)

        # 创建第一行外星人
        for row_number in range(number_aliens_y):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    """ 创建一个外星人 并放在当前行"""
    def _create_alien(self, alien_number, row_number):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    """ 检查是否靠近边缘，更新外星人群中的所有外星人位置 """
    def _update_aliens(self):
        self._check_fleet_edges()
        self.aliens.update()
        # 检测外星人和飞船之间的碰撞
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            print("-- GAME OVER --")
            self._ship_hit()
        # 检查是否有外星人到达屏幕底端
        self._check_aliens_bottom()

    """ 有外星人到达边缘时采取相应的措施 """
    def _check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    """ 将整群外星人下移，并改变它们的方向 """
    def _change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    """ 响应子弹和外星人碰撞 """
    def _check_bullet_alien_collisions(self):
        # 检查是否有子弹击中了外星人；如果是，就删除相应的子弹和外星人。
        collections = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        # 删除现有的子弹并新建一群外星人
        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()

    """ 响应飞船被外星人撞击 """
    def _ship_hit(self):
        if self.stats.ships_left > 0:
            # 将ship_left 性命减1
            self.stats.ships_left -= 1
            # 清空余下的外星人和子弹
            self.aliens.empty()
            self.bullets.empty()

            # 创建一群新的外星人，并将飞船放到屏幕的中央
            self._create_fleet()
            self.ship.center_ship()

            # 暂停
            sleep(0.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    """ 检查是否有外星人到达了屏幕底端 """
    def _check_aliens_bottom(self):
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # 像飞船被撞到一样处理
                self._ship_hit()
                break

    """ 在玩家单击Play按钮时开始新游戏 """
    def _check_play_button(self, mouse_pos):
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            # 重置游戏统计信息
            self.stats.reset_stats()
            self.stats.game_active = True
            self.settings.initialize_dynamic_settings()

            # 清空余下的外星人和子弹
            self.aliens.empty()
            self.bullets.empty()

            # 创建一群外星人、飞机居中
            self._create_fleet()
            self.ship.center_ship()

            # 隐藏鼠标
            pygame.mouse.set_visible(False)


if __name__ == '__main__':
    # 创建游戏实例并运行
    ai = AlienInvasion()
    ai.run_game()
