import pygame
import math

class turtle:
    def __init__(self, x, y):
        self.origanl_image = pygame.image.load("turtle.png")
        self.image2 = pygame.transform.scale_by(self.origanl_image, 0.2)
        self.image = self.image2
        self.rect = self.image.get_rect()
        self.center_x = self.rect.centerx
        self.center_y = self.rect.centery
        self.speed = 5
        self.angle = 0


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

