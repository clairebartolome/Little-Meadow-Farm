
import pygame
from settings import *


class Button:

    def __init__(self, x, y, width, height,
                 text, enabled=True):

        self.rect = pygame.Rect(
            x, y, width, height
        )

        self.text = text
        self.enabled = enabled
        self.font = pygame.font.Font(None, 32)

    def draw(self, screen):

        mouse_position = pygame.mouse.get_pos()

        if not self.enabled:
            color = BUTTON_DISABLED_COLOR

        elif self.rect.collidepoint(mouse_position):
            color = BUTTON_HOVER_COLOR

        else:
            color = BUTTON_COLOR

        # Draw button shadow
        shadow_rect = self.rect.move(4, 5)

        pygame.draw.rect(
            screen,
            BUTTON_BORDER_COLOR,
            shadow_rect,
            border_radius=8
        )

        # Draw button
        pygame.draw.rect(
            screen,
            color,
            self.rect,
            border_radius=8
        )

        # Draw button border
        pygame.draw.rect(
            screen,
            BUTTON_BORDER_COLOR,
            self.rect,
            width=3,
            border_radius=8
        )

        # Draw text
        text_surface = self.font.render(
            self.text,
            True,
            BUTTON_TEXT_COLOR
        )

        text_rect = text_surface.get_rect(
            center=self.rect.center
        )

        screen.blit(text_surface, text_rect)

    def is_clicked(self, event):

        if not self.enabled:
            return False

        if event.type == pygame.MOUSEBUTTONDOWN:

            if event.button == 1:

                return self.rect.collidepoint(
                    event.pos
                )

        return False
