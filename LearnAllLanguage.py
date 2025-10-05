import pygame, sys

# Initialize
pygame.init()
W, H = 900, 700
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("LearnAllLang.Org")
font = pygame.font.SysFont("comicsansms", 32)
BG = (255, 182, 193)  # Light pink
WHITE = (255, 255, 255)

def fade(lines):
    s = pygame.Surface((W, H)); s.fill(BG)
    for a in range(0, 255, 5):
        s.set_alpha(a); screen.fill(BG)
        for i, line in enumerate(lines):
            screen.blit(font.render(line, True, WHITE), (50, 50 + i * 50))
        screen.blit(s, (0, 0)); pygame.display.update(); pygame.time.delay(30)

def get_phrases(lang):
    lang = lang.lower()
    return {
        "french": ["Hello - Bonjour", "Thank you - Merci", "Please - S'il vous plaît"],
        "spanish": ["Hello - Hola", "Thank you - Gracias", "Please - Por favor"],
        "german": ["Hello - Hallo", "Thank you - Danke", "Please - Bitte"],
        "italian": ["Hello - Ciao", "Thank you - Grazie", "Please - Per favore"],
        "chainese": ["Hello - 你好 (Nǐ hǎo)", "Thank you - 谢谢 (Xièxiè)", "Please - 请 (Qǐng)"],
        "japanese": ["Hello - こんにちは (Konnichiwa)", "Thank you - ありがとう (Arigatō)", "Please - お願いします (Onegaishimasu)"],
        "irish": ["Hello - Dia dhuit", "Thank you - Go raibh maith agat", "Please - Le do thoil"],
        "swahili": ["Hello - Jambo", "Thank you - Asante", "Please - Tafadhali"]
    }.get(lang, ["Sorry, we don't have lessons for that language yet."])

def input_loop(prompt_text):
    text = ''
    while True:
        screen.fill(BG)
        screen.blit(font.render(prompt_text, True, WHITE), (50, 50))
        box = pygame.Rect(50, 100, 700, 50); pygame.draw.rect(screen, (0, 0, 0), box, 2)
        screen.blit(font.render(text, True, WHITE), (box.x + 10, box.y + 10))
        for e in pygame.event.get():
            if e.type == pygame.QUIT: pygame.quit(); sys.exit()
            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_RETURN: return text
                elif e.key == pygame.K_BACKSPACE: text = text[:-1]
                else: text += e.unicode
        pygame.display.update()

def main():
    fade(["Hello!", "This is an app where you can learn many languages.", "You can learn French, Spanish, German, Italian, and many more."])
    name = input_loop("What's your name?")
    fade([f"Hello {name}!", "Let's start learning."])
    
    for _ in range(3):
        lang = input_loop("Enter the language you want to learn:")
        phrases = [f"You have chosen to learn {lang}.", f"Great choice! Let's get started with some basics of {lang}.", f"Here are some common phrases in {lang}:"] + get_phrases(lang)
        fade(phrases)

    fade(["You can learn more languages in the next update.", "Stay tuned for more updates.", "Thank you for using LearnAllLang.Org", "Goodbye!"])

main()