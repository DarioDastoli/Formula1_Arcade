import pygame
from settings import Settings
import math

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

    def update(self):
        """update all informations about the car"""
        self.rotate()
        self.move()
        self.graphic_update()
        
    def rotate(self):
        """rotate the car"""
        if self.turn_right:
            self.angle += self.rotation_speed
        if self.turn_left:
            self.angle -= self.rotation_speed

    def move(self):
        """move the car"""
        angle_rad = math.radians(self.angle)
        if self.accelerate:
            self.position.x += self.speed * math.cos(angle_rad)
            self.position.y += self.speed * math.sin(angle_rad)
        elif self.decelerate:
            self.position.x -= self.speed * math.cos(angle_rad)
            self.position.y -= self.speed * math.sin(angle_rad)
        

    def graphic_update(self):
        """update the cars surface, rect, and mask"""
        self.surface = pygame.transform.rotate(self.base_surf, -self.angle)
        self.rect = self.surface.get_rect(center=self.position)
        self.mask = pygame.mask.from_surface(self.surface)

    def draw(self):
        """draw the car on the screen"""
        self.screen.blit(self.surface, self.rect)

