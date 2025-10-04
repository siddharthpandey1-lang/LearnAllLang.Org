import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 1000, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Language Learner")

# Fonts and colors
font_title = pygame.font.SysFont("comicsansms", 40)
font_text = pygame.font.SysFont("comicsansms", 28)
font_input = pygame.font.SysFont("comicsansms", 32)
WHITE = (255, 255, 255)
BLUE = (100, 149, 237)
BLACK = (0, 0, 0)

# Input box setup
input_box = pygame.Rect(250, 300, 300, 40)
user_text = ''
active = False

# Language phrases
phrases = {
    "french": [("Hello", "Bonjour"), ("Thank you", "Merci"), ("Please", "S'il vous plaît")],
    "spanish": [("Hello", "Hola"), ("Thank you", "Gracias"), ("Please", "Por favor")],
    "german": [("Hello", "Hallo"), ("Thank you", "Danke"), ("Please", "Bitte")],
    "italian": [("Hello", "Ciao"), ("Thank you", "Grazie"), ("Please", "Per favore")]
}

def draw_text(text, font, color, surface, x, y):
    rendered = font.render(text, True, color)
    surface.blit(rendered, (x, y))

def show_phrases(language):
    y_offset = 400
    for eng, trans in phrases[language]:
        draw_text(f"{eng} - {trans}", font_text, BLACK, screen, 250, y_offset)
        y_offset += 40

# Main loop
running = True
language_chosen = False
while running:
    screen.fill(WHITE)
    draw_text("What do you want to learn?", font_title, BLUE, screen, 180, 100)
    draw_text("Enter the language:", font_text, BLACK, screen, 250, 250)

    pygame.draw.rect(screen, BLUE if active else BLACK, input_box, 2)
    text_surface = font_input.render(user_text, True, BLACK)
    screen.blit(text_surface, (input_box.x + 5, input_box.y + 5))
    input_box.w = max(300, text_surface.get_width() + 10)

    if language_chosen:
        lang_key = user_text.strip().lower()
        if lang_key in phrases:
            draw_text(f"You have chosen to learn {user_text.title()}", font_text, BLACK, screen, 180, 360)
            show_phrases(lang_key)
        else:
            draw_text("Sorry, we don't have lessons for that language yet.", font_text, BLACK, screen, 180, 400)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            active = input_box.collidepoint(event.pos)
        elif event.type == pygame.KEYDOWN:
            if active:
                if event.key == pygame.K_RETURN:
                    language_chosen = True
                elif event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                else:
                    user_text += event.unicode

    pygame.display.flip()

pygame.quit()
sys.exit()