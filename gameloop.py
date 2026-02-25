import pygame

pygame.init()

w_width = 500
w_height = 500
window = pygame.display.set_mode((w_width,w_height))
pygame.display.set_caption("Car Race")

#game variables
clock = pygame.time.Clock()

#drawing on window surface 
def DrawInGameLoop():
    clock.tick(60)
    window.fill("gray")
    pygame.display.flip()

#game loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    DrawInGameLoop()

pygame.quit()