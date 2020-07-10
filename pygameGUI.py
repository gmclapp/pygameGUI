import pygame

class game_object:
    def __init__(self):
        self.width = 600
        self.height = 300
        self.screens = {}
        self.FPS = pygame.time.Clock()
        self.SURFACE_MAIN = pygame.display.set_mode((self.width,
                                                     self.height))

        
    def set_screen_size(self,w,h):
        self.width = w
        self.height = h
        
    def change_active_screen(self,screen):
        if self.active_screen != screen:
            self.active_screen = screen
        else:
            pass

class screen:
    def __init__(self, name,wid,hei):
        self.buttons = []
        self.active = False
        self.wid = wid
        self.hei = hei
        self.name = name
        self.surf = pygame.Surface((wid,hei))
        
def initialize_game():
    os.environ['SDL_VIDEO_WINDOW_POS'] = "5,35"
    pygame.init()
    
    GO = game_object()
    
    return(GO)
if __name__ == "__main__":
    GO = initialize_game()
    game_main_loop()
