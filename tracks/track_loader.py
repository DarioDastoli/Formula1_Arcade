import json
from pathlib import Path
from .track import Track
import pygame

def read_track() -> Track:
    """Read the track from the json vlaue"""
    track_path = Path(__file__).with_name('track.json')
    with track_path.open('r', encoding='utf-8') as file:
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


