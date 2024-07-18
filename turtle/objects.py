import pygame
import math

class turtle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.direction = 0
        self.origanl_image = pygame.image.load("turtle.png")
        self.image2 = pygame.transform.scale_by(self.origanl_image, 0.2)
        self.image = self.image2

    def move_forward(self, distance):
        self.x += distance * math.cos(self.direction)
        self.y += distance * math.sin(self.direction)
    
    def rotate_left(self, angle):
        self.direction += angle
        self.image = pygame.transform.rotate(self.origanl_image, 90)

    def rotate_right(self, angle):
        self.direction -= angle
        self.image = pygame.transform.rotate(self.origanl_image, -90)

    def lazer(self):
        pass

class tower:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("tower.png")

class icetower:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("icetower.png")

class box:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("box.png")

