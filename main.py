import pygame

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
ORNAMENT_AREA_WIDTH = 200 # Width of the area to the right for ornaments
GAME_AREA_WIDTH = SCREEN_WIDTH - ORNAMENT_AREA_WIDTH
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Ostara - Easter Tree Decorator")

# Colors
WHITE = (255, 255, 255)
BROWN = (139, 69, 19)
GREEN = (0, 128, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Ornaments data
ornaments = [
    {'rect': pygame.Rect(GAME_AREA_WIDTH + 20, 50, 30, 30), 'color': RED, 'original_pos': (GAME_AREA_WIDTH + 20, 50)},
    {'rect': pygame.Rect(GAME_AREA_WIDTH + 80, 50, 30, 30), 'color': BLUE, 'original_pos': (GAME_AREA_WIDTH + 80, 50)},
    {'rect': pygame.Rect(GAME_AREA_WIDTH + 140, 50, 30, 30), 'color': YELLOW, 'original_pos': (GAME_AREA_WIDTH + 140, 50)},
    {'rect': pygame.Rect(GAME_AREA_WIDTH + 20, 100, 30, 30), 'color': BLUE, 'original_pos': (GAME_AREA_WIDTH + 20, 100)},
    {'rect': pygame.Rect(GAME_AREA_WIDTH + 80, 100, 30, 30), 'color': YELLOW, 'original_pos': (GAME_AREA_WIDTH + 80, 100)},
    {'rect': pygame.Rect(GAME_AREA_WIDTH + 140, 100, 30, 30), 'color': RED, 'original_pos': (GAME_AREA_WIDTH + 140, 100)},
]

def draw_ornaments(screen, ornaments):
    for ornament in ornaments:
        pygame.draw.circle(screen, ornament['color'], ornament['rect'].center, ornament['rect'].width // 2)

def run_application():
    running = True
    selected_ornament = None

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: # Left mouse button
                    for ornament in ornaments:
                        if ornament['rect'].collidepoint(event.pos):
                            selected_ornament = ornament
                            break
            
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    selected_ornament = None

            elif event.type == pygame.MOUSEMOTION:
                if selected_ornament:
                    selected_ornament['rect'].center = event.pos

        # Fill the background
        screen.fill(WHITE)

        # Draw the tree trunk
        pygame.draw.rect(screen, BROWN, (GAME_AREA_WIDTH // 2 - 20, SCREEN_HEIGHT - 100, 40, 100))

        # Draw the tree canopy
        pygame.draw.polygon(screen, GREEN, [
            (GAME_AREA_WIDTH // 2, SCREEN_HEIGHT - 250),           # Top point
            (GAME_AREA_WIDTH // 2 - 100, SCREEN_HEIGHT - 100),    # Bottom-left point
            (GAME_AREA_WIDTH // 2 + 100, SCREEN_HEIGHT - 100)     # Bottom-right point
        ])

        # Draw the ornament area separator
        pygame.draw.line(screen, (0,0,0), (GAME_AREA_WIDTH, 0), (GAME_AREA_WIDTH, SCREEN_HEIGHT), 2)

        # Draw ornaments
        draw_ornaments(screen, ornaments)

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    run_application()