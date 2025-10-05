import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Language Learner 0.0.2")

# Colors
background_color = (135, 206, 250)  # Sky blue
text_color = (255, 255, 255)        # White

# Font
font = pygame.font.SysFont("comicsansms", 32)

# Fade function
def fade(text_lines):
    fade_surface = pygame.Surface((WIDTH, HEIGHT))
    fade_surface.fill(background_color)
    for alpha in range(0, 255, 5):
        fade_surface.set_alpha(alpha)
        screen.fill(background_color)
        for i, line in enumerate(text_lines):
            text = font.render(line, True, text_color)
            screen.blit(text, (50, 50 + i * 50))
        screen.blit(fade_surface, (0, 0))
        pygame.display.update()
        pygame.time.delay(30)

# Main loop
def main():
    running = True
    input_active = False
    user_text = ''
    phrases = []

    intro_lines = [
        "Update 0.0.2 is here!",
        "You can now learn more languages.",
        "There are many languages you can learn."
    ]
    fade(intro_lines)

    while running:
        screen.fill(background_color)
        prompt = font.render("Enter the language you want to learn:", True, text_color)
        screen.blit(prompt, (50, 50))

        input_box = pygame.Rect(50, 100, 700, 50)
        pygame.draw.rect(screen, (0, 0, 0), input_box, 2)
        text_surface = font.render(user_text, True, text_color)
        screen.blit(text_surface, (input_box.x + 10, input_box.y + 10))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    language = user_text.lower()
                    phrases = [f"You have chosen to learn {user_text}.",
                               f"Great choice! Let's get started with some basics of {user_text}.",
                               f"Here are some common phrases in {user_text}:"]
                    if language == "german":
                        phrases += ["Hello - Hallo", "Thank you - Danke", "Please - Bitte"]
                    elif language == "irish":
                        phrases += ["Hello - Dia dhuit", "Thank you - Go raibh maith agat", "Please - Le do thoil"]
                    elif language == "swahili":
                        phrases += ["Hello - Jambo", "Thank you - Asante", "Please - Tafadhali"]
                    else:
                        phrases += ["Sorry, we don't have lessons for that language yet."]
                    fade(phrases)
                    user_text = ''
                elif event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                else:
                    user_text += event.unicode

        pygame.display.update()

    pygame.quit()
    sys.exit()

main()