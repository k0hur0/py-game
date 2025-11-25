import pygame
from random import uniform as func

pygame.init()

WIDTH = 600
HEIGHT = 400
FPS = 60
bound = 20 
white = (255, 255, 255)
blue = (0, 0, 255)
black = (0, 0, 0)

win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Ball Game")
clock = pygame.time.Clock()

x, y = WIDTH // 2, HEIGHT // 2 
radius = 10
velocity = 8 
vp = 10
score = 0 

vx = velocity * func(-1, 1) 
vy = velocity * func(-1, 1)

border_l = bound + radius
border_u = bound + radius
border_r = WIDTH - bound - radius

p_height = 10 
p_width = 80 
xp = (WIDTH - p_width) // 2
yp = HEIGHT - p_height


def drawScore():
    """Відображає фінальний рахунок у центрі вікна."""
    font = pygame.font.Font(None, 50)
    text = font.render(f"Your score: {score}", True, white)
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    win.blit(text, text_rect)

def drawWindow():
    """Малює вікно, межі, м'яч та майданчик."""
    win.fill(black)

    pygame.draw.rect(win, white, (0, 0, WIDTH, bound)) 

    pygame.draw.rect(win, white, (0, 0, bound, HEIGHT))

    pygame.draw.rect(win, white, (WIDTH - bound, 0, bound, HEIGHT))

    pygame.draw.circle(win, blue, (int(x), int(y)), radius)

    pygame.draw.rect(win, white, (int(xp), yp, p_width, p_height))

    pygame.display.update()

run = True
game_over = False

while run:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            game_over = True 

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and xp > bound:
        xp -= vp
    
    if keys[pygame.K_RIGHT] and xp < WIDTH - bound - p_width:
        xp += vp

    x += vx
    y += vy

    if x + vx < border_l or x + vx > border_r:
        vx = -vx
    
    if y + vy < border_u:
        vy = -vy

    touch_paddle_y = (y + vy >= yp - radius) 
    
    touch_paddle_x = (xp <= x + vx and x + vx <= xp + p_width)

    if touch_paddle_y and touch_paddle_x:
        vy = -vy

        num = 1.5
        vx *= num
        vy *= num

        score += 1
    
    elif y + vy > yp:
        run = False

    drawWindow()

if not run and not game_over:
    drawWindow()
    drawScore() 
    pygame.display.update()
    
    pygame.time.delay(3000)

pygame.quit()