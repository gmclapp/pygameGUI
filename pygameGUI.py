import pygame
import os

class screen:
    def __init__(self, name, x=0, y=0,wid=100,hei=100):
        self.buttons = []
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

    def add_button(self,new_button):
        self.buttons.append(new_button)

    def remove_button(self,button):
        self.buttons.remove(button)
        
    def make_active(self):
        GO.change_active_screen(self.name)

class panel:
    pass
class button(panel):
    pass
class radio_button_manager():
    pass
class radio_button(button):
    pass
class indicator(panel):
    pass
