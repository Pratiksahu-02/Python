import pygame
import time
import sys

# Initialize pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 600, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Digital Clock")

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Font
font = pygame.font.SysFont("Arial", 80)

clock = pygame.time.Clock()

running = True
while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get current time
    current_time = time.strftime("%I:%M:%S %p")

    # Render text
    text_surface = font.render(current_time, True, GREEN)
    text_rect = text_surface.get_rect(center=(WIDTH//2, HEIGHT//2))

    screen.blit(text_surface, text_rect)

    pygame.display.update()
    clock.tick(1)  # Update once per second

pygame.quit()
sys.exit()