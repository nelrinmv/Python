import pygame
import random
import sys

# 1. Initialize Pygame and Setup Window
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rocket Space Dodger")
clock = pygame.time.Clock()

# Colors (RGB)
BLACK = (10, 10, 20)
WHITE = (255, 255, 255)
RED = (255, 50, 50)
ORANGE = (255, 165, 0)
YELLOW = (255, 255, 0)

# Game Variables
score = 0
game_over = False

# 2. Player Rocket Configuration
rocket_w, rocket_h = 400, 500  # Starting position coordinates
rocket_speed = 7

# 3. Asteroid Hazard Configuration
asteroid_size = 40
asteroid_speed = 5
# List containing dictionaries of coordinates for each falling obstacle
asteroids = [{"x": random.randint(0, WIDTH - asteroid_size), "y": random.randint(-600, -50)}]

def draw_rocket(x, y):
    """Draws a rocket using polygon and rect shapes."""
    # Rocket body
    pygame.draw.rect(screen, WHITE, (x, y, 30, 50))
    # Rocket nose cone
    pygame.draw.polygon(screen, RED, [(x, y), (x + 15, y - 20), (x + 30, y)])
    # Rocket fins
    pygame.draw.polygon(screen, RED, [(x, y + 30), (x - 10, y + 50), (x, y + 50)])
    pygame.draw.polygon(screen, RED, [(x + 30, y + 30), (x + 40, y + 50), (x + 30, y + 50)])
    # Engine flame
    if random.choice([True, False]):
        pygame.draw.polygon(screen, ORANGE, [(x + 5, y + 50), (x + 15, y + 70), (x + 25, y + 50)])
    else:
        pygame.draw.polygon(screen, YELLOW, [(x + 8, y + 50), (x + 15, y + 65), (x + 22, y + 50)])

# 4. Main Game Loop
while True:
    screen.fill(BLACK)
    
    # Event handling (Window close and restarts)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN and game_over:
            if event.key == pygame.K_r:  # Reset game state
                rocket_w, rocket_h = 400, 500
                asteroids = [{"x": random.randint(0, WIDTH - asteroid_size), "y": random.randint(-600, -50)}]
                score = 0
                asteroid_speed = 5
                game_over = False

    if not game_over:
        # Movement inputs
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and rocket_w > 10:
            rocket_w -= rocket_speed
        if keys[pygame.K_RIGHT] and rocket_w < WIDTH - 40:
            rocket_w += rocket_speed
        if keys[pygame.K_UP] and rocket_h > 20:
            rocket_h -= rocket_speed
        if keys[pygame.K_DOWN] and rocket_h < HEIGHT - 75:
            rocket_h += rocket_speed

        # Manage and move asteroids
        for ast in asteroids:
            ast["y"] += asteroid_speed
            # If asteroid goes off screen, reset it to top and increase score
            if ast["y"] > HEIGHT:
                ast["y"] = random.randint(-150, -50)
                ast["x"] = random.randint(0, WIDTH - asteroid_size)
                score += 1
                # Gradually scale difficulty
                if score % 5 == 0:
                    asteroid_speed += 0.5
                if score % 10 == 0 and len(asteroids) < 6:
                    asteroids.append({"x": random.randint(0, WIDTH - asteroid_size), "y": random.randint(-400, -50)})

            # Draw obstacle
            pygame.draw.ellipse(screen, RED, (ast["x"], ast["y"], asteroid_size, asteroid_size))

            # Hitbox / Collision Checks
            rocket_rect = pygame.Rect(rocket_w, rocket_h - 20, 30, 70)
            ast_rect = pygame.Rect(ast["x"], ast["y"], asteroid_size, asteroid_size)
            if rocket_rect.colliderect(ast_rect):
                game_over = True

        # Draw the rocket
        draw_rocket(rocket_w, rocket_h)

        # Render current score UI
        font = pygame.font.SysFont("Arial", 26)
        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))
    else:
        # Game Over Screen UI
        font_big = pygame.font.SysFont("Arial", 50)
        font_small = pygame.font.SysFont("Arial", 24)
        
        text1 = font_big.render("GAME OVER", True, RED)
        text2 = font_small.render(f"Final Score: {score}", True, WHITE)
        text3 = font_small.render("Press 'R' to Restart or Close Window to Quit", True, WHITE)
        
        screen.blit(text1, (WIDTH // 2 - 120, HEIGHT // 2 - 60))
        screen.blit(text2, (WIDTH // 2 - 60, HEIGHT // 2 + 10))
        screen.blit(text3, (WIDTH // 2 - 180, HEIGHT // 2 + 50))

    pygame.display.flip()
    clock.tick(120)  # Caps game framework at 60 FPS
