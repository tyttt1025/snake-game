import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
x = 10
y = 10
speed = 20
direction = 0
past_time = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    arrowkeys = [keys[pygame.K_DOWN], keys[pygame.K_LEFT], keys[pygame.K_RIGHT], keys[pygame.K_UP]]
    if arrowkeys[2]:
        direction = "right"
    elif arrowkeys[1]:
        direction = "left"
    elif arrowkeys[0]:
        direction = "down"
    elif arrowkeys[3]:
        direction = "up"

    if (pygame.time.get_ticks() - past_time) > 200:
        if direction == "right":
            x += speed
        elif direction == "left":
            x -= speed
        elif direction == "down":
            y += speed
        elif direction == "up":
            y -= speed
        elif direction == 0:
            x += speed
        screen.fill("black")
        pygame.draw.rect(screen, (0, 255, 0), (x, y, 20, 20))
        past_time = pygame.time.get_ticks()

    pygame.display.flip()
    clock.tick(60)


pygame.quit()