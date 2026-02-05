import sys
import pygame
from settings import Settings
from car import Car

def check_events(car:Car):
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    # Move the ship to the right.
                    car.turn_right = True
                elif event.key == pygame.K_LEFT:
                    # Move the ship to the right.
                    car.turn_left = True

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    # Move the ship to the right.
                    car.turn_right = False
                elif event.key == pygame.K_LEFT:
                    # Move the ship to the right.
                    car.turn_left = False

def update_screen(settings: Settings, screen: pygame.Surface, car: Car):
        screen.fill(settings.bg_color)   
        car.blitme()

       # make the most recently drawn screen visible
        pygame.display.flip()


