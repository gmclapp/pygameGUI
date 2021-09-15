import pygame
import os

class screen_manager:
    def __init__(self):
        self.screens = {}
        self.active_screen = None

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
        self.screens[self.active_screen].draw()
        
class screen:
    def __init__(self, name, x=0, y=0,wid=100,hei=100):
        self.elements = []
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

    def remove_button(self,element):
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
    pass
class radio_button(button):
    pass
class indicator(panel):
    pass
