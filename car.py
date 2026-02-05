import pygame
from settings import Settings

class Car():
    def __init__(self, screen, settings: Settings):
        self.screen = screen 
        
        #load the car image
        self.image = pygame.image.load('images/car.png')
        self.transformed_image = pygame.transform.scale(self.image, (settings.car_height, settings.car_width))
        self.rect = self.transformed_image.get_rect()
        self.screen_rect = screen.get_rect()
        
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.turn_right = False
        self.turn_left = False

    def update_car(self):
        if self.turn_right:
            self.rect.centerx += 1
        elif self.turn_left:
            self.rect.centerx -= 1
            
    def blitme(self):
        """Draw the car at the current location"""
        self.screen.blit(self.transformed_image, self.rect)
