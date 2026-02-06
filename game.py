import sys
import pygame
from car import car
from settings import Settings
from car.car import Car
from tracks import track_loader, track
import game_functions as gf

def run_game():
    # Initialize the game
    pygame.init()
    
    track = track_loader.read_track()
    settings = Settings()
  
    screen = pygame.display.set_mode(
        (settings.screen_width, settings.screen_height))
    
    car = Car(screen, settings, (500,160), 90)
        
    while True:
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

        # Watch for keyboard and mouse events
        screen.fill(settings.bg_color)   
        for segment in track.wall_collection:
            pygame.draw.line(screen, (0,0,255), segment[0], segment[1])

        pygame.draw.line(screen, (250,0,0), track.start_finish[0], track.start_finish[1])
        car.rotate()
        
        car.draw()

        

        pygame.display.flip()

run_game()