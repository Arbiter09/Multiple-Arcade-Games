import pygame, sys
from button import Button
import Pong
import Naruto_Game
import Snake

pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Arcade Games")

BG = pygame.image.load("assets/Background.png")

def get_font(size): 
    return pygame.font.Font("assets/font.ttf", size)

def play():
   Pong.game()
        
def naruto():
    Naruto_Game.Naruto()
def Snnake():
    Snake.snake()
def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("ARCADE GAMES", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 250), 
                            text_input="PONG", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        Naruto_Button = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 400), 
                            text_input="Naruto", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        Snake_button = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 550), 
                            text_input="Snake", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, Naruto_Button, Snake_button]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if Naruto_Button.checkForInput(MENU_MOUSE_POS):
                    naruto()
                if Snake_button.checkForInput(MENU_MOUSE_POS):
                    Snnake()

        pygame.display.update()

main_menu()