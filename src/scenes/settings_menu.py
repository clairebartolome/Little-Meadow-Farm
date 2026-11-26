
import pygame

from settings import *
from src.ui.button import Button


class SettingsMenu:

    def __init__(self):

        self.title_font = pygame.font.Font(None, 64)
        self.font = pygame.font.Font(None, 30)

        self.back_button = Button(
            (SCREEN_WIDTH - BUTTON_WIDTH) // 2,
            480,
            BUTTON_WIDTH,
            BUTTON_HEIGHT,
            "Back"
        )

    def draw(self, screen):

        screen.fill(CREAM)

        title = self.title_font.render(
            "Settings",
            True,
            BROWN
        )

        screen.blit(
            title,
            title.get_rect(
                center=(SCREEN_WIDTH // 2, 100)
            )
        )

        options = [
            f"Resolution: {SCREEN_WIDTH} x {SCREEN_HEIGHT}",
            f"Frame Rate: {FPS} FPS",
            "Music: Coming soon",
            "Sound Effects: Coming soon",
            "Controls: Coming soon"
        ]

        for index, option in enumerate(options):

            text = self.font.render(
                option,
                True,
                BROWN
            )

            screen.blit(
                text,
                text.get_rect(
                    center=(
                        SCREEN_WIDTH // 2,
                        200 + index * 45
                    )
                )
            )

        self.back_button.draw(screen)

    def handle_event(self, event):

        if self.back_button.is_clicked(event):
            return "menu"

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_ESCAPE:
                return "menu"

        return None
