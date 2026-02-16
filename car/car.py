import pygame
from settings import Settings
import math

from tracks.track import Track

class Car():
    def __init__(self, screen: pygame.Surface, settings: Settings, position, orientation):
        self.screen = screen
        self.position = pygame.Vector2(position)
        self.angle = orientation

        self.turn_right = False
        self.turn_left = False
        self.accelerate = False
        self.decelerate = False

        self.speed = 0.1
        self.rotation_speed = settings.rotation_speed
        
        self.base_surf = self.create_car_surface(settings)
        self.surface = self.base_surf
        self.rect = self.surface.get_rect(center=self.position)
        self.mask = pygame.mask.from_surface(self.surface)


    def create_car_surface(self, settings: Settings):
        """Create a triangular surface representing the car"""
        base_surface = pygame.Surface((50,40), pygame.SRCALPHA)
        base_surface.fill((0,0,0,0))
        pygame.draw.polygon(
            base_surface,
            (255,0,0),
            [(0, 10), (0, 30), (50, 20)]
        )
        return base_surface

    def update(self, track):
        """update all informations about the car"""
        self.rotate()
        self.move(track)
        self.graphic_update()
        
    def rotate(self):
        """rotate the car"""
        if self.turn_right:
            self.angle += self.rotation_speed
        if self.turn_left:
            self.angle -= self.rotation_speed

    def move(self, track:Track):
        """move the car"""
        angle_rad = math.radians(self.angle)
        
        dx, dy = 0,0

        if self.accelerate:
            dx += self.speed * math.cos(angle_rad)
            dy += self.speed * math.sin(angle_rad)
        elif self.decelerate:
            dx -= self.speed * math.cos(angle_rad)
            dy -= self.speed * math.sin(angle_rad)

        old_x = self.position.x
        self.position.x += dx
        self.graphic_update()

        if self.check_car_wall_collisions(track):
            self.position.x = old_x
            self.graphic_update()

        old_y = self.position.y
        self.position.y += dy
        self.graphic_update()

        if self.check_car_wall_collisions(track):
            self.position.y = old_y
            self.graphic_update()
    

    def graphic_update(self):
        """update the cars surface, rect, and mask"""
        self.surface = pygame.transform.rotate(self.base_surf, -self.angle)
        self.rect = self.surface.get_rect(center=self.position)
        self.mask = pygame.mask.from_surface(self.surface)

    def draw(self):
        """draw the car on the screen"""
        self.screen.blit(self.surface, self.rect)



    def check_car_wall_collisions(self, track: Track) -> bool:
        """check if the car is colliding with the wall rects"""

        for wall_rect, wall_mask in track.wall_masks:

            offset = (
                wall_rect.left - self.rect.left,
                wall_rect.top - self.rect.top
            )

            if self.mask.overlap(wall_mask, offset):
                return True
        
        return False
    