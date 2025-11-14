import pygame

pygame.init()

SCREEN_HEIGHT = 500
SCREEN_WIDTH = 500

display_surface = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDTH))

background_image = pygame.transform.scale(
    pygame.image.load('/Users/swagatmohanty/Documents/Python/Pygame/Space-Background-Images.jpeg').convert(), (SCREEN_HEIGHT, SCREEN_WIDTH)
)

text = pygame.font.Font(None, 36).render('My First Game Screen', True, pygame.Color('aqua'))

text_rect = text.get_rect(center = (SCREEN_WIDTH//2, SCREEN_HEIGHT//2))

def game_loop():
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        display_surface.blit(background_image, (0,0))
        display_surface.blit(text, text_rect)

        pygame.display.flip()
        clock.tick(30)
            
    pygame.quit()

if __name__ == '__main__':
            game_loop()