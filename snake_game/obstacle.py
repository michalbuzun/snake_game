from random import randint
import pygame

from snake_game.constants import SCREEN_HEIGHT, SCREEN_WIDTH, SNAKE_INITIAL_HEIGHT, SNAKE_INITIAL_WIDTH


class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((SNAKE_INITIAL_HEIGHT, SNAKE_INITIAL_WIDTH))
        self.image.fill("green")
        self.rect = self.image.get_rect()
        self.rect.midbottom = (randint(0, SCREEN_WIDTH), randint(0, SCREEN_HEIGHT))
        
    def update(self) -> None:  # type: ignore
        ...
