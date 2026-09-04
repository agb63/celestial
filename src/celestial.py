# Example file showing a circle moving on screen
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
elapsed = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

frames = [
    pygame.image.load("../assets/maddy/maddy-walk-tmp-3.png").convert_alpha(),
    pygame.image.load("../assets/maddy/maddy-walk-tmp-4.png").convert_alpha()
]

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill((0, 0, 0))

    frameIdx = int(elapsed / 0.2) % len(frames)
    screen.blit(frames[frameIdx], player_pos)

    keys = pygame.key.get_pressed()

    if keys[pygame.K_q] or keys[pygame.K_ESCAPE]:
        running = False

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
    if keys[pygame.K_d]:
        player_pos.x += 150 * dt
        moving = True

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000
    elapsed = elapsed + dt if moving else 0

pygame.quit()
