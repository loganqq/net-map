import pygame
from data import data

# initialize pygame
pygame.init()

# set up window
size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Network Traffic")

# create a font for displaying text
font = pygame.font.Font(None, 30)


class Sprite(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()

        self.image = pygame.image.load("./assets/pc.png")
        self.smaller_img = pygame.transform.scale(self.image, (50, 50))

        self.rect = self.smaller_img.get_rect()


# create a dictionary to store the connections
connections = {}

# iterate through the data
for flow in data:
    src_ip = flow["src_ip"]
    dst_ip = flow["dst_ip"]
    # add the connection to the dictionary
    if dst_ip not in connections:
        connections[dst_ip] = [src_ip]
    else:
        connections[dst_ip].append(src_ip)

# create a sprite object
object_ = Sprite()
object_.rect.x = 200
object_.rect.y = 200

all_sprites_list = pygame.sprite.Group(object_)

# main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # clear the screen
    screen.fill((255, 255, 255))

    # display the connections
    y = 50
    for dst_ip, src_ips in connections.items():
        text = f"{dst_ip} is connected to {src_ips}"
        text = font.render(text, True, (0, 0, 0))
        screen.blit(text, (50, y))
        y += 50

    # sprite logic
    all_sprites_list.update()
    all_sprites_list.draw(screen)

    # update the display
    pygame.display.flip()

# quit pygame
pygame.quit()
