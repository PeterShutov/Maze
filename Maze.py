from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 10:
            self.rect.y -= self.speed

        if keys_pressed[K_s] and self.rect.y < 530:
            self.rect.y += self.speed

        if keys_pressed[K_d] and self.rect.x < 830:
            self.rect.x += self.speed

        if keys_pressed[K_a] and self.rect.x > 10:
            self.rect.x -= self.speed

class Enemy(GameSprite):
    direction = 'left'
    direction2 = 'up'
    def update(self):
        if self.rect.x < 450:
            self.direction = 'right'
        if self.rect.x > 620:
            self.direction = 'left'

        if self.direction == 'right':
            self.rect.x += self.speed

        else:
            self.rect.x -= self.speed

    def update2(self):
        if self.rect.y < 200:
            self.direction = 'down'
        if self.rect.y > 420:
            self.direction = 'up'

        if self.direction == 'up':
            self.rect.y -= self.speed

        else:
            self.rect.y += self.speed

class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height
        self.image = Surface((self.width, self.height))
        self.image.fill((color_1, color_2, color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


player = Player('player.png', 50, 107, 5)
enemy1 = Enemy('free-icon-ghost-121202.png', 300, 200, 2)
enemy2 = Enemy('free-icon-ghost-121202.png', 700, 100, 2)
treasure = GameSprite('winner.png', 800, 450, 0)
wall1 = Wall(0, 0, 0, 100, 550, 700, 9)
wall2 = Wall(0, 0, 0, 100, 50, 700, 10)
wall3 = Wall(0, 0, 0, 100, 200, 10, 350)
wall4 = Wall(0, 0, 0, 200, 300, 450, 10)
wall5 = Wall(0, 0, 0, 800, 50, 10, 350)
wall6 = Wall(0, 0, 0, 450, 50, 10, 130)
wall7 = Wall(0, 0, 0, 350, 170, 200, 10)
wall8 = Wall(0, 0, 0, 350, 300, 10, 150)
wall9 = Wall(0, 0, 0, 640, 390, 10, 170)
wall10 = Wall(0, 0, 0, 450, 460, 200, 10)
wall11 = Wall(0, 0, 0, 450, 300, 10, 80)
wall12 = Wall(0, 0, 0, 650, 170, 150, 10)
wall13 = Wall(0, 0, 0, 100, 430, 130, 10)
wall14 = Wall(0, 0, 0, 250, 50, 10, 130)


window = display.set_mode((900, 600))
display.set_caption('Maze')

background = transform.scale(image.load('1614845760_1-p-fon-tetrad-v-kletku-1.jpg'), (900, 600))

clock = time.Clock()

game = True
finish = False

mixer.init()
mixer.music.load('48bb90af8e1e401.mp3')
kick = mixer.Sound('kick.ogg')
money = mixer.Sound('money.ogg')
mixer.music.play()

font.init()
font = font.Font(None, 150)
win = font.render('YOU WIN!', True, (40, 181, 27))
loos = font.render('GAME OVER!', True, (181, 55, 27))
    
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.blit(background, (0, 0))
        player.reset()
        enemy1.reset()
        treasure.reset()
        player.update()
        enemy1.update()
        enemy2.reset()
        enemy2.update2()
        wall1.draw_wall()
        wall2.draw_wall()
        wall3.draw_wall()
        wall4.draw_wall()
        wall5.draw_wall()
        wall6.draw_wall()
        wall7.draw_wall()
        wall8.draw_wall()
        wall9.draw_wall()
        wall10.draw_wall()
        wall11.draw_wall()
        wall12.draw_wall()
        wall13.draw_wall()
        wall14.draw_wall()

        if sprite.collide_rect(player, treasure):
            finish = True
            money.play()
            window.blit(win, (150, 200))

        if sprite.collide_rect(player, enemy1) or  sprite.collide_rect(player, enemy2) or sprite.collide_rect(player, wall1) or sprite.collide_rect(player, wall2) or sprite.collide_rect(player, wall3) or sprite.collide_rect(player, wall4) or sprite.collide_rect(player, wall5) or sprite.collide_rect(player, wall6) or sprite.collide_rect(player, wall7) or sprite.collide_rect(player, wall8) or sprite.collide_rect(player, wall9) or sprite.collide_rect(player, wall10) or sprite.collide_rect(player, wall11) or sprite.collide_rect(player, wall12) or sprite.collide_rect(player, wall13) or sprite.collide_rect(player, wall14):
            finish = True
            kick.play()
            window.blit(loos, (150, 200))

    display.update()
    clock.tick(60)
