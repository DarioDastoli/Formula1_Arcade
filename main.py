import sys
import pygame
from settings import Settings
from car import Car
import game_functions as gf

def run_game():
    # Initialize the game
    pygame.init()

    settings = Settings()
    
    screen = pygame.display.set_mode(
        (settings.screen_width, settings.screen_height))
    
    car = Car(screen, settings)
    
    pygame.display.set_caption("Arcade F1")

    # Start the main loop for the game
    while True:
        # Watch for keyboard and mouse events
        gf.check_events(car)
        car.update_car()
        gf.update_screen(settings, screen, car)

run_game()