import os

import pygame


def init_sprite(image : str, x : int = 0, y : int = 0, scale : tuple[int, int] = (32,32)) -> pygame.sprite.Sprite():
    sprite = pygame.sprite.Sprite()
    sprite.image = pygame.transform.scale(pygame.image.load(image), scale)
    sprite.rect = sprite.image.get_rect()
    sprite.rect.topleft = (x, y)

    return sprite