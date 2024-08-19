import pygame
import math

class turtle:
    def __init__(self, x, y):
        self.origanl_image = pygame.image.load("turtle.png")
        self.image_2 = pygame.transform.scale_by(self.origanl_image, 0.15)
        self.image = self.image_2
        self.rect = self.image.get_rect()
        self.center_x = self.rect.centerx
        self.center_y = self.rect.centery
        self.speed = 5
        self.angle = 0

    def update_position(self, x, y):
        self.x, self.y = x, y
        self.rect.center = (self.x, self.y)


    def move_forward(self, speed):
        # Convert angle to radians
        radians = math.radians(self.angle)
        # Calculate change in x and y
        dx = speed * math.cos(radians)
        dy = -speed * math.sin(radians)  # Negative because y decreases as you go up
        # Update position
        self.rect.x += dx
        self.rect.y += dy
        self.center_x = self.rect.centerx
        self.center_y = self.rect.centery

    def rotate_left(self, angle):
        self.angle += angle
        self.angle %= 360
        self.image = pygame.transform.rotate(self.image2, self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)

    def rotate_right(self, angle):
        self.angle += angle
        self.angle %= 360
        self.image = pygame.transform.rotate(self.image2, self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)

    def lazer(self):
        pass

class icetower:
    def __init__(self, x, y):
        self.image = pygame.image.load("icetower.png")
        self.image_2=pygame.transform.scale(self.image, (120, 80))
        self.rect = self.image_2.get_rect(topleft=(x, y))

    def update_position(self, x, y):
        self.x, self.y = x, y
        self.rect.topleft = (self.x, self.y)

class tower:
    def __init__(self, x, y):
        self.image = pygame.image.load("tower.png")
        self.image_2=pygame.transform.scale(self.image, (200, 100))
        self.rect = self.image_2.get_rect(topleft=(x, y))

    def update_position(self, x, y):
        self.x, self.y = x, y
        self.rect.topleft = (self.x, self.y)

class box:
    def __init__(self, x, y):
        self.image = pygame.image.load("box.png")
        self.image_2=pygame.transform.scale(self.image, (120, 80))
        self.rect = self.image_2.get_rect(topleft=(x, y))

    def update_position(self, x, y):
        self.x, self.y = x, y
        self.rect.topleft = (self.x, self.y)

class mouse:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.transform.scale_by(pygame.image.load("mouse.png"), 0.3)

    def draw(self, win):
        win.blit(self.image, (self.x, self.y))

class box_1:
    def __init__(self):
        self.image_2 = pygame.transform.scale(pygame.image.load('icetower.png'), (100, 100))
        self.rect = self.image_2.get_rect(topleft=(820, 50))

    def draw(self, win):
        pygame.draw.rect(win, 'black', self.rect, 0)
        win.blit(self.image_2, self.rect.topleft)

class box_2:
    def __init__(self):
        self.image_2 = pygame.transform.scale(pygame.image.load('tower.png'), (100, 100))
        self.rect = self.image_2.get_rect(topleft=(950, 50))

    def draw(self, win):
        pygame.draw.rect(win, 'black', self.rect, 0)
        win.blit(self.image_2, self.rect.topleft)

class box_3:
    def __init__(self):
        self.image_2 = pygame.transform.scale(pygame.image.load('box.png'), (100,100))
        self.rect = self.image_2.get_rect(topleft=(820, 200))

    def draw(self, win):
        pygame.draw.rect(win, 'black', self.rect, 0)
        win.blit(self.image_2, self.rect.topleft)

class box_4:
    def __init__(self):
        self.image_2 = pygame.transform.scale(pygame.image.load('gem_1.png'), (100,100))
        self.rect = self.image_2.get_rect(topleft=(950, 200))

    def draw(self, win):
        pygame.draw.rect(win, 'black', self.rect, 0)
        win.blit(self.image_2, self.rect.topleft)

class box_5:
    def __init__(self):
        self.image_2 = pygame.transform.scale(pygame.image.load('gem_2.png'), (100,100))
        self.rect = self.image_2.get_rect(topleft=(820, 350))

    def draw(self, win):
        pygame.draw.rect(win, 'black', self.rect, 0)
        win.blit(self.image_2, self.rect.topleft)

class box_6:
    def __init__(self):
        self.image_2 = pygame.transform.scale(pygame.image.load('gem_3.png'), (100,100))
        self.rect = self.image_2.get_rect(topleft=(950, 350))

    def draw(self, win):
        pygame.draw.rect(win, 'black', self.rect, 0)
        win.blit(self.image_2, self.rect.topleft)

class box_7:
    def __init__(self):
        self.image_2 = pygame.transform.scale(pygame.image.load('gem_4.png'), (100,100))
        self.rect = self.image_2.get_rect(topleft=(820, 500))

    def draw(self, win):
        pygame.draw.rect(win, 'black', self.rect, 0)
        win.blit(self.image_2, self.rect.topleft)

class box_8:
    def __init__(self):
        self.image_2 = pygame.transform.scale(pygame.image.load('turtle.png'), (100,100))
        self.rect = self.image_2.get_rect(topleft=(950, 500))

    def draw(self, win):
        pygame.draw.rect(win, 'black', self.rect, 0)
        win.blit(self.image_2, self.rect.topleft)

class box_9:
    def __init__(self):
        self.image_2 = pygame.transform.scale(pygame.image.load('trash.png'), (100,100))
        self.rect = self.image_2.get_rect(topleft=(820, 650))

    def draw(self, win):
        pygame.draw.rect(win, 'black', self.rect, 0)
        win.blit(self.image_2, self.rect.topleft)

class box_10:
    def __init__(self):
        self.image_2 = pygame.transform.scale(pygame.image.load('save.png'), (100,100))
        self.rect = self.image_2.get_rect(topleft=(950, 650))

    def draw(self, win):
        pygame.draw.rect(win, 'black', self.rect, 0)
        win.blit(self.image_2, self.rect.topleft)

class gem_1:
    def __init__(self, x, y):
        self.image = pygame.image.load("gem_1.png")
        self.image_2=pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image_2.get_rect(topleft=(x, y))

    def update_position(self, x, y):
        self.x, self.y = x, y
        self.rect.topleft = (self.x, self.y)

class gem_2:
    def __init__(self, x, y):
        self.image = pygame.image.load("gem_2.png")
        self.image_2=pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image_2.get_rect(topleft=(x, y))

    def update_position(self, x, y):
        self.x, self.y = x, y
        self.rect.topleft = (self.x, self.y)

class gem_3:
    def __init__(self, x, y):
        self.image = pygame.image.load("gem_3.png")
        self.image_2=pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image_2.get_rect(topleft=(x, y))

    def update_position(self, x, y):
        self.x, self.y = x, y
        self.rect.topleft = (self.x, self.y)

class gem_4:
    def __init__(self, x, y):
        self.image = pygame.image.load("gem_4.png")
        self.image_2=pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image_2.get_rect(topleft=(x, y))

    def update_position(self, x, y):
        self.x, self.y = x, y
        self.rect.topleft = (self.x, self.y)

class selection_box:
    def __init__(self, x, y,z,q):
        self.size=(z,q)
        self.rect = pygame.Rect(x, y,self.size[0], self.size[1])
    
    def draw(self, win, color):
        pygame.draw.rect(win, color, self.rect, 0)