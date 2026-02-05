import sys
import pygame
from settings import Settings
from car import Car
from tracks import track_loader, track
import game_functions as gf

def run_game():
    # Initialize the game
    pygame.init()
    
    track = track_loader.read_track()
    settings = Settings()

    print(track.wall_collection)
    print(track.start_finish)    
    screen = pygame.display.set_mode(
        (settings.screen_width, settings.screen_height))
    
    
        
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        # Watch for keyboard and mouse events
        screen.fill(settings.bg_color)   
        for segment in track.wall_collection:
            pygame.draw.line(screen, (0,0,255), segment[0], segment[1])

        pygame.draw.line(screen, (250,0,0), track.start_finish[0], track.start_finish[1])
        pygame.display.flip()

run_game()