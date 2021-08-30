import pygame
import os

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
            e.is_pressed(x,y)

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
        self.wid = wid
        self.hei = hei

        self.art = art

    def place(self,x,y,screen):
        self.x = x
        self.y = y
        self.screen = screen
        screen.add_element(self)

    def update(self):
        pass
    def draw(self):
        if self.active:
            self.screen.surf.blit(self.art,(self.x,self.y))
            
class button(panel):
    pass
class radio_button_manager():
    pass
class radio_button(button):
    pass
class indicator(panel):
    pass
