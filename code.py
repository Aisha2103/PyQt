from pygame import*


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))


        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y


    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))





class Player(GameSprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_x_speed, player_y_speed):
        GameSprite.__init__(self, player_image, player_x, player_y, size_x, size_y)


        self.x_speed = player_x_speed
        self.y_speed = player_y_speed

    def update(self):
        if hk.rect.x <= win_widht-80 and hk.x_speed > 0 or hk.rect.x >= 0 and hk>x_speed < 0:
            self.rectx +=self.x_speed

            platform_touched = sprite.spritecollide(self, barriers, False)
            if self.x_speed > 0:
                for p in platforms_touched:
                    self.rect.right = min(self.rect.right, p.rect.left)
            elif self.x_speed <0:
                for p in platforms_touched:
                    self.rect.left = max(self.rect.left, p.rect.right)
        if hk.rect.y <= win_heigh-80 and hk.y_speed > 0 or hk.rect.y >=0  and hk.y_speed < 0:
            self.rect.y += self.y_speed
            platforms_touched = sprite.spritecollide(self, barriers, False)
            if sekf.y_speed > 0:
                for p in platforms_touched:
                    self.rect.bottom = min(self.rect.bottom, p.rect.top)
                    if self.y_speed > 0:
                        for p in platforms_touched:
                            self.rect.bottom = min(self.rect.bottom, p.rect.top)
                    elif self.y_speed <0:
                        for p in platforms_touched:
                            self.rect.top = max(self.rect.top, p.rect.bottom)
                    
def fire(self):
    bullet=Bullet('pixelheart.png', self.rect.right, self.rect.centery, 15, 20, 15)
    bullets.add(bullet)


class Enemy(GameSprite):
    side="left"
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        GameSprite.__init__(self, player_image, player_x, player_y, size_x, size_y)
        self.speed = player_speed


    def update(self):
        if self.rect.x <=420:
            self.side = "right"
        if self.rect.x >= win_widh -85:
            self.side ="left"
        if self.side == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed



class Bullet(GameSprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        GameSprite.__init__(self, player_image, player_x, player_y, size_x, size_y)
        self.speed = player_speed
    def update(self):
        self.rect.x += self_speed
        if self.rect.x > win_widh+10:
            self.kill()

    

win_widht = 700
win_heigh = 500
display.set_caption("Лабиринт")
window = display.set_mode((win_widht, win_heigh))
back = (119, 210, 223)


barriers = sprite.Group()


monsters = sprite.Group()

w1 = GameSprite('lll.jpg', win_widht /2 - win_heigh /3, win_heigh /2, 300, 50)
w2 = GameSprite('lll.jpg', 370, 100, 50, 400)

bullets = sprite.Group()

barriers.add(w1)
barriers.add(w2)



hk = Player('hello_kit.png', 5, win_heigh - 80, 80 ,80, 0, 0)
final_sprite = GameSprite('final_sprite.png', win_widht - 85, win_heigh - 100, 80, 80)


monster1 = Enemy('bbblue.png', win_widht - 80, 150, 80, 80, 5)
monster2 = Enemy('bbblue.png', win_widht - 80, 150, 80, 80, 5)
Enemy.add(monster1)
Enemy.add(monster2)

finish = final_sprite
run = True
finish = False
while run:

    time.delay(50)


    
    for e in event.get():
        if e.type == QUIT:
            run =False
        elif e.type == KEYDOWN:
            if e.key == K_LEFT:
                hk.x_speed = -5
            elif e.key == K_RIGHT:
                hk.y_speed = 5
            

        elif e.type == KEYUP:
            if e.key == K_LEFT:
                hk.x_speed = 0
            elif e.key == K_RIGHT:
                hk.y_speed = 0
            elif e.key == K_UP:
                hk.y_speed = 0
            elif e.key == K_DOWN:
                hk.y_speed = 0
    if not finish:
        window.fill(back)
        barriers.draw(window)
        monsters.draw(window)
        hk.update()
        
        final_sprite.reset()
        hk.reset()

        
        sprite.groupcollide(monsters, bullets, True, True)
        monsters.update()
        monsters.draw(window)
        sprite.groupcollide(bullets, barriers, True, False)


        if sprite.spritecollide(hk, monsters, False):
            finish = True

            img=image.load('plpl.jpg')
            d =img.get_widht()//img.get_height()
            window.fill((255, 255, 255))
            window.blit(transform.scale(img, (win_height * d, win_height)), (90, 0))

            
        if sprite.collide_rect(hk, final_sprite):
            finish = True
            img = image.load('plpl.jpg')
            window.fill((255, 255, 255))
            window.blit(transform.scale(img, (win_height, win_height)), (0, 0))

    display.update()






        
            






