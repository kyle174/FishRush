import pygame
import random

# Bottle class
class Bottle(pygame.sprite.Sprite):
     
    def __init__(self, width, height):
        # Call the parent class and set variables
        super().__init__()
        self.width = width
        self.height = height
        rotateDegrees = random.randint(0,360)
        # Set the image of the bottle, image from: https://opengameart.org/content/bottle-of-water
        self.image = pygame.image.load("graphics/waterbottle.png").convert()
        self.image.set_colorkey((0, 0, 0))
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.image = pygame.transform.rotate(self.image, rotateDegrees)
        # Fetch the rectangle object that has the dimensions of the image
        self.rect = self.image.get_rect()
        # Set speed vector
        self.change_x = -1
 
    def changespeed(self, x, y):
        # Change the speed of the bottle
        self.change_x += x
 
    def update(self):
        # Move randomly in the y direction
        self.rect.y += random.randint(-2, 2)
        # Reset if off screen
        if self.rect.x < -100:
            self.rect.x = random.randrange(800, 2000)
            self.rect.y = random.randrange(0, 400)
        if self.rect.y < 0:
            self.rect.y = 0
        if self.rect.y > 400-self.width:
            self.rect.y = 400-self.width
        # Move the bottle
        self.rect.x += self.change_x