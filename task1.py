import pygame
pygame.init()
screen=pygame.display.set_mode((700,500))
screenrect = screen.get_rect()

clock = pygame.time.Clock()
running = True
FPS = 30

background = pygame.Surface(screen.get_size())
background.fill((255,255,255))     
background = background.convert()
screen.blit(background, (0,0))     

ballsurface = pygame.Surface((50,50))    
ballsurface.set_colorkey((0,0,0))        

pygame.draw.circle(ballsurface, (255,0,0), (25,25),25)
ballsurface = ballsurface.convert_alpha()       
ballrect = ballsurface.get_rect() 
ballx, bally = 250, 300           
dx = 20                        
dy = 20                 

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False 
            elif event.key == pygame.K_UP:
                bally -= 20
            elif event.key == pygame.K_DOWN:
                bally += 20
            elif event.key == pygame.K_RIGHT:
                ballx += 20
            elif event.key == pygame.K_LEFT:
                ballx -= 20
    screen.blit(background, (0,0)) 
    pygame.display.set_caption("X: {0:.1f}, Y: {1:.2f}".format(ballx, bally))
    if ballx < 0: 
        ballx = 0
        dx *= -1 
    elif ballx + ballrect.width > screenrect.width:
        ballx = screenrect.width - ballrect.width
        dx *= -1
   
    if bally < 0: 
        bally = 0
        dy *= -1 
    elif bally + ballrect.height > screenrect.height:
        bally = screenrect.height - ballrect.height
        dy *= -1 
    screen.blit(ballsurface, (round(ballx,0), round(bally,0))) 
    pygame.display.flip()  