
import pygame

from settings import *
from src.entities.player import Player


class GameScene:

    def __init__(self):

        self.font = pygame.font.Font(None, 30)
        self.small_font = pygame.font.Font(None, 24)

        # Starting player statistics
        self.day = STARTING_DAY
        self.money = STARTING_MONEY
        self.energy = PLAYER_MAX_ENERGY
        self.seeds = STARTING_SEEDS

        # Create the player
        self.player = Player(
            PLAYER_START_X,
            PLAYER_START_Y
        )

    def update(self, dt):

        self.player.update(dt)

    def draw(self, screen):

        # Grass background
        screen.fill(GRASS)

        # Vertical grid lines
        for x in range(0, SCREEN_WIDTH, TILE_SIZE):

            pygame.draw.line(
                screen,
                DARK_GRASS,
                (x, 0),
                (x, SCREEN_HEIGHT)
            )

        # Horizontal grid lines
        for y in range(0, SCREEN_HEIGHT, TILE_SIZE):

            pygame.draw.line(
                screen,
                DARK_GRASS,
                (0, y),
                (SCREEN_WIDTH, y)
            )

        # Draw farming plots
        for row in range(5):

            for col in range(8):

                tile = pygame.Rect(
                    352 + col * TILE_SIZE,
                    256 + row * TILE_SIZE,
                    TILE_SIZE - 2,
                    TILE_SIZE - 2
                )

                pygame.draw.rect(
                    screen,
                    SOIL,
                    tile,
                    border_radius=3
                )

        # Draw player
        self.player.draw(screen)

        # Draw information bar
        pygame.draw.rect(
            screen,
            CREAM,
            (0, 0, SCREEN_WIDTH, HUD_HEIGHT)
        )

        information = [
            f"Day: {self.day}",
            "Season: Spring",
            f"Gold: {self.money}",
            f"Energy: {self.energy}",
            f"Seeds: {self.seeds}"
        ]

        # Display player information
        for index, text in enumerate(information):

            surface = self.small_font.render(
                text,
                True,
                BROWN
            )

            screen.blit(
                surface,
                (20 + index * 185, 20)
            )

        # Display player coordinates
        coordinates = self.small_font.render(
            f"X: {int(self.player.position.x)} "
            f"Y: {int(self.player.position.y)}",
            True,
            WHITE
        )

        screen.blit(coordinates, (15, 75))

        # Display facing direction
        direction_text = self.small_font.render(
            f"Facing: {self.player.facing}",
            True,
            WHITE
        )

        screen.blit(direction_text, (15, 100))

        # Display keyboard controls
        instructions = self.small_font.render(
            "WASD / Arrow Keys: Move | ESC: Main Menu",
            True,
            WHITE
        )

        screen.blit(
            instructions,
            instructions.get_rect(
                center=(SCREEN_WIDTH // 2, 610)
            )
        )

    def handle_event(self, event):

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_ESCAPE:
                return "menu"

        return None
