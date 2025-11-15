import pygame

def main():
    pygame.init()
    screen_height, screen_width = 500, 500
    screen = pygame.display.set_mode((screen_height, screen_width))
    pygame.display.set_caption("Colour Changing Sprite")

    colors = {
        'red' : pygame.Color('red'),
        'yellow' : pygame.Color('yellow'),
        'green' : pygame.Color('green'),
        'blue' : pygame.Color('blue'),
        'white' : pygame.Color('white')
    }

    current_colors = colors['white']

    x, y = 30,30
    sprite_height, sprite_width = 60,60

    clock = pygame.time.Clock()

    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True 

        pressed = pygame.key.get_pressed()
        if pressed [pygame.K_LEFT]: x-=3
        if pressed [pygame.K_RIGHT]: x+=3
        if pressed [pygame.K_UP]: y-=3
        if pressed [pygame.K_DOWN]: y+=3

        x = min(max(0, x), screen_width - sprite_width)
        y = min(max(0, y), screen_height - sprite_height)

        if x == 0: current_colors = colors['blue']
        elif x == screen_width - sprite_width: current_colors = colors['yellow']
        elif y == 0: current_colors = colors['red']
        elif y == screen_height - sprite_height: 
            current_colors = colors['green']
        else:
            current_colors = colors['white']
        
        screen.fill((0,0,0))
        pygame.draw.rect(screen, current_colors, (x, y, sprite_width, sprite_height))
        pygame.display.flip()

        clock.tick(90)

    pygame.quit()

if __name__ == '__main__':
    main()