import pygame
from scoreboard import Scoreboard
from settings import Settings
from car.car import Car
from tracks.track import Track


def check_events(car:Car):
    """check for any input from the user"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                raise SystemExit
            if event.key == pygame.K_RIGHT:
                car.turn_right = True
            elif event.key == pygame.K_LEFT:
                car.turn_left = True
            elif event.key == pygame.K_UP:
                car.accelerate = True
            elif event.key == pygame.K_DOWN:
                car.decelerate = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                car.turn_right = False
            elif event.key == pygame.K_LEFT:
                car.turn_left = False
            elif event.key == pygame.K_UP:
                car.accelerate = False
            elif event.key == pygame.K_DOWN:
                car.decelerate = False

def update_screen(settings: Settings, track: Track, screen: pygame.Surface, scoreboard: Scoreboard):
    """Update the screen with the drawing of the track."""
    screen.fill(settings.bg_color)

    for segment in track.wall_collection:
        pygame.draw.line(screen, settings.wall_color, segment[0], segment[1])
    pygame.draw.line(screen, settings.start_finish_color, track.start_finish[0], track.start_finish[1])
    scoreboard.show_score()

def check_car_Start_finish_collision(car: Car, track: Track) -> bool:
    offset = (
        track.start_finish_rect.left - car.rect.left,
        track.start_finish_rect.top - car.rect.top
    )

    if car.mask.overlap(track.start_finish_mask, offset):
        return True
    # print('false')
    return False

def start_lap(car: Car, track: Track, scoreboard: Scoreboard, settings: Settings):
    on_line = check_car_Start_finish_collision(car, track)

    if on_line and not car.on_start_finish:
        car.on_start_finish = True

        # Formation lap
        if scoreboard.formation_lap and scoreboard.current_lap == 0:
            scoreboard.current_lap = 1
            scoreboard.current_laptime = 0
            return

        # Normal lap completion
        if scoreboard.current_laptime > 0:
            print(f'Lap completed in {scoreboard.current_laptime:.2f} seconds!')
            scoreboard.current_lap += 1
            scoreboard.current_laptime = 0

    elif not on_line:
        car.on_start_finish = False

        # Only count time AFTER lap 1 has started
        if scoreboard.current_lap > 0:
            scoreboard.current_laptime += 1 / settings.fps

    scoreboard.prep_score()



