# Example file showing a circle moving on screen
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
dt = 0
elapsed = 0
flip = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

def _LoadWithFlip(filename):
    img = pygame.image.load(filename).convert_alpha()
    return [img, pygame.transform.flip(img, True, False)]

frames = [
    _LoadWithFlip("../assets/maddy/maddy-walk-tmp-3.png"),
    _LoadWithFlip("../assets/maddy/maddy-walk-tmp-4.png")
]

while True:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break

    keys = pygame.key.get_pressed()

    if keys[pygame.K_q] or keys[pygame.K_ESCAPE]:
        break

    moving = False

    if keys[pygame.K_w]:
        player_pos.y -= 150 * dt
        moving = True
    if keys[pygame.K_s]:
        player_pos.y += 150 * dt
        moving = True
    if keys[pygame.K_a]:
        player_pos.x -= 150 * dt
        moving = True
        flip = 1
    if keys[pygame.K_d]:
        player_pos.x += 150 * dt
        moving = True
        flip = 0

    # fill the screen with a color to wipe away anything from last frame
    screen.fill((0, 0, 0))

    frameIdx = int(elapsed / 0.2) % len(frames)
    screen.blit(frames[frameIdx][flip], player_pos)

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000
    elapsed = elapsed + dt if moving else 0

pygame.quit()
