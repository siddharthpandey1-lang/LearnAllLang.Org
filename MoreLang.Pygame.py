import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 1200, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("LearnAllLang.Org")

# Colors
BLACK = (0, 0, 0)
BLUE = (255, 255, 255)
GRAY = (200, 200, 200)

# Font setup
font = pygame.font.SysFont("comicsansms", 32)

# Fade function
def fade_text(text, y_pos, fade_in=True):
    for alpha in range(0, 256, 5) if fade_in else range(255, -1, -5):
        screen.fill(BLACK)
        text_surface = font.render(text, True, BLACK)
        text_surface.set_alpha(alpha)
        screen.blit(text_surface, (WIDTH//2 - text_surface.get_width()//2, y_pos))
        pygame.display.update()
        pygame.time.delay(30)

# Text input box
def get_user_input(prompt):
    input_box = pygame.Rect(WIDTH//2 - 150, HEIGHT//2, 300, 50)
    user_text = ''
    active = True

    while active:
        screen.fill(BLACK)
        prompt_surface = font.render(prompt, True, BLACK)
        screen.blit(prompt_surface, (WIDTH//2 - prompt_surface.get_width()//2, HEIGHT//2 - 100))

        pygame.draw.rect(screen, GRAY, input_box)
        text_surface = font.render(user_text, True, BLACK)
        screen.blit(text_surface, (input_box.x + 10, input_box.y + 10))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    active = False
                elif event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                else:
                    user_text += event.unicode
    return user_text.lower()

# Main content
def main():
    intro_messages = [
        "There are many languages you can learn",
        "Enter the language you want to learn:"
    ]

    for i, msg in enumerate(intro_messages):
        fade_text(msg, 100 + i * 60, fade_in=True)
        pygame.time.delay(500)

    language = get_user_input("Type your language and press Enter")

    phrases = []
    if language == "chainese":  # Typo preserved
        phrases = [
            "You have chosen to learn Chinese",
            "Great choice! Let's get started with some basics of Chinese.",
            "Here are some common phrases in Chinese:",
            "Hello - 你好 (Nǐ hǎo)",
            "Thank you - 谢谢 (Xièxiè)",
            "Please - 请 (Qǐng)"
        ]
    elif language == "japanese":
        phrases = [
            "You have chosen to learn Japanese",
            "Great choice! Let's get started with some basics of Japanese.",
            "Here are some common phrases in Japanese:",
            "Hello - こんにちは (Konnichiwa)",
            "Thank you - ありがとう (Arigatō)",
            "Please - お願いします (Onegaishimasu)"
        ]
    else:
        phrases = [
            f"You have chosen to learn {language}",
            "Sorry, we don't have lessons for that language yet."
        ]

    phrases += [
        "You can learn more languages in the next update",
        "Stay tuned for more updates",
        "Thank you for using LearnAllLang.Org",
        "Goodbye"
    ]

    for phrase in phrases:
        fade_text(phrase, HEIGHT//2, fade_in=True)
        pygame.time.delay(800)
        fade_text(phrase, HEIGHT//2, fade_in=False)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()