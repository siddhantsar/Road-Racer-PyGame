import pygame

pygame.init()

display_width = 500
display_height = 600

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Road Race")

def car(x, y):
    gameDisplay.blit(carImg, (x, y))

carImg = pygame.image.load("car.png")
carWidth = 60
carHeight = 111

backgroundImg = pygame.image.load("road.png")
backgroundImg = pygame.transform.scale(backgroundImg, (display_width, display_height))

clock = pygame.time.Clock()

def game_loop():

    gameExit = False

    x = (display_width * 0.31)
    y = (display_height * 0.78)

    x_change = 0
    y_change = 0

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = +5
                elif event.key == pygame.K_UP:
                    y_change = -5
                elif event.key == pygame.K_DOWN:
                    y_change = +5
                
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    x_change = 0
                    y_change = 0

        x += x_change
        y += y_change
        gameDisplay.blit(backgroundImg, (0, 0))
        car(x, y)

        if x > ((display_width*0.8)- carWidth) or x < (display_width*0.20) or y > display_height - carHeight or y < 0:
            gameExit = True

        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
quit()