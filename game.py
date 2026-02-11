import pygame
from car import car
from settings import Settings
from car.car import Car
from tracks import track_loader, track
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
        
    print(track.wall_collection)

    while True:
        gf.check_events(car)
        if not gf.check_car_wall_collisions(car, track):
            car.update()

        gf.update_screen(settings, track, screen)   
        car.draw()

        pygame.display.flip()

run_game()