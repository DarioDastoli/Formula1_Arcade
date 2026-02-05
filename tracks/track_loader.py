import json
from .track import Track

def read_track() -> Track:
    """Read the track from the json vlaue"""
    with open('tracks\\track.json', 'r') as file:
        data = json.load(file)
    
    raw_walls = data['walls']
    raw_start_finish_line = data['start_finish']
    print("raw walls", raw_walls)
    print("raw start finish line", raw_start_finish_line)

    track = Track(raw_walls, raw_start_finish_line)
    return track

def is_valid_walls():
    """Check if the track data is valid"""
    pass

def is_valid_start_finish_line():
    """Check if the start finish line is valid"""
    pass