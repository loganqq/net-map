import pygame
from pygame.locals import *

# Basic example to get used to pygame
def main():
    # Initialize screen
    pygame.init()
    screen = pygame.display.set_mode((150, 50))
    pygame.display.set_caption("Basic example")

    # Fill background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((250, 250, 250))

    # Display text
    font = pygame.font.Font(None, 36)
    text = font.render("Hello there", 1, (10, 10, 10))
    text_pos = text.get_rect()
    text_pos.centerx = background.get_rect().centerx
    background.blit(text, text_pos)

    # Blit everything to the screen
    screen.blit(background, (0, 0))
    pygame.display.flip()

    # Event loop
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                return

        screen.blit(background, (0, 0))
        pygame.display.flip()


if __name__ == "__main__":
    main()
