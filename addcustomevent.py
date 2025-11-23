import pygame

def main():
    pygame.init()
    screen_height, screen_width = 500, 500
    screen = pygame.display.set_mode((screen_height, screen_width))
    pygame.display.set_caption("Colour Changing Sprite With Custom Event")

    colors = {
        'red' : pygame.Color('red'),
        'yellow' : pygame.Color('yellow'),
        'green' : pygame.Color('green'),
        'blue' : pygame.Color('blue'),
        'white' : pygame.Color('white')
    }

    sp1_color = colors['white']
    sp1_x, sp1_y = 30, 30
    sp1_height, sp1_width = 60, 60

    sp2_color = colors ['blue']
    sp2_x, sp2_y = 400, 400

    clock = pygame.time.Clock()
    done = False
    
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    sp1_color = colors['red']
                elif event.key == pygame.K_y:
                    sp1_color = colors['yellow']
                elif event.key == pygame.K_g:
                    sp1_color = colors['green']
                elif event.key == pygame.K_b:
                    sp1_color = colors['blue']
                elif event.key == pygame.K_w:
                    sp1_color = colors['white']
            
                elif event.key == pygame.K_1:
                    sp2_color = colors['red']
                elif event.key == pygame.K_2:
                    sp2_color = colors['yellow']
                elif event.key == pygame.K_3:
                    sp2_color = colors['green']
                elif event.key == pygame.K_4:
                    sp2_color = colors['blue']
                elif event.key == pygame.K_5:
                    sp2_color = colors['white']
        
        pressed = pygame.key.get_pressed()
        if pressed [pygame.K_LEFT]: sp1_x-=3
        if pressed [pygame.K_RIGHT]: sp1_x+=3
        if pressed [pygame.K_UP]: sp1_y-=3
        if pressed [pygame.K_DOWN]: sp1_y+=3

        pressed = pygame.key.get_pressed()
        if pressed [pygame.K_j]: sp2_x-=3
        if pressed [pygame.K_l]: sp2_x+=3
        if pressed [pygame.K_i]: sp2_y-=3
        if pressed [pygame.K_k]: sp2_y+=3

        sp1_x = min(max(0, sp1_x), screen_width - sp1_width)
        sp1_y = min(max(0, sp1_y), screen_height - sp1_height)

        sp2_x = min(max(0, sp2_x), screen_width - sp1_width)
        sp2_y = min(max(0, sp2_y), screen_height - sp1_height)
     
        screen.fill(pygame.Color('black'))

        pygame.draw.rect(screen, sp1_color, (sp1_x, sp1_y, sp1_height, sp1_width))
        pygame.draw.rect(screen, sp2_color, (sp2_x, sp2_y, sp1_height, sp1_width))

        pygame.display.flip()

        clock.tick(90)

    pygame.quit()

if __name__ == '__main__':
    main()