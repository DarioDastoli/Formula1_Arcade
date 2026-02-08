import pygame
from settings import Settings
import math

class Car():
    def __init__(self, screen: pygame.Surface, settings: Settings, position, orientation):
        self.screen = screen
        self.position = position
        self.local_points = [
            (0, -10),    
            (0, 10),     
            (50, 0)
        ]
        self.position = pygame.Vector2(position)
        self.angle = orientation
        self.turn_right = False
        self.turn_left = False
        self.rotation_speed = settings.rotation_speed
        self.centroid = self.calcuateCentroid()

    def draw(self):
        """Draw the car at the current location"""

        # Rotate the local points based on the current angle
        rotated_points = [
            self.rotate_point(x, y, self.angle, self.position)
            for x, y in self.local_points
        ]
        pygame.draw.polygon(self.screen, (255,0,0), rotated_points)

        # Draw the centroid for debugging purposes
        pygame.draw.circle(self.screen, (255,255,255), self.centroid, 2)

    def rotate(self):
        if self.turn_right:
            self.angle += self.rotation_speed
        elif self.turn_left:
            self.angle -= self.rotation_speed

    def calcuateCentroid(self) -> tuple[int, int]:
        b1_values, b2_values, v_value = self.local_points

        centroid_x = (b1_values[0] + b2_values[0] + v_value[0])/3
        centroid_y = (b1_values[1] + b2_values[1] + v_value[1])/3

        return [centroid_x, centroid_y]
    
    def rotate_point(self, x:float, y:float, angle:float, center: tuple[int,int]):
        angle_rad = math.radians(angle)
        cos_a = math.cos(angle_rad)
        sin_a = math.sin(angle_rad)
        
        # Rotate the point
        rotated_x = x * cos_a - y * sin_a + center[0]
        rotated_y = x * sin_a + y * cos_a + center[1]

        return (rotated_x, rotated_y)
