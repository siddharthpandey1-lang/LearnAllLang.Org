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
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Font setup
font = pygame.font.SysFont("comicsansms", 32)
small_font = pygame.font.SysFont("comicsansms", 24)

# Fade-in and fade-out animation
def fade_screen_text(text, y_pos, fade_in=True):
    overlay = pygame.Surface((WIDTH, HEIGHT))
    overlay.fill(BLACK)
    for alpha in range(0, 256, 5) if fade_in else range(255, -1, -5):
        screen.fill(BLACK)
        text_surface = font.render(text, True, WHITE)
        screen.blit(text_surface, (WIDTH // 2 - text_surface.get_width() // 2, y_pos))
        overlay.set_alpha(255 - alpha if fade_in else alpha)
        screen.blit(overlay, (0, 0))
        pygame.display.update()
        pygame.time.delay(30)

# Text input box
def get_user_input(prompt):
    input_box = pygame.Rect(WIDTH // 2 - 150, HEIGHT // 2, 300, 50)
    user_text = ''
    active = True
    while active:
        screen.fill(BLACK)
        prompt_surface = font.render(prompt, True, WHITE)
        screen.blit(prompt_surface, (WIDTH // 2 - prompt_surface.get_width() // 2, HEIGHT // 2 - 100))
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

# Quiz data with English options
quiz_questions = [
    {
        "question": "What is the Chinese word for 'Hello'?",
        "options": ["Hello", "Thank you", "Please", "Goodbye"],
        "answer": 0,
        "explanation": "'你好 (Nǐ hǎo)' means 'Hello' in Chinese."
    },
    {
        "question": "What does 'Arigatō' mean in Japanese?",
        "options": ["Hello", "Please", "Thank you", "Goodbye"],
        "answer": 2,
        "explanation": "'ありがとう (Arigatō)' means 'Thank you' in Japanese."
    },
    {
        "question": "Which phrase means 'Please' in Chinese?",
        "options": ["Hello", "Thank you", "Please", "Goodbye"],
        "answer": 2,
        "explanation": "'请 (Qǐng)' is used to say 'Please' in Chinese."
    },
    {
        "question": "Which of these is a Japanese greeting?",
        "options": ["Hello", "Thank you (Chinese)", "Hello (Chinese)", "Please (Chinese)"],
        "answer": 0,
        "explanation": "'こんにちは (Konnichiwa)' is a common Japanese greeting meaning 'Hello'."
    },
    {
        "question": "Which language uses 'Xièxiè' for 'Thank you'?",
        "options": ["Japanese", "Chinese", "Korean", "Thai"],
        "answer": 1,
        "explanation": "'谢谢 (Xièxiè)' is the Chinese word for 'Thank you'."
    }
]

# Quiz mode
def run_quiz():
    score = 0
    for q in quiz_questions:
        selected = -1
        while selected == -1:
            screen.fill(BLACK)
            question_surface = small_font.render(q["question"], True, WHITE)
            screen.blit(question_surface, (WIDTH // 2 - question_surface.get_width() // 2, 100))
            buttons = []
            for i, option in enumerate(q["options"]):
                btn_rect = pygame.Rect(WIDTH // 2 - 200, 180 + i * 60, 400, 50)
                pygame.draw.rect(screen, GRAY, btn_rect)
                option_surface = small_font.render(option, True, BLACK)
                screen.blit(option_surface, (btn_rect.x + 10, btn_rect.y + 10))
                buttons.append(btn_rect)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for i, btn in enumerate(buttons):
                        if btn.collidepoint(event.pos):
                            selected = i
                            break
        correct = selected == q["answer"]
        score += int(correct)
        feedback = "Correct!" if correct else "Incorrect!"
        color = GREEN if correct else RED
        screen.fill(BLACK)
        feedback_surface = font.render(feedback, True, color)
        explanation_surface = small_font.render(q["explanation"], True, WHITE)
        screen.blit(feedback_surface, (WIDTH // 2 - feedback_surface.get_width() // 2, HEIGHT // 2 - 40))
        screen.blit(explanation_surface, (WIDTH // 2 - explanation_surface.get_width() // 2, HEIGHT // 2 + 20))
        pygame.display.update()
        pygame.time.delay(1500)
    screen.fill(BLACK)
    final_surface = font.render(f"You scored {score}/{len(quiz_questions)}", True, WHITE)
    screen.blit(final_surface, (WIDTH // 2 - final_surface.get_width() // 2, HEIGHT // 2))
    pygame.display.update()
    pygame.time.delay(3000)

# Main content
def main():
    intro_messages = [
        "There are many languages you can learn",
        "Enter the language you want to learn:"
    ]
    for i, msg in enumerate(intro_messages):
        fade_screen_text(msg, 100 + i * 60, fade_in=True)
        pygame.time.delay(500)
    language = get_user_input("Type your language and press Enter")
    phrases = []
    if language == "chinese":
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
        "Let's test your knowledge with a quick quiz!"
    ]
    for phrase in phrases:
        fade_screen_text(phrase, HEIGHT // 2, fade_in=True)
        pygame.time.delay(800)
        fade_screen_text(phrase, HEIGHT // 2, fade_in=False)
    run_quiz()
    fade_screen_text("Goodbye!", HEIGHT // 2, fade_in=True)
    pygame.time.delay(1000)
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()