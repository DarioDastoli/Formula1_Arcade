import pygame

class Track():
    def __init__(self, walls_collection, start_finish_line):
        self.wall_collection = walls_collection
        self.start_finish = start_finish_line
        self.wall_masks = []
        self._get_track_mask()

    def _get_track_mask(self):
        """map all the wall segments as rect and return a list of masks"""
        wall_thickness = 10
        track_masks = []  

        for segment in self.wall_collection:
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

            self.wall_masks.append((rect, rect_mask))