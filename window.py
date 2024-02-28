import pygame
from sort import Sort

class Window:
    def __init__(self, width, height, fps):
        pygame.init()

        self.width = width
        self.height = height
        self.fps = fps
        self.bg_color = "Black"

        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Sort")

        self.draw_surface = pygame.Surface((self.width, self.height))
        self.draw_surface.fill(self.bg_color)

        self.sort_instance = Sort(self.width, self.height)
        self.sort_instance.draw_sort_display(self.draw_surface)

        self.running = True
        

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

        self.screen.fill(self.bg_color)
        self.screen.blit(self.draw_surface, (0, 0))

        pygame.display.flip()
        self.clock.tick(self.fps)

    def close():
        pygame.quit()