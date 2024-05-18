import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BALL_SIZE = 20
PADDLE_WIDTH = 20
PADDLE_HEIGHT = 100
PADDLE_SPEED = 7
BALL_INITIAL_SPEED = 5

# Defining Colors
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
PURPLE = (128, 0, 128)
PINK = (255, 192, 203)
GRAY = (128, 128, 128)
BROWN = (139, 69, 19)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BACKGROUND_COLOR = (0, 128, 128)
PADDLE_COLOR = (255, 255, 0)
BALL_COLOR = (255, 0, 0)
TEXT_COLOR = (128, 0, 128)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Pong Game')


try:
    hit_sound = pygame.mixer.Sound('hit.wav')
except pygame.error:
    hit_sound = None

try:
    score_sound = pygame.mixer.Sound('score.mp3')
except pygame.error:
    score_sound = None

try:
    win_sound = pygame.mixer.Sound('win.mp3')
except pygame.error:
    win_sound = None

try:
    background_image = pygame.image.load('background.png')
    background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
except pygame.error:
    background_image = None

try:
    start_screen_image = pygame.image.load('start_screen.png')
    start_screen_image = pygame.transform.scale(start_screen_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
except pygame.error:
    start_screen_image = None

try:
    game_over_image = pygame.image.load('game_over_screen.png')
    game_over_image = pygame.transform.scale(game_over_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
except pygame.error:
    game_over_image = None


try:
    custom_font = pygame.font.Font('custom_font.ttf', 48)  # Adjust size as needed
except pygame.error:
    custom_font = pygame.font.Font(None, 48)  # Fallback to default font


paddle1 = pygame.Rect(50, (SCREEN_HEIGHT - PADDLE_HEIGHT) // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
paddle2 = pygame.Rect(SCREEN_WIDTH - 50 - PADDLE_WIDTH, (SCREEN_HEIGHT - PADDLE_HEIGHT) // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
ball = pygame.Rect((SCREEN_WIDTH - BALL_SIZE) // 2, (SCREEN_HEIGHT - BALL_SIZE) // 2, BALL_SIZE, BALL_SIZE)


score1 = 0
score2 = 0


def reset_ball():
    ball.x = (SCREEN_WIDTH - BALL_SIZE) // 2
    ball.y = (SCREEN_HEIGHT - BALL_SIZE) // 2
    speed_x = random.choice([BALL_INITIAL_SPEED, -BALL_INITIAL_SPEED])
    speed_y = random.choice([BALL_INITIAL_SPEED, -BALL_INITIAL_SPEED])
    return speed_x, speed_y


ball_speed_x, ball_speed_y = reset_ball()


def draw_paddle(paddle, color):
    pygame.draw.rect(screen, color, paddle, border_radius=10)

def draw_ball(ball, color):
    pygame.draw.ellipse(screen, color, ball)


def score_flash():
    flash_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    flash_surface.set_alpha(128)
    flash_surface.fill((255, 255, 255))
    screen.blit(flash_surface, (0, 0))
    pygame.display.flip()
    pygame.time.delay(100)


def start_screen():
    if start_screen_image:
        screen.blit(start_screen_image, (0, 0))
    else:
        screen.fill(BACKGROUND_COLOR)
    title = custom_font.render('PONG GAME', True, TEXT_COLOR)
    instruction = custom_font.render('Press SPACE to Start', True, TEXT_COLOR)
    screen.blit(title, (SCREEN_WIDTH // 2 - title.get_width() // 2, SCREEN_HEIGHT // 3))
    screen.blit(instruction, (SCREEN_WIDTH // 2 - instruction.get_width() // 2, SCREEN_HEIGHT // 2))
    pygame.display.flip()
    wait_for_key()


def game_over_screen(winner):
    if game_over_image:
        screen.blit(game_over_image, (0, 0))
    else:
        screen.fill(BACKGROUND_COLOR)
    game_over_text = custom_font.render('GAME OVER', True, TEXT_COLOR)
    winner_text = custom_font.render(f'{winner} Wins!', True, TEXT_COLOR)
    instruction = custom_font.render('Press SPACE to Play Again', True, TEXT_COLOR)
    screen.blit(game_over_text, (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2, SCREEN_HEIGHT // 3))
    screen.blit(winner_text, (SCREEN_WIDTH // 2 - winner_text.get_width() // 2, SCREEN_HEIGHT // 2))
    screen.blit(instruction, (SCREEN_WIDTH // 2 - instruction.get_width() // 2, SCREEN_HEIGHT // 2 + 50))
    pygame.display.flip()
    if win_sound:
        win_sound.play()
    wait_for_key()


def wait_for_key():
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    waiting = False


start_screen()


running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and paddle1.top > 0:
        paddle1.y -= PADDLE_SPEED
    if keys[pygame.K_s] and paddle1.bottom < SCREEN_HEIGHT:
        paddle1.y += PADDLE_SPEED
    if keys[pygame.K_UP] and paddle2.top > 0:
        paddle2.y -= PADDLE_SPEED
    if keys[pygame.K_DOWN] and paddle2.bottom < SCREEN_HEIGHT:
        paddle2.y += PADDLE_SPEED

    
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    
    if ball.top <= 0 or ball.bottom >= SCREEN_HEIGHT:
        ball_speed_y = -ball_speed_y
        if hit_sound:
            hit_sound.play()

    
    if ball.colliderect(paddle1) or ball.colliderect(paddle2):
        ball_speed_x = -ball_speed_x
        if hit_sound:
            hit_sound.play()

    
    if ball.left <= 0:
        score2 += 1
        score_flash()
        if score_sound:
            score_sound.play()
        ball_speed_x, ball_speed_y = reset_ball()
    if ball.right >= SCREEN_WIDTH:
        score1 += 1
        score_flash()
        if score_sound:
            score_sound.play()
        ball_speed_x, ball_speed_y = reset_ball()

    
    if background_image:
        screen.blit(background_image, (0, 0))
    else:
        screen.fill(BACKGROUND_COLOR)

    
    draw_paddle(paddle1, PADDLE_COLOR)
    draw_paddle(paddle2, PADDLE_COLOR)
    draw_ball(ball, BALL_COLOR)
    pygame.draw.aaline(screen, WHITE, (SCREEN_WIDTH // 2, 0), (SCREEN_WIDTH // 2, SCREEN_HEIGHT))

    score_text = custom_font.render(f"{score1} - {score2}", True, TEXT_COLOR)
    screen.blit(score_text, (SCREEN_WIDTH // 2 - score_text.get_width() // 2, 20))

    
    pygame.display.flip()

    
    clock.tick(60)

    if score1 == 10 or score2 == 10:
        winner = "Player 1" if score1 == 10 else "Player 2"
        game_over_screen(winner)
        score1, score2 = 0, 0
        start_screen()

pygame.quit()
