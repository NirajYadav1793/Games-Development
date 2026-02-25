import pygame
import time

pygame.init()

w_width = 500
w_height = 500
window = pygame.display.set_mode((w_width,w_height))
pygame.display.set_caption("Car Race")

#game variables
clock = pygame.time.Clock()
font = pygame.font.SysFont("helvetica", 50,1,1)

#importing images
carImage = pygame.image.load("CarRaceGame/img/car1.png")
grass = pygame.image.load("CarRaceGame/img/grass.jpg")
yellow_line = pygame.image.load("CarRaceGame/img/yellow_line.jpg")
white_line = pygame.image.load("CarRaceGame/img/white_line.jpg")

class car():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.width = 28
        self.height = 54
        self.vel = 4

    def draw(self,window):
        window.blit(carImage, (self.x,self.y))

#drawing background images
def drawing_background():
    window.blit(grass, (0,0))
    window.blit(grass, (420,0))
    window.blit(white_line, (90,0))
    window.blit(white_line, (405,0))
    window.blit(yellow_line, (225,0))
    window.blit(yellow_line, (225,100))
    window.blit(yellow_line, (225,200))
    window.blit(yellow_line, (225,300))
    window.blit(yellow_line, (225,400))

#drawing on window surface 
def DrawInGameLoop():
    clock.tick(60)
    window.fill((136,134,134))
    drawing_background()
    maincar.draw(window)
    pygame.display.flip()

#creating objects
maincar = car(250,250)

#adding crash condition
def crash():
    text = font.render("CAR CRASHED", 1,"black")
    window.blit(text, (95,250))
    pygame.display.flip()
    time.sleep(2)
    maincar.x = 250
    maincar.y = 250
    game_loop()

#game loop
run = True
def game_loop():
    global run


    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        if maincar.x < 100 or maincar.x > 400 - maincar.width:
            crash()

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and maincar.x > 0:
            maincar.x -= maincar.vel
        
        elif keys[pygame.K_RIGHT] and maincar.x < w_width - maincar.width:
            maincar.x += maincar.vel
        
        if keys[pygame.K_UP] and maincar.y > 0:
            maincar.y -= maincar.vel

        elif keys[pygame.K_DOWN] and maincar.y < w_height - maincar.height:
            maincar.y += maincar.vel

        DrawInGameLoop()

game_loop()
pygame.quit()
