
import pygame

from settings import *

from src.scenes.main_menu import MainMenu
from src.scenes.game_scene import GameScene
from src.scenes.settings_menu import SettingsMenu


def main():

    # Initialise Pygame
    pygame.init()

    # Create window
    screen = pygame.display.set_mode(
        (SCREEN_WIDTH, SCREEN_HEIGHT)
    )

    pygame.display.set_caption(GAME_TITLE)

    clock = pygame.time.Clock()

    # Create game scenes
    scenes = {
        "menu": MainMenu(),
        "game": GameScene(),
        "settings": SettingsMenu()
    }

    # Start on the main menu
    current_scene = "menu"

    running = True

    # Main game loop
    while running:

        for event in pygame.event.get():

            # Close window
            if event.type == pygame.QUIT:

                running = False
                break

            # Send events to current scene
            next_scene = scenes[
                current_scene
            ].handle_event(event)

            # Handle scene transitions
            if next_scene == "quit":

                running = False
                break

            elif next_scene in scenes:

                # Reset gameplay when starting
                # a new game
                if next_scene == "game":
                    scenes["game"] = GameScene()

                current_scene = next_scene
                break

        if not running:
            break

        # Draw current scene
        scenes[current_scene].draw(screen)

        # Refresh display
        pygame.display.flip()

        # Limit frame rate
        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()
