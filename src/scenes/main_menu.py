
import pygame

from settings import *
from src.ui.button import Button


class MainMenu:

    def __init__(self):

        self.title_font = pygame.font.Font(None, 82)
        self.subtitle_font = pygame.font.Font(None, 28)
        self.small_font = pygame.font.Font(None, 22)

        button_x = (SCREEN_WIDTH - BUTTON_WIDTH) // 2

        self.new_game = Button(
            button_x,
            260,
            BUTTON_WIDTH,
            BUTTON_HEIGHT,
            "New Game"
        )

        self.continue_game = Button(
            button_x,
            330,
            BUTTON_WIDTH,
            BUTTON_HEIGHT,
            "Continue Game",
            enabled=False
        )

        self.settings = Button(
            button_x,
            400,
            BUTTON_WIDTH,
            BUTTON_HEIGHT,
            "Settings"
        )

        self.exit_game = Button(
            button_x,
            470,
            BUTTON_WIDTH,
            BUTTON_HEIGHT,
            "Exit Game"
        )

        self.buttons = [
            self.new_game,
            self.continue_game,
            self.settings,
            self.exit_game
        ]

    def draw_background(self, screen):

        # Sky
        screen.fill(SKY_COLOR)

        # Sun
        pygame.draw.circle(
            screen,
            (255, 225, 130),
            (800, 90),
            48
        )

        # Clouds
        for x, y in [(100, 70), (360, 100), (620, 45)]:

            pygame.draw.circle(
                screen, CLOUD_COLOR, (x, y), 24
            )

            pygame.draw.circle(
                screen, CLOUD_COLOR,
                (x + 30, y - 10), 30
            )

            pygame.draw.circle(
                screen, CLOUD_COLOR,
                (x + 60, y), 24
            )

        # Distant hills
        pygame.draw.ellipse(
            screen,
            HILL_COLOR,
            (-100, 190, 650, 450)
        )

        pygame.draw.ellipse(
            screen,
            HILL_COLOR,
            (450, 170, 650, 450)
        )

        # Grass
        pygame.draw.rect(
            screen,
            GRASS,
            (0, 360, SCREEN_WIDTH, 280)
        )

        # Farmhouse walls
        pygame.draw.rect(
            screen,
            (225, 190, 140),
            (60, 310, 190, 140)
        )

        # Farmhouse roof
        pygame.draw.polygon(
            screen,
            (150, 65, 45),
            [(40, 310), (155, 225), (270, 310)]
        )

        # Door
        pygame.draw.rect(
            screen,
            BROWN,
            (140, 375, 38, 75)
        )

        # Left window
        pygame.draw.rect(
            screen,
            SKY_COLOR,
            (85, 340, 42, 42)
        )

        # Right window
        pygame.draw.rect(
            screen,
            SKY_COLOR,
            (190, 340, 42, 42)
        )

        # Trees
        for x, y in [
            (70, 490),
            (850, 380),
            (910, 500)
        ]:

            pygame.draw.rect(
                screen,
                BROWN,
                (x - 10, y, 20, 65)
            )

            pygame.draw.circle(
                screen,
                DARK_GRASS,
                (x, y),
                45
            )

            pygame.draw.circle(
                screen,
                GRASS,
                (x - 15, y - 15),
                30
            )

        # Flowers
        for x in range(30, SCREEN_WIDTH, 55):

            y = 580 + (x % 35)

            pygame.draw.rect(
                screen,
                DARK_GRASS,
                (x, y, 3, 12)
            )

            pygame.draw.circle(
                screen,
                (255, 220, 100),
                (x + 1, y),
                5
            )

    def draw(self, screen):

        self.draw_background(screen)

        # Game title shadow
        shadow = self.title_font.render(
            GAME_TITLE,
            True,
            TITLE_SHADOW_COLOR
        )

        screen.blit(
            shadow,
            shadow.get_rect(
                center=(SCREEN_WIDTH // 2 + 4, 134)
            )
        )

        # Game title
        title = self.title_font.render(
            GAME_TITLE,
            True,
            TITLE_COLOR
        )

        screen.blit(
            title,
            title.get_rect(
                center=(SCREEN_WIDTH // 2, 130)
            )
        )

        # Subtitle
        subtitle = self.subtitle_font.render(
            "A peaceful countryside adventure",
            True,
            BROWN
        )

        screen.blit(
            subtitle,
            subtitle.get_rect(
                center=(SCREEN_WIDTH // 2, 190)
            )
        )

        # Draw buttons
        for button in self.buttons:
            button.draw(screen)

        # Game version
        version = self.small_font.render(
            f"Version {GAME_VERSION}",
            True,
            WHITE
        )

        screen.blit(
            version,
            (15, SCREEN_HEIGHT - 25)
        )

    def handle_event(self, event):

        if self.new_game.is_clicked(event):
            return "game"

        if self.settings.is_clicked(event):
            return "settings"

        if self.exit_game.is_clicked(event):
            return "quit"

        return None
