# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 21:28:09 2020

@author: Roy

copy_by:https://ithelp.ithome.com.tw/articles/10220072

"""

from enum import Enum, unique   # 該模組可以用於定義名稱和值
from math import sqrt
from random import randint

import pygame
 # 名稱不可重複,值可以重複
 # 使用 @unique 限制值不能重複
@unique    
class Color(Enum):          # 顏色
    
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GRAY = (242, 242, 242)

    @staticmethod
    def random_color():     # 獲取隨機顏色
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        return (r, g, b)

class Ball(object):        # 球

    def __init__(self, x, y, radius, sx, sy, color = Color.RED): # 初始化
        self.x = x
        self.y = y
        self.radius = radius
        self.sx = sx
        self.sy = sy
        self.color = color
        self.alive = True

    def move(self, screen): # 移動
        self.x += self.sx
        self.y += self.sy
        if self.x - self.radius <= 0 or \
                self.x + self.radius >= screen.get_width():
            self.sx = -self.sx
        if self.y - self.radius <= 0 or \
                self.y + self.radius >= screen.get_height():
            self.sy = -self.sy

    def eat(self, other):   # 吃其他球
        if self.alive and other.alive and self != other:
            dx, dy = self.x - other.x, self.y - other.y
            distance = sqrt(dx ** 2 + dy ** 2)
            if distance < self.radius + other.radius \
                    and self.radius > other.radius:
                other.alive = False
                self.radius = self.radius + int(other.radius * 0.146)

    def draw(self, screen): # 繪製球
        pygame.draw.circle(screen, self.color,
                           (self.x, self.y), self.radius, 0)
def main():
    balls = []  # 定義裝所有球的容器
    pygame.init()   # 初始化導入 pygame 的模組
    screen = pygame.display.set_mode((800, 600))  # 顯示的視窗並設置視窗大小
    pygame.display.set_caption('大球吃小球')    # 設置視窗標題
    running = True
    while running:  # 開啟一個事件循環處理發生的事件
        for event in pygame.event.get():    # 獲取事件並進行處理
            if event.type == pygame.QUIT:
                running = False
            # 處理鼠標事件
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos    # 獲得點擊鼠標的位置
                radius = randint(10, 100)
                sx, sy = randint(-15, 15), randint(-15, 15)
                color = Color.random_color()
                # 在點擊鼠標的位置創建球（大小、速度和顏色隨機）
                ball = Ball(x, y, radius, sx, sy, color)
                balls.append(ball)  # 將球添加到列表容器中
        screen.fill((255, 255, 255))    # 設置視窗背景顏色
        # 取出容器中的球,如果没被吃掉就會繪出,被吃掉就會移除
        for ball in balls:
            if ball.alive:
                ball.draw(screen)
            else:
                balls.remove(ball)
        # 每隔50毫秒就改變球的位置再刷新窗口
        pygame.display.flip()
        pygame.time.delay(50)
        for ball in balls:
            ball.move(screen)
            # 檢查球有没有吃到其他的球
            for other in balls:
                ball.eat(other)


if __name__ == '__main__':
    main()