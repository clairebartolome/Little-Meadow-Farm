
import pygame
from settings import *


def main():

    # Initialise Pygame
    pygame.init()

    # Create game window
    screen = pygame.display.set_mode(
        (SCREEN_WIDTH, SCREEN_HEIGHT)
    )

    pygame.display.set_caption(GAME_TITLE)

    # Create game clock
    clock = pygame.time.Clock()

    # Create fonts
    title_font = pygame.font.Font(None, 72)
    subtitle_font = pygame.font.Font(None, 32)
    small_font = pygame.font.Font(None, 22)

    running = True

    # Main game loop
    while running:

        # Handle events
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:
                    running = False

        # Draw grass background
        screen.fill(GRASS)

        # Draw world tile grid
        for x in range(0, SCREEN_WIDTH, TILE_SIZE):

            pygame.draw.line(
                screen,
                DARK_GRASS,
                (x, 0),
                (x, SCREEN_HEIGHT)
            )

        for y in range(0, SCREEN_HEIGHT, TILE_SIZE):

            pygame.draw.line(
                screen,
                DARK_GRASS,
                (0, y),
                (SCREEN_WIDTH, y)
            )

        # Draw title
        title = title_font.render(
            GAME_TITLE,
            True,
            WHITE
        )

        screen.blit(
            title,
            title.get_rect(
                center=(SCREEN_WIDTH // 2, 250)
            )
        )

        # Draw subtitle
        subtitle = subtitle_font.render(
            "Your farming adventure begins here!",
            True,
            CREAM
        )

        screen.blit(
            subtitle,
            subtitle.get_rect(
                center=(SCREEN_WIDTH // 2, 320)
            )
        )

        # Draw instructions
        instructions = small_font.render(
            "Press ESC to exit",
            True,
            WHITE
        )

        screen.blit(
            instructions,
            instructions.get_rect(
                center=(SCREEN_WIDTH // 2, 380)
            )
        )

        # Draw game version
        version = small_font.render(
            f"Version {GAME_VERSION}",
            True,
            WHITE
        )

        screen.blit(
            version,
            (15, SCREEN_HEIGHT - 30)
        )

        # Update display
        pygame.display.flip()

        # Limit frame rate
        clock.tick(FPS)

    # Close Pygame
    pygame.quit()


if __name__ == "__main__":
    main()
