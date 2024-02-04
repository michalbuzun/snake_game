import pygame
from snake_game.constants import FPS, SCREEN_HEIGHT, SCREEN_WIDTH
from snake_game.obstacle import Obstacle
from snake_game.snake import Snake



pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

clock = pygame.time.Clock()

snake = Snake()
snake_group = pygame.sprite.GroupSingle()  # type: ignore
snake_group.add(snake)  # type: ignore

obstacle = Obstacle()
obstacle_group = pygame.sprite.GroupSingle()  # type: ignore
obstacle_group.add(obstacle)  # type: ignore

running = True
game_active = True
while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False

    if game_active:
        snake_group.update(events)
        snake_group.draw(screen)

        obstacle_group.update()
        obstacle_group.draw(screen)

    else:
        ...

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
