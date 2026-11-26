
import pygame

from settings import *


class GameScene:

    def __init__(self):

        self.font = pygame.font.Font(None, 30)
        self.small_font = pygame.font.Font(None, 24)

        self.day = STARTING_DAY
        self.money = STARTING_MONEY
        self.energy = PLAYER_MAX_ENERGY
        self.seeds = STARTING_SEEDS

    def draw(self, screen):

        # Draw grass
        screen.fill(GRASS)

        # Draw farm tile grid
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

        # Draw farming area
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

        # Draw information bar
        pygame.draw.rect(
            screen,
            CREAM,
            (0, 0, SCREEN_WIDTH, 60)
        )

        information = [
            f"Day: {self.day}",
            "Season: Spring",
            f"Gold: {self.money}",
            f"Energy: {self.energy}",
            f"Seeds: {self.seeds}"
        ]

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

        # Instructions
        text = self.font.render(
            "Welcome to your farm!",
            True,
            WHITE
        )

        screen.blit(
            text,
            text.get_rect(
                center=(SCREEN_WIDTH // 2, 150)
            )
        )

        instruction = self.small_font.render(
            "Press ESC to return to the main menu",
            True,
            WHITE
        )

        screen.blit(
            instruction,
            instruction.get_rect(
                center=(SCREEN_WIDTH // 2, 580)
            )
        )

    def handle_event(self, event):

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_ESCAPE:
                return "menu"

        return None
