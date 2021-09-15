import pygameGUI as pg
import json
import pygame
import os

class game_object:
    def __init__(self):
        self.width = 600
        self.height = 300

        self.screenManager = pg.screen_manager()

        self.FPS = pygame.time.Clock()

    def set_screen_size(self,w,h):
        self.width = w
        self.height = h

    def update(self):
        pass

        
def initialize_game():
    os.environ['SDL_VIDEO_WINDOW_POS'] = "5,30"
    pygame.init()
    
    GO = game_object()
    GO.FPS = pygame.time.Clock()
    
    # Build game screens
    intro_screen = pg.screen("intro",0,0,784,947)
    intro_screen.set_BG(pygame.image.load("art\DetailBox.png"))
    
    GO.screenManager.add_screen(intro_screen)

    exit_button = pg.panel(75,76,pygame.image.load("art\Exit button.png"))
    exit_button.place(693,12,intro_screen)

    BG = pygame.image.load("art\ButtonBG1.png")
    label = pygame.image.load("art\ConfirmLabel.png")
    confirm = pg.button(217,217,BG,BG,label,confirmLMB)
    confirm.place(100,100,intro_screen)
    
    BG = pygame.image.load("art\ButtonBG1.png")
    label = pygame.image.load("art\CancelLabel.png")
    cancel = pg.button(217,217,BG,BG,label,cancelLMB)
    cancel.place(350,100,intro_screen)

    return(GO)

def update_game():
    GO.update()
    GO.screenManager.update()

def draw_game():
    GO.screenManager.draw()
    pygame.display.flip()

def quit_nicely():
    pygame.display.quit()
    pygame.quit()

def confirmLMB():
    print("confirmed")

def cancelLMB():
    print("cancelled")
    
def game_main_loop():
    game_quit = False
    LMB_down = False
    RMB_down = False
    Simul_down = False
    L_click = None
    R_click = None
    Simul_click = None
    click_x = None
    click_y = None
    down_x = None
    down_y = None
    
    while not game_quit:
        event_list = pygame.event.get()
        for event in event_list:
            if event.type == pygame.QUIT:
                game_quit = True
                                      
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    LMB_down = True
                    down_x,down_y = event.pos
                elif event.button == 3:
                    RMB_down = True
                    down_x,down_y = event.pos
            if event.type == pygame.MOUSEBUTTONUP:
                click_x,click_y = event.pos
                if event.button == 1:
                    if RMB_down:
                        Simul_click = True
                    else:
                        L_click = True
                    LMB_down = False
                elif event.button == 3:
                    if LMB_down:
                        Simul_click = True
                    else:
                        R_click = True
                    RMB_down = False

                else:
                    print("Mouse button {}".format(event.button))
                
        if LMB_down:
            GO.screenManager.screens[GO.screenManager.active_screen].is_pressed(down_x,down_y,"LEFT")
                
        if RMB_down:
            GO.screenManager.screens[GO.screenManager.active_screen].is_pressed(down_x,down_y,"RIGHT")

        if L_click:
            GO.screenManager.screens[GO.screenManager.active_screen].is_clicked(click_x,click_y,"LEFT")
            L_click = False
                
        if R_click:
            GO.screenManager.screens[GO.screenManager.active_screen].is_clicked(click_x,click_y,"RIGHT")
            R_click = False
            
        if Simul_click:
            GO.screenManager.screens[GO.screenManager.active_screen].is_clicked(click_x,click_y,"BOTH")
            Simul_click = False
                

        update_game()
        draw_game()
        GO.FPS.tick(60)
    quit_nicely()
        
if __name__ == "__main__":
    GO = initialize_game()
    game_main_loop()
