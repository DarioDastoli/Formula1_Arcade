import json
from .track import Track
import pygame

def read_track() -> Track:
    """Read the track from the json vlaue"""
    with open('tracks\\track.json', 'r') as file:
        data = json.load(file)
    
    raw_walls = data['walls']
    raw_start_finish_line = data['start_finish']

    track = Track(raw_walls, raw_start_finish_line)
    return track

def is_valid_walls():
    """Check if the track data is valid"""
    pass

def is_valid_start_finish_line():
    """Check if the start finish line is valid"""
    pass

def get_track_mask(track):
    """map all the wall segments as rect and return a list of masks"""
    wall_thickness = 10
    track_masks = []  

    for segment in track.wall_collection:
        p1, p2 = segment

        if p1[0] == p2[0]:
            rect = pygame.Rect(
                p1[0] - wall_thickness // 2,
                min(p1[1], p2[1]),
                wall_thickness,
                abs(p2[1] - p1[1])
            )

        else:
            rect = pygame.Rect(
                min(p1[0], p2[0]),
                p1[1] - wall_thickness // 2,
                abs(p2[0] - p1[0]),
                wall_thickness
            )

        rect_mask = pygame.Mask((rect.width, rect.height), fill=True)

        track_masks.append((rect, rect_mask))

    return track_masks
