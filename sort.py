import pygame

class Sort:
    def __init__(self, window_width, window_height):
        self.window_width = window_width
        self.window_height = window_height

        self.margin_size = 50
        self.sort_display = pygame.Surface((
            self.window_width - (self.margin_size * 2),
            self.window_height - (self.margin_size * 2)
        ))

        self.sort_display.fill("White")

        self.items_to_sort = [36, 82, 5, 49, 18, 97, 65, 31, 74, 10, 56, 93, 26, 88, 68, 14, 42, 73, 20, 60, 3, 48, 87, 11, 67, 38, 94, 76, 22, 69, 53, 7, 80, 17, 61, 29, 83, 50, 8, 70, 16, 59, 46, 79, 23, 95, 33, 91, 55, 44, 2, 64, 37, 89, 71, 24, 9, 47, 99, 57, 34, 13, 72, 41, 92, 62, 19, 86, 32, 58, 4, 98, 63, 27, 75, 45, 6, 85, 21, 78, 54, 1, 39, 66, 30, 84, 52, 25, 90, 40, 81, 15, 51, 28, 77, 12, 43, 96, 35, 0]
        unique_elements, duplicates = self.find_duplicates(self.items_to_sort)

        print(unique_elements, duplicates)


    def find_duplicates(self, item_list):
        seen = set()
        duplicates = []
        unique_elements = []

        for element in item_list:
            if element in seen:
                duplicates.append(element)
            else:
                seen.add(element)
                unique_elements.append(element)

        return unique_elements, duplicates


    
    def draw_sort_display(self, window_draw_surface):
        window_draw_surface.blit(self.sort_display, (self.margin_size, self.margin_size))

    def update(self):
        pass