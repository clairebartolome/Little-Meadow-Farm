
import pygame

from settings import *

from src.scenes.main_menu import MainMenu
from src.scenes.game_scene import GameScene
from src.scenes.settings_menu import SettingsMenu


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

    # Create game scenes
    scenes = {
        "menu": MainMenu(),
        "game": GameScene(),
        "settings": SettingsMenu()
    }

    # Start at the main menu
    current_scene = "menu"

    running = True

    # ======================================
    # MAIN GAME LOOP
    # ======================================

    while running:

        # Calculate delta time in seconds
        dt = min(clock.tick(FPS) / 1000, 0.05)

        # Process events
        for event in pygame.event.get():

            # Close game window
            if event.type == pygame.QUIT:

                running = False
                break

            # Handle current scene events
            next_scene = scenes[
                current_scene
            ].handle_event(event)

            # Exit game
            if next_scene == "quit":

                running = False
                break

            # Switch scenes
            elif next_scene in scenes:

                # Reset gameplay for New Game
                if next_scene == "game":
                    scenes["game"] = GameScene()

                current_scene = next_scene

        if not running:
            break

        # Update gameplay
        if current_scene == "game":

            scenes["game"].update(dt)

        # Draw current scene
        scenes[current_scene].draw(screen)

        # Update display
        pygame.display.flip()

    # Close Pygame
    pygame.quit()


if __name__ == "__main__":
    main()

