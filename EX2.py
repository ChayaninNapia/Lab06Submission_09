import sys
import pygame as pg

class Rectangle:
    def __init__(self,x=0,y=0,w=0,h=0):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = (71, 211, 169 )

    def draw(self,screen):
        pg.draw.rect(screen,self.color,(self.x,self.y,self.w,self.h))

class Button(Rectangle):
    def __init__(self, x=0, y=0, w=0, h=0):
        Rectangle.__init__(self,x,y,w,h)
    
    def MouseIsOn(self):
        if (pg.mouse.get_pos()[0] > self.x and pg.mouse.get_pos()[0] < self.x+self.w) and (pg.mouse.get_pos()[1] > self.y and pg.mouse.get_pos()[1] < self.y+self.h):
            return True
        else:
            self.color = (71, 211, 169)
            return False

    def MouseIsPressed(self):
        if pg.mouse.get_pressed()[0]:
            return True
        else:
            return False

pg.init()
run = True
win_x,win_y = 800,480
screen = pg.display.set_mode((win_x,win_y))
obj_1 = Rectangle(120,300,100,100)
btn = Button(20,20,50,50)
color = (71, 211, 169 )

# Create font object and set size
font = pg.font.Font(None, 36)

while(run):
    screen.fill((255, 255, 255))
   
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            
        # if event.type == pg.KEYDOWN and event.key == pg.K_w: 
        #     btn.y -= 1
        # if event.type == pg.KEYDOWN and event.key == pg.K_a: 
        #     btn.x -= 1
        # if event.type == pg.KEYDOWN and event.key == pg.K_s: 
        #     btn.y += 1
        # if event.type == pg.KEYDOWN and event.key == pg.K_d: 
        #     btn.x += 1
    keys = pg.key.get_pressed()
    if keys[pg.K_w] and btn.y > 0:
        btn.y -= 1
    if keys[pg.K_a] and btn.x > 0:
        btn.x -= 1
    if keys[pg.K_s] and btn.y+btn.h < 480:
        btn.y += 1
    if keys[pg.K_d] and btn.x+btn.w < 800:
        btn.x += 1

    if btn.MouseIsOn() and not btn.MouseIsPressed():
        btn.color = (113, 116, 125)
    elif btn.MouseIsOn() and btn.MouseIsPressed():
        btn.color = (127, 46, 217 )
    else:
        btn.color = (217, 46, 56)
    btn.draw(screen)
    pg.display.update()

