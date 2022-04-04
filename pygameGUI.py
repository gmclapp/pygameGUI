import pygame
import os

__version__ = 0.1

class screen_manager:
    def __init__(self):
        self.screens = {}
        self.active_screen = None
        self.SURFACE_MAIN = pygame.display.set_mode((1600,1000))

    def add_screen(self,new_screen):
        if len(self.screens)== 0:
            self.active_screen = new_screen.name
            
        self.screens[new_screen.name] = new_screen

    def change_active_screen(self,screen):
        if self.active_screen != screen:
            # Need to handle what happens when the requested screen doesn't exist.
            self.active_screen = screen
        else:
            pass

    def update(self):
        self.screens[self.active_screen].update()
        
    def draw(self):
        self.SURFACE_MAIN.fill((100,100,100))
        self.screens[self.active_screen].draw()
        self.SURFACE_MAIN.blit(self.screens[self.active_screen].surf,(0,0))
        
class screen:
    def __init__(self, name, x=0, y=0,wid=100,hei=100):
        self.elements = []
        self.active = False
        self.x = x
        self.y = y
        self.wid = wid
        self.hei = hei
        self.name = name
        self.surf = pygame.Surface((wid,hei),pygame.SRCALPHA,32)
        self.surf = self.surf.convert_alpha()

    def set_BG(self,background):
        self.BG = background

    def is_pressed(self,x,y,MB):
        '''processes x,y coordinates of a mouse button press and the mouse
        button used to generate it.'''
        for e in self.elements:
            e.is_pressed(x,y,MB)

    def is_clicked(self,x,y,MB):
        for e in self.elements:
            e.is_clicked(x,y,MB)

    def update(self):
        for e in self.elements:
            e.update()

    def draw(self):
        self.surf.blit(self.BG,(0,0))
        for e in self.elements:
            e.draw()

    def add_element(self,new_element):
        self.elements.append(new_element)

    def remove_element(self,element):
        self.elements.remove(element)
        
    def make_active(self):
        GO.change_active_screen(self.name)

class panel:
    def __init__(self,wid,hei,art):
        self.active = True
        self.pressed = False
        self.wid = wid
        self.hei = hei

        self.art = art

    def place(self,x,y,screen):
        self.x = x
        self.y = y
        self.screen = screen
        screen.add_element(self)

    def is_pressed(self, mx, my,MB):
        mx -= self.screen.x
        my -= self.screen.y
        if self.x < mx < self.x+self.wid and self.y < my < self.y+self.hei:
            if MB == "LEFT":
                self.pressed = True
        else:
            self.pressed = False

    def is_clicked(self,mx,my,MB):
        mx -= self.screen.x
        my -= self.screen.y
        if self.x < mx < self.x+self.wid and self.y < my < self.y+self.hei:
            if MB == "LEFT":
                self.clicked = True
            elif MB == "RIGHT":
                self.Rclicked = True
            elif MB == "BOTH":
                self.Simul_clicked = True
                
        else:
            self.clicked = False
            self.Rclicked = False
            self.Simul_clicked = False
            
    def update(self):
        pass
    def draw(self):
        if self.active:
            self.screen.surf.blit(self.art,(self.x,self.y))
            
class button(panel):
    def __init__(self,wid,hei,art,pressed_art,label_art,action=None,RMB_action=None,Simul_action=None):
        super().__init__(wid,hei,art)
        self.pressed = False
        self.clicked = False
        self.Rclicked = False
        self.Simul_clicked = False

        self.pressed_art = pressed_art
        self.label_art = label_art
        self.action = action
        self.RMB_action = RMB_action
        self.Simul_action = Simul_action

    def update(self):
        if self.clicked:
            if self.action:
                self.action()
            else:
                print("No action assigned to LMB.")
            self.clicked = False
            self.pressed = False
        if self.Rclicked:
            if self.RMB_action:
                self.RMB_action()
            else:
                print("No action assigned to RMB.")
            self.Rclicked = False
            self.pressed = False
        if self.Simul_clicked:
            if self.Simul_action:
                self.Simul_action()
            else:
                print("No action assigned to simultaneous click.")
                self.Simul_clicked = False
                self.pressed = False

    def draw(self):
        if self.pressed:
            self.screen.surf.blit(self.pressed_art,(self.x,self.y))
        else:
            self.screen.surf.blit(self.art,(self.x,self.y))
        if self.label_art:
            self.screen.surf.blit(self.label_art,(self.x,self.y))
            
class radio_button_manager():
    def __init__(self):
        self.var = 0 # Currently selected radio button
        self.buttons = []

    def add_button(self,button):
        button.index = len(self.buttons) # tell the button what its index is
        if button.index == 0:
            button.active = True
        self.buttons.append(button)
        button.manager = self

    def make_active(self,button_index):
        for i,b in enumerate(self.buttons):
            if i == button_index:
                b.active = True
                self.var = i
            else:
                b.active = False

    def get_var(self):
        return(self.var)
    
    def set_var(self,new):
        self.var = new
        for i,b in enumerate(self.buttons):
            if i == new:
                b.active = True
            else:
                b.active = False
            
    
class radio_button(button):
    def __init__(self,wid,hei,art,pressed_art,label_art,action=None,RMB_action=None,Simul_action=None,active_art=None):
        super().__init__(wid,hei,art,pressed_art,label_art,action,RMB_action,Simul_action)
        self.active_art = active_art
        self.active = False
        self.action = self.make_active
        
    def update(self):
        if self.clicked:
            if self.action:
                self.action()
                
            else:
                print("No action assigned to LMB.")
            self.clicked = False
            self.pressed = False
        if self.Rclicked:
            if self.RMB_action:
                self.RMB_action()
            else:
                print("No action assigned to RMB.")
            self.Rclicked = False
            self.pressed = False
        if self.Simul_clicked:
            if self.Simul_action:
                self.Simul_action()
            else:
                print("No action assigned to simultaneous click.")
                self.Simul_clicked = False
                self.pressed = False

    def make_active(self):
        self.manager.make_active(self.index)
                
    def draw(self):
        if self.pressed:
            self.screen.surf.blit(self.pressed_art,(self.x,self.y))
        else:
            self.screen.surf.blit(self.art,(self.x,self.y))
            
        if self.active:
            self.screen.surf.blit(self.active_art,(self.x,self.y))
        else:
            self.screen.surf.blit(self.label_art,(self.x,self.y))
            
class indicator(panel):
    pass
