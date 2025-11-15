# All the basics coded 

import pygame

pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((640,480))
pygame.display.set_caption("My First Game Screen With Elements")

# All the colours

WHITE = (255, 255, 255)
AQUA = (0, 255, 255)
RECT_COLOR = (0, 125, 125)

# All the text, surfaces and rect

font = pygame.font.Font(None, 36)
text_surface = font.render("My First Element Game Screen!", True, AQUA)
text_rect = text_surface.get_rect(center =(320,50))

# Game Loop

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill(WHITE)
    pygame.draw.rect(screen, RECT_COLOR, pygame.Rect(100,130,60,100))

    screen.blit(text_surface, text_rect)
    pygame.display.flip()

pygame.quit()