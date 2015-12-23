import pygame,time
import math,random
class radargui:

    def __init__(self,step=48,width=800,height = 600,linecolor = (255, 0, 0),bgcolor = (0, 0, 0)):

        self.running = 1
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        self.linecolor = linecolor
        self.bgcolor = bgcolor
        self.step = step
        self.i = 0
    def biradim(self,dist):
        if self.i == self.step:
            self.i = 0
            self.screen.fill((0, 0, 0))
        derece = 360/self.step*self.i
        pygame.draw.line(self.screen, self.linecolor, (self.width/2, self.height/2), (self.width/2+ (dist*math.cos(derece)), (self.height/2+dist*math.sin(derece))))
        pygame.display.flip()
        self.i = self.i + 1
        time.sleep(0.2)
            
radar = radargui()
while 1:
    radar.biradim(random.randint(0,500))
    
