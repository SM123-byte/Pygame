import pygame
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PLAYER_SIZE = 30
ENEMY_SIZE = 20
NUM_ENEMIES = 7
PLAYER_COLOR = (0, 128, 255) 
ENEMY_COLOR = (255, 0, 0)
BACKGROUND_COLOR_FALLBACK = (30, 30, 30)
BACKGROUND_IMAGE = None

pygame.init()
pygame.mixer.init()

# For some reason, I couldn't get the background to show up on the game screen:)

try: 
    BACKGROUND_IMAGE = pygame.transform.scale(
        pygame.image.load('/Users/swagatmohanty/Documents/Python/Pygame/background.jpeg').convert(), (SCREEN_WIDTH, SCREEN_HEIGHT)) 
except pygame.error as er:
    print(f"Could not load image {er}")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Add More Sprites Game")

clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)

# Same problem with the music and it not being played:)

try: 
    pygame.mixer.music.load('sound/backgrounds.ogg')
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.5)
except pygame.error as e:
    print(f"Could not load music file: {e}")

class Base(pygame.sprite.Sprite):
    def __init__(self, size, color):
        super().__init__()
        self.image = pygame.Surface([size, size])
        self.image.fill(color)
        self.rect = self.image.get_rect()

class Player(Base):
    def __init__(self):
        super().__init__(PLAYER_SIZE, PLAYER_COLOR)
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.speed = 5

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.x += self.speed
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.bottom < SCREEN_HEIGHT: 
            self.rect.y += self.speed

class Enemy(Base):
    def __init__(self):
        super().__init__(ENEMY_SIZE, ENEMY_COLOR)
        self.rect.x = random.randrange(0, SCREEN_WIDTH - ENEMY_SIZE)
        self.rect.y = random.randrange(0, SCREEN_HEIGHT - ENEMY_SIZE)

all_sprites =  pygame.sprite.Group()
enemy_list = pygame.sprite.Group()

player = Player()
all_sprites.add(player)

for i in range(NUM_ENEMIES):
    enemy = Enemy()
    all_sprites.add(enemy)
    enemy_list.add(enemy)

score = 0

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        
    all_sprites.update()

    collided_enemies = pygame.sprite.spritecollide(player, enemy_list, True)
    
    for enemy in collided_enemies:
        score += 1
        new_enemy = Enemy()
        all_sprites.add(new_enemy)
        enemy_list.add(new_enemy)
        print("Score Increased! ")

    if BACKGROUND_IMAGE:
        screen.blit(BACKGROUND_IMAGE, (0,0))
    else:
        screen.fill(BACKGROUND_COLOR_FALLBACK)

    all_sprites.draw(screen)

    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    pygame.display.flip()

    clock.tick(60)

pygame.quit()