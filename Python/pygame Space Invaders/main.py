import pygame
import os
import time
import random



## Pygame initialize
pygame.font.init()

WIDTH, HEIGHT = 750, 750
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooter")

## Load images
RED_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_red_small.png"))
BLUE_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_blue_small.png"))
GREEN_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_green_small.png"))


## Player Ship
YELLOW_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_yellow.png"))

## Lasers
RED_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_red.png"))
GREEN_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_green.png"))
BLUE_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_blue.png"))
YELLOW_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_yellow.png"))

## Background
BG = pygame.transform.scale(pygame.image.load(os.path.join("assets", "background-black.png")), (WIDTH, HEIGHT))

## Laser
class Laser (object):
    def __init__ (self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        self.mask = pygame.mask.from_surface(self.img)

    def draw (self, window):
        window.blit(self.img, (self.x, self.y))

    def move (self, vel):
        self.y += vel

    def off_screen (self, height):
        return not(self.y <= height and self.y >= 0)

    def collision (self, obj):
        return collide(self, obj)


## Ship
class Ship (object):

    COOLDOWN = 15

    def __init__ (self, x, y, health=100):
        self.x = x
        self.y = y
        self.health = health
        self.ship_img = None
        self.laser_img = None
        self.lasers  =  []
        self.cool_down_counter = 0

    def draw (self, window):  # can't work in this oject because ship img  and lasers are none
        window.blit(self.ship_img, (self.x, self.y))
        for laser in self.lasers:
            laser.draw(window)

    def move_lasers (self, vel, obj):
        self.cool_down()
        for laser in self.lasers :
            laser.move(vel)
            if laser.off_screen(HEIGHT):
                self.lasers.remove(laser)
            elif laser.collision(obj):
                obj.health -= 10
                self.lasers.remove(laser)


    def cool_down (self):
        if self.cool_down_counter >= self.COOLDOWN :
            self.cool_down_counter = 0
        elif self.cool_down_counter <= self.COOLDOWN :
            self.cool_down_counter += 1


    def shoot (self):
        if self.cool_down_counter == 0:
            laser = Laser (self.x, self.y, self.laser_img)
            self.lasers.append(laser)
            self.cool_down_counter = 1


    def get_width (self):
        return self.ship_img.get_width()

    def get_height (self):
        return self.ship_img.get_height()


## Player Ship
class Player(Ship):
    def __init__ (self, x, y, health=100):
        super().__init__(x, y, health)
        self.ship_img = YELLOW_SPACE_SHIP
        self.laser_img = YELLOW_LASER
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.max_health = health
 
    def move_lasers (self, vel, objs):
        self.cool_down()
        for laser in self.lasers :
            laser.move(vel)
            if laser.off_screen(HEIGHT):
                self.lasers.remove(laser)
            else:
                for obj in objs:
                    if  laser.collision(obj):
                        objs.remove(obj)
                        self.lasers.remove(laser)

    def draw(self, window):
        super().draw(window)
        self.healthbar(window)

    def healthbar(self, window):
        pygame.draw.rect(window, (255, 0, 0), (self.x, self.y + self.get_height() + 10, self.get_width(), 10))
        pygame.draw.rect(window, (0, 255, 0), (self.x, self.y + self.get_height() + 10, self.get_width()*(1 - (self.max_health - self.health)/self.max_health), 10))

#  Enemy Ship
class Enemy(Ship):

    COLOR_MAP = {
        "red":(RED_SPACE_SHIP, RED_LASER), 
        "green":(GREEN_SPACE_SHIP, GREEN_LASER), 
        "blue":(BLUE_SPACE_SHIP, BLUE_LASER)
    }

    def __init__ (self, x, y, color, level, health=100):
        super().__init__(x, y, health)
        self.ship_img, self.laser_img = self.COLOR_MAP[color]
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.level = level

    def move_lasers (self, vel, obj):
        self.cool_down()
        for laser in self.lasers :
            laser.move(vel*self.level)
            if laser.off_screen(HEIGHT):
                self.lasers.remove(laser)
            elif laser.collision(obj):
                obj.health -= 10
                self.lasers.remove(laser)

    def cool_down (self):
        if self.cool_down_counter >= self.COOLDOWN/self.level :
            self.cool_down_counter = 0
        elif self.cool_down_counter <= self.COOLDOWN/self.level :
            self.cool_down_counter += 1


    def move (self, vel):
        self.y += vel

    def shoot (self):
        if self.cool_down_counter == 0:
            laser = Laser (self.x - 10, self.y, self.laser_img)
            self.lasers.append(laser)
            self.cool_down_counter = 1
            self.cool_down()

## check collide
def collide (obj1, obj2):
    offset_x = obj2.x - obj1.x
    offset_y = obj2.y - obj1.y
    return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None

## Main function
def main():
    run = True
    FPS = 30
    level = 0
    lives = 1
    lost = False
    lost_count = 0
    main_font = pygame.font.SysFont("Consolas", 30)


    enemies = []
    wave_length = 5 # emeny amout
    enemy_vel = 1


    player_vel = 10
    laser_vel = 8

    player = Player(300, 600)

    clock = pygame.time.Clock()

    def redraw_window():
        WIN.blit(BG, (0, 0))

        ## draw text
        lives_label = main_font.render(f"Lives: {lives}", 1, (255, 255, 255))
        level_label = main_font.render(f"Level: {level}", 1, (255, 255, 255))


        for enemy in enemies:
            enemy.draw(WIN)

        player.draw(WIN)



        WIN.blit(level_label, (10, 10))
        WIN.blit(lives_label, (WIDTH + level_label.get_width()/2 - 10, 10))

        if lost:
            lost_label = main_font.render("You Lost !", 1, (255, 255, 255))
            WIN.blit(lost_label, (WIDTH/2 - lost_label.get_width()/2, HEIGHT/2))

        pygame.display.update()

    while run: 
        clock.tick(FPS)

        redraw_window()

        if lives <= 0 or player.health <= 0:
            lost = True
            lost_count += 1

        if lost:
            if lost_count > FPS * 3:
                run = False
            else:
                continue


        if len(enemies) == 0:
            level += 1
            wave_length += 5
            for i in range(wave_length):  # random.randrange(A, B) :  a randm number from A to BB
                enemy = Enemy(random.randrange(50, WIDTH-100), random.randrange(-1500, -100), random.choice(["red", "green", "blue"]), level)
                enemies.append(enemy)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        
        ## movment
        if not lost:
            if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and player.x - player_vel > 0: # left
                player.x -= player_vel
            if (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and player.x + player_vel + player.get_width() < WIDTH: # right
                player.x += player_vel
            if (keys[pygame.K_w] or keys[pygame.K_UP]) and player.y - player_vel > 0: # up
                player.y -= player_vel
            if (keys[pygame.K_s] or keys[pygame.K_DOWN]) and player.y + player_vel + player.get_height() < HEIGHT: #down
                player.y += player_vel


            player.shoot()
    
            for enemy in enemies[:]:
                enemy.move(enemy_vel)
                enemy.move_lasers(laser_vel, player)
                if random.randrange(0,5) == 1:
                    enemy.shoot()
                if collide(player, enemy):
                    player.health -= 10
                    enemies.remove(enemy)
                if enemy.y + enemy.get_height() > HEIGHT:
                    lives -= 1
                    enemies.remove(enemy)

            player.move_lasers(0 - laser_vel, enemies)

            if player.health < 100:
                player.health += 1/30
            else:
                continue


def main_menu ():
    title_font = pygame.font.SysFont("Consolas", 40)
    run = True
    while run:
        WIN.blit(BG, (0, 0))
        title_label = title_font.render("Press the mouse to begin ...", 1, (255, 255, 255))
        # WIN.blit(title_label, (WIDTH/2 - title_label.get_width()/2), (HEIGHT/2))
        WIN.blit(title_label, ((WIDTH/2 - title_label.get_width()/2), HEIGHT/2))

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                main()

    pygame.quit()


main_menu()

