import pygame
import time
import random

pygame.init()

w_width = 500
w_height = 500
window = pygame.display.set_mode((w_width,w_height))
pygame.display.set_caption("Car Race")

#game variables
clock = pygame.time.Clock()
font = pygame.font.SysFont("helvetica", 50,1,1)
font2 = pygame.font.SysFont("helvetica", 20,1,1)
bg_speed = 5
score = 0
lvl = 1
next_lvl = 5
run = True

#importing images
carImage = pygame.image.load("CarRaceGame/img/car1.png")
grass = pygame.image.load("CarRaceGame/img/grass.jpg")
yellow_line = pygame.image.load("CarRaceGame/img/yellow_line.jpg")
white_line = pygame.image.load("CarRaceGame/img/white_line.jpg")
enemy_car_image = [pygame.image.load("CarRaceGame/img/car2.png"),pygame.image.load("CarRaceGame/img/car3.png")]
bg = pygame.image.load("CarRaceGame/img/bg.jpeg")
bg = pygame.transform.scale(bg,(w_width,w_height))

#displaying text on screen
def text_display(score,lvl):
    score_text = font2.render("Score: "+str(score),1,"black")
    window.blit(score_text,(0,0))
    level_text = font2.render("Level: "+str(lvl),1,"black")
    window.blit(level_text,(w_width-level_text.get_width(),0))

#font for buttons
font3 = pygame.font.SysFont(None, 30)

class Button():
    def __init__(self,x,y,width,height,text,action):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = pygame.Rect(x,y,width,height)
        self.text = text
        self.action = action
        self.is_hovered = False

    def draw(self):
        if self.is_hovered:
            pygame.draw.rect(window,"gray",self.rect)
        else:
            pygame.draw.rect(window,"white",self.rect)

        pygame.draw.rect(window,"black",self.rect,3)
        text_surface = font3.render(self.text,True,"black")
        text_rect = text_surface.get_rect(center = self.rect.center)
        window.blit(text_surface,text_rect)

    def perform_action(self):
        self.action()

    def check_hover(self,mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            self.is_hovered = True
        else:
            self.is_hovered = False


#start game function
def start_game():


    class Car():
        def __init__(self,x,y,img):
            self.x = x
            self.y = y
            self.width = 28
            self.height = 54
            self.vel = 3
            self.img = img

        def draw(self,window):
            window.blit(self.img, (self.x,self.y))

    #enemy car class
    class EnemyCar(Car):
        def __init__(self,x,y,img):
            self.x = x
            self.y = y
            self.width = 28
            self.height = 69
            self.vel = 2
            self.img = img

        def move(self):
            self.y += self.vel

        def draw(self,window,enemy_cars):
            for enemy_car in enemy_cars:
                if enemy_car != self:
                    if( self.y + self.height >= enemy_car.y
                       and self.y <= enemy_car.y + enemy_car.height
                       and self.x + self.width >= enemy_car.x
                       and self.x <= enemy_car.x + enemy_car.width):
                        return #skip drawing if collision
            window.blit(self.img, (self.x,self.y))

    #enemy car list
    enemy_cars = []
    for i in range(3):
        x = random.randint(100,400-28)
        y = random.randint(-500,-50)
        img = random.choice(enemy_car_image)
        enemy_car = EnemyCar(x,y,img)
        enemy_cars.append(enemy_car)

    #drawing background images
    def drawing_background():
        #calculate  the y position for each background element based on the scrolling speed 
        bg_y = pygame.time.get_ticks() // bg_speed

        #drawing background elements at thier corresponding positions
        window.blit(grass, (0,bg_y % w_height - w_height))
        window.blit(grass, (420,bg_y % w_height - w_height))
        window.blit(white_line, (90,bg_y % w_height - w_height))
        window.blit(white_line, (405,bg_y % w_height - w_height))
        window.blit(yellow_line, (225,bg_y % w_height - w_height))
        window.blit(yellow_line, (225,(bg_y + 100) % w_height - w_height))
        window.blit(yellow_line, (225,(bg_y + 200) % w_height - w_height))
        window.blit(yellow_line, (225,(bg_y + 300) % w_height - w_height))
        window.blit(yellow_line, (225,(bg_y + 400) % w_height - w_height))

        #drawing background elements for bottom part
        window.blit(grass, (0,bg_y % w_height))
        window.blit(grass, (420,bg_y % w_height))
        window.blit(white_line, (90,bg_y % w_height))
        window.blit(white_line, (405,bg_y % w_height))
        window.blit(yellow_line, (225,bg_y % w_height))
        window.blit(yellow_line, (225,(bg_y + 100) % w_height))
        window.blit(yellow_line, (225,(bg_y + 200) % w_height))
        window.blit(yellow_line, (225,(bg_y + 300) % w_height))
        window.blit(yellow_line, (225,(bg_y + 400) % w_height))

    #drawing on window surface 
    def DrawInGameLoop():
        clock.tick(60)
        window.fill((136,134,134))
        drawing_background()
        maincar.draw(window)

        #drawing enemy cars
        for enemy_car in enemy_cars:
            enemy_car.draw(window,enemy_cars)
        
        text_display(score,lvl)
        pygame.display.flip()

    #creating objects
    maincar = Car(250,250,carImage)

    #adding crash condition
    def crash():
        global run,score,lvl,next_lvl,bg_speed

        text = font.render("CAR CRASHED", 1,"black")
        window.blit(text, (95,250))
        pygame.display.flip()
        time.sleep(2)

        score = 0
        lvl = 1
        next_lvl = 5
        bg_speed = 5

        #reset position of main car
        maincar.x = 250
        maincar.y = 250

        #resset the position of all enemy cars
        for enemy_car in enemy_cars:
            enemy_car.x = random.randint(100,400-28)
            enemy_car.y = random.randint(-500,-50)
            enemy_car.img = random.choice(enemy_car_image)
            enemy_car.vel = 2 

        game_loop()

    #game loop
    def game_loop():
        global run,score,lvl,next_lvl,bg_speed


        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            if maincar.x < 100 or maincar.x > 400 - maincar.width:
                crash()

            #adding difficulty levels
            if score >= next_lvl:
                lvl += 1
                next_lvl += 5
                if bg_speed > 1:
                    bg_speed -= 1
                else:
                    bg_speed = 1

            keys = pygame.key.get_pressed()

            if keys[pygame.K_LEFT] and maincar.x > 0:
                maincar.x -= maincar.vel
            
            elif keys[pygame.K_RIGHT] and maincar.x < w_width - maincar.width:
                maincar.x += maincar.vel
            
            if keys[pygame.K_UP] and maincar.y > 0:
                maincar.y -= maincar.vel

            elif keys[pygame.K_DOWN] and maincar.y < w_height - maincar.height:
                maincar.y += maincar.vel

            for enemy_car in enemy_cars:
                enemy_car.move()

                #check for collision with main car
                if (enemy_car.x < maincar.x + maincar.width and enemy_car.x + enemy_car.width > maincar.x and enemy_car.y < maincar.y + maincar.height and enemy_car.y + enemy_car.height > maincar.y):
                    crash()

                #if enemy car goes off the screen, reset its position
                if enemy_car.y > w_height:
                    enemy_car.x = random.randint(100,400-28)
                    enemy_car.y = random.randint(-500,-50)
                    enemy_car.img = random.choice(enemy_car_image)
                    enemy_car.vel = 2
                    score += 1

            DrawInGameLoop()

    game_loop()
    pygame.quit()

#quit game function
def quit_game():
    pygame.quit()

#create function
start_button = Button(200,200,100,100,"Start",start_game)
quit_button = Button(200,320,100,100,"Quit",quit_game)

#menu loop
menu = True
while menu:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if start_button.rect.collidepoint(mouse_pos):
                start_button.perform_action()
            elif quit_button.rect.collidepoint(mouse_pos):
                quit_button.perform_action()
        elif event.type == pygame.MOUSEMOTION:
            mouse_pos = pygame.mouse.get_pos()
            start_button.check_hover(mouse_pos)
            quit_button.check_hover(mouse_pos)
            
    

    window.blit(bg,(0,0))

    start_button.draw()
    quit_button.draw()

    pygame.display.flip()