import pygame as pg
class Rectangle:
    def __init__(self,x=0,y=0,w=0,h=0,color = (174, 90, 11)):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color
        self.width = 0
        self.rect = pg.Rect(x,y,w,h)

    def draw(self,Screen,W=None):
        if W == None:
            W = self.width
        pg.draw.rect(Screen,self.color,(self.x,self.y,self.w,self.h),W)

class Button(Rectangle):
    def __init__(self,x=0,y=0,w=0,h=0):
        Rectangle.__init__(self,x,y,w,h)

    def is_pressed(self,event):
        if event.type == pg.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                return True
            else:
                return False
    # def is_on(self,event):
        


class CheckBox(Rectangle):
    def __init__(self,x=0,y=0,w=0,h=0):
        Rectangle.__init__(self,x,y,w,h)   
        self.status = False
        self.color = (217, 46, 79)
    def draw(self,Screen):
        if self.status:
            self.color = (46, 217, 99)
        else:
            self.color = (217, 46, 79)
        # pg.draw.rect(Screen,self.color,(self.x,self.y,self.w,self.h))
        super().draw(Screen)

class TextBox():
    def __init__(self, x=0, y=0,text = "",textSize = 20,textColor = (255,255,255),font = None):
        self.x = x
        self.y = y
        self.text = text
        self.textSize = textSize
        self.font = font
        self.textColor = textColor
        self.lenght = pg.font.Font(self.font, self.textSize).render(self.text, True,self.textColor).get_rect()[2]
    def draw(self,Screen):
        Font = pg.font.Font(self.font, self.textSize)
        text_surface = Font.render(self.text, True,self.textColor)
        text_rect = text_surface.get_rect()
        text_rect.topleft = (self.x, self.y)
        Screen.blit(text_surface, text_rect)

class InputButton(Rectangle):
    def __init__(self,x=0,y=0,w=0,h=0):
        super().__init__(x,y,w,h)
        # self.rect = pg.Rect(x,y,w,h)
        self.text = ""
        self.color = (0,0,0)
        self.txt_surface = FONT.render(self.text,True,self.color)
        self.active = False
    def Check_event(self,event):
        if event.type == pg.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
        self.color = (127, 46, 217) if self.active else (0,0,0) 
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    print(self.text)
                    box1.color = (46, 217, 99 )
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode

                self.txt_surface = FONT.render(self.text, True, (255,255,255))

    def update(self):
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width
    def draw(self,Screen):
        # Blit the text.
        Screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pg.draw.rect(Screen, self.color, self.rect, 2)

def has_digit(s):
    return any(char.isdigit() for char in s)    




pg.init()
win_x,win_y = 800,480
screen = pg.display.set_mode((win_x,win_y))
run = True
FONT = pg.font.Font(None, 32)
ruleCheck = 0
ruleNum = 0
caution = [
    "Incorrect FirstName",
    "Incorrect LastName",
    "Incorrect Age"
]

input1 = InputButton(20,50,100,32)
input2 = InputButton(20,130,100,32)
input3 = InputButton(20,210,100,32)

submit = Button(20,290,100,32)

txt1 = TextBox(20,20,"FirstName",30)
txt2 = TextBox(20,100,"LastName",30)
txt3 = TextBox(20,180,"Age",30)
txt4 = TextBox(35,300,"submit",30)
output1 = TextBox(20,340,"",30)
output2 = TextBox(20,380,"",30)
output3 = TextBox(20,420,"",30)
txt4.textColor = (255,255,255)


box1 = CheckBox(txt1.lenght+30,20,20,20)
box2 = CheckBox(txt1.lenght+30,100,20,20)
box3 = CheckBox(txt1.lenght+30,180,20,20)

cbox = [box1,box2,box3]
box = [txt1,txt2,txt3,txt4]
output = [output1,output2,output3]
inbox = [input1,input2,input3]


while(run):

    screen.fill((61, 62, 62))
    submit.draw(screen)
    for i in box:
        i.draw(screen)
    for i in inbox:
        i.update()
        i.draw(screen)
    for i in range(len(cbox)):
        if inbox[i].text != "":
            cbox[i].status = True
            cbox[i].draw(screen)
        else:
            cbox[i].status = False
            cbox[i].draw(screen)
    for i in output:
        i.draw(screen)
    
    for event in pg.event.get():
        if submit.is_pressed(event):
            for i in output:
                i.text = ""
            print("submit!")
            for i in cbox:
                if i.status:
                    ruleCheck+=1
            
            if ruleCheck == len(cbox):
                if has_digit(input1.text):
                    print("BUG")
                    output[ruleNum].text = ""
                    output[ruleNum].text = caution[ruleNum]
                ruleNum+=1
                if has_digit(input2.text):
                    output[ruleNum].text = ""
                    output[ruleNum].text = caution[ruleNum]
                ruleNum+=1
                if not input3.text.isdigit():
                    output[ruleNum].text = ""
                    output[ruleNum].text = caution[ruleNum]
                if not has_digit(input1.text) and not has_digit(input2.text) and input3.text.isdigit():
                    for i in output:
                        i.text = ""
                    output1.text = F"Hello {input1.text} {input2.text}! You are {input3.text} years old."
                


            else:
                print("Incomplete Information!")
                output1.text = "Incomplete Information!"

            
        ruleNum = 0
        ruleCheck = 0
        for i in inbox:
            i.Check_event(event)
        if event.type == pg.QUIT:
            pg.quit()
            run = False
    
    pg.display.update()