import pygame
from pygame import display
import os
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pythong game")

WHITE = (255, 255, 255)

FPS = 60

SPACESHIP_HEIGHT, SPACESHIP_WIDTH = 55, 40

VEL = 3  # speed of our player

YELLOW_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('Assets', 'spaceship_yellow.png'))

YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    YELLOW_SPACESHIP_IMAGE, (SPACESHIP_HEIGHT, SPACESHIP_WIDTH)), 90)

RED_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('Assets', 'spaceship_red.png'))

RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    RED_SPACESHIP_IMAGE, (SPACESHIP_HEIGHT, SPACESHIP_WIDTH)), 270)


def draw_window(red, yellow):
    WIN.fill((WHITE))
    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP, (red.x, red.y))
    pygame.display.update()


def main():
    red = pygame.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys_pressed = pygame.key.get_pressed()

        # Moving yellow player
        if keys_pressed[pygame.K_a]:
            yellow.x -= VEL
        if keys_pressed[pygame.K_d]:
            yellow.x += VEL
        if keys_pressed[pygame.K_w]:
            yellow.y -= VEL
        if keys_pressed[pygame.K_s]:
            yellow.y += VEL

        # Moving red player
        if keys_pressed[pygame.K_LEFT]:
            red.x -= VEL
        if keys_pressed[pygame.K_RIGHT]:
            red.x += VEL
        if keys_pressed[pygame.K_UP]:
            red.y -= VEL
        if keys_pressed[pygame.K_DOWN]:
            red.y += VEL

        draw_window(red, yellow)
    pygame.quit()


if __name__ == "__main__":
    main()
