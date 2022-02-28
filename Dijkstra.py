import pygame

pygame.init()
screen_size = width, height = 400, 250
screen = pygame.display.set_mode(screen_size)
black = [0, 0, 0]
white = [255, 255, 255]
screen.fill(white)


def draw_map():
    while True:
        # circle(surface, color, center, radius)
        pygame.draw.circle(screen, black, (300, (250-185)), 40)

        # polygon(surface, color, points)
        pygame.draw.polygon(
            screen, black, [(115, 40), (75, 70), (105, 150), (36, 64)], True)

        # Hexagon
        pygame.display.flip()


draw_map()
