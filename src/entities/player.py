
import pygame

from settings import *


class Player:

    def __init__(self, x, y):

        # Position and direction
        self.position = pygame.Vector2(x, y)
        self.direction = pygame.Vector2(0, 0)

        # Player settings
        self.speed = PLAYER_SPEED
        self.width = PLAYER_WIDTH
        self.height = PLAYER_HEIGHT

        # Movement status
        self.facing = "down"
        self.is_moving = False

        # Player rectangle
        self.rect = pygame.Rect(
            x,
            y,
            self.width,
            self.height
        )

    def handle_input(self):

        keys = pygame.key.get_pressed()

        self.direction.x = 0
        self.direction.y = 0

        # Move left
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.direction.x -= 1

        # Move right
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.direction.x += 1

        # Move up
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.direction.y -= 1

        # Move down
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.direction.y += 1

        # Determine movement and facing direction
        if self.direction.length_squared() > 0:

            if self.direction.y < 0:
                self.facing = "up"

            elif self.direction.y > 0:
                self.facing = "down"

            elif self.direction.x < 0:
                self.facing = "left"

            elif self.direction.x > 0:
                self.facing = "right"

            # Normalise diagonal movement
            self.direction = self.direction.normalize()

            self.is_moving = True

        else:
            self.is_moving = False

    def move(self, dt):

        # Update player position
        self.position += (
            self.direction * self.speed * dt
        )

        # Horizontal screen boundaries
        self.position.x = max(
            0,
            min(
                self.position.x,
                SCREEN_WIDTH - self.width
            )
        )

        # Vertical screen boundaries
        self.position.y = max(
            HUD_HEIGHT,
            min(
                self.position.y,
                SCREEN_HEIGHT - self.height
            )
        )

        # Update rectangle
        self.rect.topleft = (
            round(self.position.x),
            round(self.position.y)
        )

    def update(self, dt):

        self.handle_input()
        self.move(dt)

    def draw(self, screen):

        x = self.rect.x
        y = self.rect.y

        # Shadow
        pygame.draw.ellipse(
            screen,
            PLAYER_SHADOW_COLOR,
            (x + 2, y + 38, 28, 10)
        )

        # Left leg
        pygame.draw.rect(
            screen,
            PLAYER_TROUSERS_COLOR,
            (x + 7, y + 32, 8, 12)
        )

        # Right leg
        pygame.draw.rect(
            screen,
            PLAYER_TROUSERS_COLOR,
            (x + 17, y + 32, 8, 12)
        )

        # Left shoe
        pygame.draw.rect(
            screen,
            PLAYER_SHOE_COLOR,
            (x + 6, y + 42, 10, 5)
        )

        # Right shoe
        pygame.draw.rect(
            screen,
            PLAYER_SHOE_COLOR,
            (x + 16, y + 42, 10, 5)
        )

        # Body
        pygame.draw.rect(
            screen,
            PLAYER_SHIRT_COLOR,
            (x + 6, y + 20, 20, 15)
        )

        # Left arm
        pygame.draw.rect(
            screen,
            PLAYER_SKIN_COLOR,
            (x + 2, y + 22, 5, 11)
        )

        # Right arm
        pygame.draw.rect(
            screen,
            PLAYER_SKIN_COLOR,
            (x + 25, y + 22, 5, 11)
        )

        # Hair
        pygame.draw.rect(
            screen,
            PLAYER_HAIR_COLOR,
            (x + 5, y + 5, 22, 17)
        )

        # Face
        if self.facing != "up":

            pygame.draw.rect(
                screen,
                PLAYER_SKIN_COLOR,
                (x + 8, y + 8, 16, 13)
            )

            # Facing down
            if self.facing == "down":

                pygame.draw.rect(
                    screen,
                    BLACK,
                    (x + 11, y + 12, 2, 3)
                )

                pygame.draw.rect(
                    screen,
                    BLACK,
                    (x + 19, y + 12, 2, 3)
                )

            # Facing left
            elif self.facing == "left":

                pygame.draw.rect(
                    screen,
                    BLACK,
                    (x + 9, y + 12, 2, 3)
                )

            # Facing right
            elif self.facing == "right":

                pygame.draw.rect(
                    screen,
                    BLACK,
                    (x + 21, y + 12, 2, 3)
                )

        # Straw hat brim
        pygame.draw.rect(
            screen,
            PLAYER_HAT_COLOR,
            (x + 3, y + 3, 26, 5)
        )

        # Straw hat top
        pygame.draw.rect(
            screen,
            PLAYER_HAT_COLOR,
            (x + 9, y, 14, 5)
        )
