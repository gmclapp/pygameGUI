import pygame
import constants
import os

class game_object:
    def __init__(self):
        self.width = 600
        self.height = 300
        self.screens = {}
        self.active_screen = "intro"
        self.FPS = pygame.time.Clock()
        self.SURFACE_MAIN = pygame.display.set_mode((self.width,
                                                     self.height))
        self.dialogs = {}

        
    def set_screen_size(self,w,h):
        self.width = w
        self.height = h
        
    def change_active_screen(self,screen):
        if self.active_screen != screen:
            self.active_screen = screen
        else:
            pass
        
    def add_screen(self,new_screen):
        key = new_screen.name
        val = new_screen
        
        self.screens[key] = val

    def update(self):
        pass

class screen:
    def __init__(self, name, x=0, y=0,
                 wid=constants.GAME_WIDTH,
                 hei=constants.GAME_HEIGHT):
        self.buttons = []
        self.sprites = []
        self.active = False
        self.x = x
        self.y = y
        self.wid = wid
        self.hei = hei
        self.name = name
        self.surf = pygame.Surface((wid,hei))

    def set_BG(self,background):
        self.BG = background

    def is_pressed(self,x,y,MB):
        '''processes x,y coordinates of a mouse button press and the mouse
        button used to generate it.'''
        for b in self.buttons:
            b.is_pressed(x,y)

    def is_clicked(self,x,y,MB):
        for b in self.buttons:
            b.is_clicked(x,y,MB)

    def update(self):
        for b in self.buttons:
            b.update()

    def draw(self):
        self.surf.blit(self.BG,(0,0))
        for b in self.buttons:
            b.draw()
        for s in self.sprites:
            s.draw()

    def add_button(self,new_button):
        self.buttons.append(new_button)

    def remove_button(self,button):
        self.buttons.remove(button)

    def add_sprite(self,new_sprite):
        self.sprites.append(new_sprite)

    def remove_sprite(self,sprite):
        self.sprites.remove(sprite)
        
    def make_active(self):
        GO.change_active_screen(self.name)
        
def initialize_game():
    os.environ['SDL_VIDEO_WINDOW_POS'] = "5,35"
    pygame.init()
    
    GO = game_object()
    GO.FPS = pygame.time.Clock()
    GO.SURFACE_MAIN = pygame.display.set_mode((constants.GAME_WIDTH,
                                               constants.GAME_HEIGHT))
    # Build game screens
    intro_screen = screen("intro",0,0,constants.GAME_WIDTH,constants.GAME_HEIGHT)
    # Set background art for screens and dialog boxes
    intro_screen.set_BG(constants.DEFAULT_BG)
    # Attach screens and dialog boxes to the game object
    GO.add_screen(intro_screen)
    
    return(GO)

def update_game():
    GO.update()
    GO.screens[GO.active_screen].update()

def draw_game():
    GO.screens[GO.active_screen].draw()
    
            
    GO.SURFACE_MAIN.blit(GO.screens[GO.active_screen].surf,
                         (0,0))
    pygame.display.flip()

def quit_nicely():
    pygame.display.quit()
    pygame.quit()
    
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

            if event.type == pygame.KEYDOWN and GO.dialogs["name"].active:
                if event.key == pygame.K_BACKSPACE:
                    GO.win_player.set(GO.win_player.get()[:-1])
                else:
                    GO.win_player.set(GO.win_player.get() + event.unicode)
                                      
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
            Dialog_active = False
            for Diag in GO.dialogs:
                if GO.dialogs[Diag].active:
                    Dialog_active = True
                    GO.dialogs[Diag].is_pressed(down_x,down_y,"LEFT")
            if not Dialog_active:
                GO.screens[GO.active_screen].is_pressed(down_x,down_y,"LEFT")
                
        if RMB_down:
            Dialog_active = False
            for Diag in GO.dialogs:
                if GO.dialogs[Diag].active:
                    Dialog_active = True
                    GO.dialogs[Diag].is_pressed(down_x,down_y,"RIGHT")
            if not Dialog_active:
                GO.screens[GO.active_screen].is_pressed(down_x,down_y,"RIGHT")

        if L_click:
            Dialog_active = False
            for Diag in GO.dialogs:
                if GO.dialogs[Diag].active:
                    Dialog_active = True
                    GO.dialogs[Diag].is_clicked(click_x,click_y,"LEFT")
            if not Dialog_active:
                GO.screens[GO.active_screen].is_clicked(click_x,click_y,"LEFT")
            L_click = False
                
        if R_click:
            Dialog_active = False
            for Diag in GO.dialogs:
                if GO.dialogs[Diag].active:
                    Dialog_active = True
                    GO.dialogs[Diag].is_clicked(click_x,click_y,"RIGHT")
            if not Dialog_active:
                GO.screens[GO.active_screen].is_clicked(click_x,click_y,"RIGHT")
            R_click = False
        if Simul_click:
            Dialog_active = False
            for Diag in GO.dialogs:
                if GO.dialogs[Diag].active:
                    Dialog_active = True
                    GO.dialogs[Diag].is_clicked(click_x,click_y,"BOTH")
            if not Dialog_active:
                GO.screens[GO.active_screen].is_clicked(click_x,click_y,"BOTH")
            Simul_click = False
                

        update_game()
        draw_game()
        GO.FPS.tick(60)
    quit_nicely()
        
if __name__ == "__main__":
    GO = initialize_game()
    game_main_loop()
