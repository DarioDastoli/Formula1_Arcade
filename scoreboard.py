import pygame


class Scoreboard:
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        self.current_laptime = 0
        self.current_lap = 0
        self.prep_score()

    def prep_score(self):
        score_str = f'Laptime: {self.current_laptime:.2f}s'
        lap_str = f'Lap: {self.current_lap}'
        self.score_image = self.font.render(score_str, True, self.text_color)
        self.lap_image = self.font.render(lap_str, True, self.text_color)

        self.score_rect = self.score_image.get_rect()
        self.score_rect.topright = self.screen_rect.topright

        self.lap_rect = self.lap_image.get_rect()
        self.lap_rect.topright = self.screen_rect.topright
        self.lap_rect.y += 50

    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.lap_image, self.lap_rect)

