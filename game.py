import pygame
from car import car
from settings import Settings
from car.car import Car
from tracks import track_loader, track
from scoreboard import Scoreboard
import game_functions as gf


def run_game():
    # Initialize the game
    pygame.init()
    
    settings = Settings()

    # Set up display, track and car
    screen = pygame.display.set_mode(
        (settings.screen_width, settings.screen_height))
  
    track = track_loader.read_track()    
    car = Car(screen, settings, (500,160), 0)
    scoreboard = Scoreboard(screen)
        
    print(track.wall_collection)

    #run the game at 60 fps
    clock = pygame.time.Clock()
    while True:
        clock.tick(120)
        gf.check_events(car)
        car.update(track)
        gf.update_screen(settings, track, screen, scoreboard)   
        car.draw()
        gf.start_lap(car, track, scoreboard)
        pygame.display.flip()

run_game()