import pygame
import random

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
snake_x = 0
snake_y = 0
snake = [(0, 0), (20, 0), (40, 0)]
food_x = random.randrange(0, 1280, 20)
food_y = random.randrange(0, 720, 20)
speed = 20
direction = 0
past_time = 0
eaten = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if snake_x == food_x - 20 and snake_y == food_y and (direction == "right" or direction == 0):
        eaten = True
    elif snake_x == food_x + 20 and snake_y == food_y and direction == "left":
        eaten = True
    elif snake_y == food_y - 20 and snake_x == food_x and direction == "down":
        eaten = True
    elif snake_y == food_y + 20 and snake_x == food_x and direction == "up":
        eaten = True

    if eaten:
        food_x = random.randrange(0, 1280, 20)
        food_y = random.randrange(0, 720, 20)

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
            snake_x += speed
        elif direction == "left":
            snake_x -= speed
        elif direction == "down":
            snake_y += speed
        elif direction == "up":
            snake_y -= speed
        elif direction == 0:
            snake_x += speed
        if eaten:
            snake.insert(0, (snake_x, snake_y))
            eaten = False
        else:
            snake.pop()
            snake.insert(0, (snake_x, snake_y))

        screen.fill("black")
        for i in range(len(snake)):
            x, y = snake[i]
            pygame.draw.rect(screen, (0, 255, 0), (x, y, 20, 20))
        pygame.draw.rect(screen, (255, 0, 0), (food_x, food_y, 20, 20))
        past_time = pygame.time.get_ticks()

    pygame.display.flip()
    clock.tick(60)


pygame.quit()