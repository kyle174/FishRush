import pygame
import random

# Player class
class Player(pygame.sprite.Sprite):
 
    def __init__(self, x, y):
        # Call the parent's constructor
        super().__init__()
        # Set the image of the fish
        self.image = pygame.image.load("graphics/userfish.png").convert()
        self.image.set_colorkey((0, 0, 0))
        self.image = pygame.transform.scale(self.image, (55, 55))
        # Fetch the rectangle object that has the dimensions of the image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        # Set speed vector
        self.change_x = 0
        self.change_y = 0
 
    def changespeed(self, x, y):
        # Change the speed of the player
        self.change_x += x
        self.change_y += y
 
    def update(self):
        # Keep the player within the screen
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x > 700-50:
            self.rect.x = 700-50
        if self.rect.y < 0:
            self.rect.y = 0
        if self.rect.y > 400-50:
            self.rect.y = 400-50
        # Move the player accordingly
        self.rect.x += self.change_x
        self.rect.y += self.change_y