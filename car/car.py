import pygame
from settings import Settings
import math

# class Car():
#     def __init__(self, screen, settings: Settings):
#         self.screen = screen 
        
#         #load the car image
#         self.image = pygame.image.load('images/car.png')
#         self.transformed_image = pygame.transform.scale(self.image, (settings.car_height, settings.car_width))
#         self.rect = self.transformed_image.get_rect()
#         self.screen_rect = screen.get_rect()
        
#         self.rect.centerx = self.screen_rect.centerx
#         self.rect.bottom = self.screen_rect.bottom

#         self.turn_right = False
#         self.turn_left = False

#     def update_car(self):
#         if self.turn_right:
#             self.rect.centerx += 1
#         elif self.turn_left:
#             self.rect.centerx -= 1
            
#     def blitme(self):
#         """Draw the car at the current location"""
#         self.screen.blit(self.transformed_image, self.rect)


class Car():
    def __init__(self, screen: pygame.Surface, settings: Settings, position, orientation):
        self.screen = screen
        self.position = position
        self.heading = orientation
        self.base1_coordinates = (500,150) 
        self.base2_coordinates =  (500,170)
        self.vertix_coordinates =  (550,160)
        self.coordinates = [self.base1_coordinates, 
                            self.base2_coordinates,
                            self.vertix_coordinates]
        self.turn_right = False
        self.turn_left = False

        self.centroid = self.calcuateCentroid()

    def draw(self):
        """Draw the car at the current location"""
        pygame.draw.polygon(self.screen, (255,0,0), self.coordinates)
        pygame.draw.circle(self.screen, (255,255,255), self.centroid, 2)

    def rotate(self):
        if self.turn_right:
            self.base1_coordinates = self.rotate_point(self.base1_coordinates[0], self.base1_coordinates[1], 10)
            self.base2_coordinates = self.rotate_point(self.base2_coordinates[0], self.base2_coordinates[1], 10)
            self.vertix_coordinates_coordinates = self.rotate_point(self.vertix_coordinates[0], self.vertix_coordinates[1], 10)
            print(self.coordinates)
                
        elif self.turn_left:
            self.base1_coordinates = self.rotate_point(self.base1_coordinates[0], self.base1_coordinates[1], -10)
            self.base2_coordinates = self.rotate_point(self.base2_coordinates[0], self.base2_coordinates[1], -10)
            self.vertix_coordinates = self.rotate_point(self.vertix_coordinates[0], self.vertix_coordinates[1], -10)
            print(self.coordinates)

        self.coordinates = [self.base1_coordinates, 
                self.base2_coordinates,
                self.vertix_coordinates]

        self.draw()

    def calcuateCentroid(self) -> tuple[int, int]:
        b1_values, b2_values, v_value = self.coordinates

        centroid_x = (b1_values[0] + b2_values[0] + v_value[0])/3
        centroid_y = (b1_values[1] + b2_values[1] + v_value[1])/3

        return [centroid_x, centroid_y]
    
    def rotate_point(self, x:float, y:float, angle:float):
        # Convert angle from degrees to radians
        angle_rad = math.radians(angle)

        # Translate point to origin
        translated_x = x - self.centroid[0]
        translated_y = y - self.centroid[1]
        
        # Apply rotation matrix
        rotated_x = translated_x * math.cos(angle_rad) - translated_y * math.sin(angle_rad)
        rotated_y = translated_x * math.sin(angle_rad) + translated_y * math.cos(angle_rad)
        
        # Translate back to original position
        rotated_x += self.centroid[0]
        rotated_y += self.centroid[1]
        
        print(rotated_x, rotated_y)
        return rotated_x, rotated_y
    
    