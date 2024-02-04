
from enum import Enum
from typing import List
import pygame

from snake_game.constants import SCREEN_HEIGHT, SCREEN_WIDTH, SNAKE_INITIAL_HEIGHT, SNAKE_INITIAL_WIDTH

class Direction(Enum):
    UP = "up"
    DOWN = "down"
    LEFT = "left"
    RIGHT = "right"
    
class Snake(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((SNAKE_INITIAL_HEIGHT, SNAKE_INITIAL_WIDTH))
        self.image.fill("red")
        self.rect = self.image.get_rect()
        self.rect.midbottom = (int(SCREEN_WIDTH/2), int(SCREEN_HEIGHT/2))
        self.direction = Direction.RIGHT.value

    def update(self, events: List[pygame.event.Event]):
        for event in events:
            if event.type == pygame.KEYDOWN:
                print("event key down")
                if event.key == pygame.K_UP:
                    print("key up pressed")
                    self.direction = "up"

                if event.key == pygame.K_DOWN:
                    self.direction = "down"
                
                if event.key == pygame.K_RIGHT:
                    self.direction = "right"
                
                if event.key == pygame.K_LEFT:
                    self.direction = "left"

        if self.direction == "right":
            self.rect.right += 1
        if self.direction == "left":
            self.rect.right -= 1
        if self.direction == "up":
            self.rect.top -= 1  
        if self.direction == "down":
            self.rect.top += 1  
        