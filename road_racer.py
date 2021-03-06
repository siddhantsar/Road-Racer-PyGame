import pygame, time, random

pygame.init()

display_width = 500
display_height = 600

blue = (34, 100, 255)
black = (0, 0, 0)

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Road Race")

traffic1 = pygame.image.load("traffic-1.png")
traffic2 = pygame.image.load("traffic-2.png")
traffic3 = pygame.image.load("traffic-3.png")
traffic4 = pygame.image.load("traffic-4.png")
traffic5 = pygame.image.load("traffic-5.png")



def cars_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Score: " + str(count), True, black)
    gameDisplay.blit(text, (0, display_height-20))

def traffic(traffic_image, traffic_x, traffic_y):
    gameDisplay.blit(traffic_image, (traffic_x, traffic_y))

traffic_list = [traffic1, traffic2, traffic3, traffic4, traffic5]
traffic_image = traffic_list[random.randint(0, 4)]
def text_objects(text, font):
    textSurface = font.render(text, True, blue)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font("font/font-style.ttf", 50)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2), (display_height/3.5))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(2)

    game_loop()

def crash():
    message_display("You crashed!")

def car(x, y):
    gameDisplay.blit(carImg, (x, y))

carImg = pygame.image.load("car.png")
carWidth = 50
carHeight = 111

backgroundImg = pygame.image.load("road.png")
backgroundImg = pygame.transform.scale(backgroundImg, (display_width, display_height))

clock = pygame.time.Clock()

def game_loop():

    gameExit = False

    x = (display_width * 0.31)
    y = (display_height * 0.78)

    x_change = 0

    traffic_width = 50
    traffic_height = 105
    traffic_start_x = random.randrange(display_width*0.2, display_width*0.8 - traffic_width)
    traffic_start_y = -500
    traffic_speed = 7

    count = 0

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = +5
                
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    x_change = 0

        x += x_change
        gameDisplay.blit(backgroundImg, (0, 0))

        traffic(traffic_image, traffic_start_x, traffic_start_y)
        traffic_start_y += traffic_speed

        car(x, y)
        cars_dodged(count)
        
        if x > ((display_width*0.8)- carWidth) or x < (display_width*0.20) or y > display_height - carHeight or y < 0:
            crash()

        if traffic_start_y > display_height:
            traffic_start_y = 0 - traffic_height
            traffic_start_x = random.randrange(display_width*0.2, display_width*0.8 - traffic_width)
            count += 1
            if count % 5 == 0:
                traffic_speed += 2
        
        if y < traffic_start_y + traffic_height:
            if x > traffic_start_x and x < traffic_start_x + traffic_width or x + carWidth > traffic_start_x and x + carWidth < traffic_start_x + traffic_width:
                crash()

        pygame.display.update()
        clock.tick(120)

game_loop()
pygame.quit()
quit()