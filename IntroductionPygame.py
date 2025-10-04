import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen setup
screen_width, screen_height = 1000,600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Language Learning App")

# Colors
background_color = (135, 206, 250)  # Sky blue
text_color = (255, 255, 255)        # White

# Fonts
title_font = pygame.font.SysFont("comicsansms", 40, bold=True)
text_font = pygame.font.SysFont("comicsansms", 30)

# Messages
messages = [
    "Hello!",
    "This is an app where you can learn many languages.",
    "You can learn French, Spanish, German, Italian, and many more.",
    "What's your name?"
]

# Input box setup
input_box = pygame.Rect(250, 400, 300, 40)
user_text = ''
active = False

# Main loop
running = True
while running:
    screen.fill(background_color)

    # Display messages
    for i, msg in enumerate(messages):
        text_surface = text_font.render(msg, True, text_color)
        screen.blit(text_surface, (50, 50 + i * 50))

    # Input box
    pygame.draw.rect(screen, (0, 0, 0), input_box, 2)
    name_surface = text_font.render(user_text, True, text_color)
    screen.blit(name_surface, (input_box.x + 10, input_box.y + 5))

    # Greeting after name is entered
    if user_text and not active:
        greet = title_font.render(f"Hello {user_text}!", True, text_color)
        screen.blit(greet, (250, 500))
        start_msg = text_font.render("Let's start learning!", True, text_color)
        screen.blit(start_msg, (270, 540))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if input_box.collidepoint(event.pos):
                active = True
            else:
                active = False

        elif event.type == pygame.KEYDOWN and active:
            if event.key == pygame.K_RETURN:
                active = False
            elif event.key == pygame.K_BACKSPACE:
                user_text = user_text[:-1]
            else:
                user_text += event.unicode

    pygame.display.flip()

pygame.quit()
sys.exit()