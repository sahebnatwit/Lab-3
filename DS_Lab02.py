import pygame
pygame.init()
 
#Initializing the display window
size = (800,400)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("pong")
 
#Starting coordinates of the paddle
pad_x = 750
pad_y = 50
 
#speed of the ball
ballChange_x = 5
ballChange_y = 5
 
#initial position of the ball
ball_x = 60
ball_y = 60
 
 
#initial speed of the paddle
padChange_x = 1
padChange_y = 1

#draws the paddle. Also restricts its movement between the edges
#of the window.
def paddleClamp(screen,x,y):
    if y <= 10:
        y = 10
    if x >= 780:
        x = 780
    pygame.draw.rect(screen,"Blue",[x,y,20,100])
 
   
#game's main loop    
done = False
clock=pygame.time.Clock()
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                padChange_y = -6
            elif event.key == pygame.K_DOWN:
                padChange_y = 6        
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                padChange_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                padChange_y = 0            
   
    pad_x += padChange_x
    pad_y += padChange_y
   
    ball_x += ballChange_x
    ball_y += ballChange_y
   
    screen.fill("Black")
 
    #this handles the movement of the ball.
    if ball_x<10:
        ball_x=10
        ball_change_x = ball_change_x * -1
    elif ball_x>800:
        ball_x=800
        pygame(exit)
    elif ball_y<10:
        ball_y=10
        ballChange_y = ballChange_y * -1
#Ball Collision with paddle
    elif ball_x>pad_x and ball_y<pad_x+50 and ball_x==20:
        ballChange_y = ballChange_y * -1
    elif ball_y>390:
        ballChange_y = ballChange_y * -1
                       
    pygame.draw.rect(screen,"White",[ball_x,ball_y,15,15])
 
    WIDTH = 800
    HEIGHT = 600
    wcolor = pygame.Color("Purple")
    Border = 10
    paddleClamp(screen,pad_x,pad_y)
 
    pygame.draw.rect(screen, wcolor, pygame.Rect((0,0),(WIDTH,Border)))
    Thick = 10
    pygame.draw.rect(screen, wcolor, pygame.Rect((0,0),(Thick,HEIGHT)))
   
    pygame.draw.rect(screen, wcolor, pygame.Rect((0,390),(WIDTH,Border)))
   
    pygame.display.update()
   
    pygame.display.flip()        
    clock.tick(60)
   
pygame.quit()    

