import sys
import pygame
from settings import Settings
from car.car import Car
from tracks import track_loader, track

def check_events(car:Car):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                car.turn_right = True
            elif event.key == pygame.K_LEFT:
                car.turn_left = True
            elif event.key == pygame.K_UP:
                car.accelerate = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                car.turn_right = False
            elif event.key == pygame.K_LEFT:
                car.turn_left = False
            elif event.key == pygame.K_UP:
                car.accelerate = False

def update_screen(settings: Settings, track: track, screen: pygame.Surface):
        screen.fill(settings.bg_color)   

        for segment in track.wall_collection:
            pygame.draw.line(screen, settings.wall_color, segment[0], segment[1])

        pygame.draw.line(screen, settings.start_finish_color, track.start_finish[0], track.start_finish[1])
        


