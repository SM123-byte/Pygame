import pygame

pygame.init()

MOVE_SPEED = 5

screen = pygame.display.set_mode((640,480))
pygame.display.set_caption("My First Game Screen With Sprites")

clock = pygame.time.Clock()

rect_x = (640//2 - 60//2)
rect_y = (480//2 - 100//2)

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True 

    
    pressed_key = pygame.key.get_pressed()

    if pressed_key[pygame.K_UP] or pressed_key[pygame.K_w]:
        rect_y -= MOVE_SPEED
    if pressed_key[pygame.K_DOWN] or pressed_key[pygame.K_s]:
        rect_y += MOVE_SPEED
    if pressed_key[pygame.K_LEFT] or pressed_key[pygame.K_a]:
        rect_x -= MOVE_SPEED
    if pressed_key[pygame.K_RIGHT] or pressed_key[pygame.K_d]:
        rect_x += MOVE_SPEED

    screen.fill((0,0,0))

    pygame.draw.rect(screen, "blue", pygame.Rect(rect_x, rect_y, 60, 100))

    pygame.display.flip()

    clock.tick(60)

pygame.quit()