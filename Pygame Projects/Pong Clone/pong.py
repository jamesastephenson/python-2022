import pygame, sys, random

# PyGame primarily has  2 sections 
    # Setup section (game logic and data) and a 
    # Loop section (continually drawing and updating what's onscreen)
# sys is being used to close the game here

# function for our ball speed and collisions
def ballAnimation():
    # account for global scope (this is only a good solution in small programs)
        # better to use return statements or classes
    global ballSpeedX, ballSpeedY, ballColor, cyan, orange, playerScore, opponentScore

    # we want the ball to move every frame by the ball speed we've defined
    ball.x += ballSpeedX
    ball.y += ballSpeedY

    # collissions with ends of screen
        # <= and >= are more useful than == here because px movement each cycle may not be strictly equal
    if ball.top <= 0 or ball.bottom >= screenHeight:
        ballSpeedY *= -1
    if ball.left <= 0:
        playerScore += 1
        ballRestart()
    elif ball.right >= screenWidth:
        opponentScore += 1
        ballRestart()

    # rect1.colliderect(rect2) - if they collide, it returns true
    if ball.colliderect(player):
        ballSpeedX *= -1 
        ballColor = cyan
    elif ball.colliderect(opponent):
        ballSpeedX *= -1 
        ballColor = orange

def playerAnimation():
    player.y += playerSpeed
    if player.top <=0:
        player.top = 0
    if player.bottom >= screenHeight:
        player.bottom = screenHeight

def opponentAnimation():
    if opponent.top < ball.y:
        opponent.top += opponentSpeed
    if opponent.bottom > ball.y:
        opponent.bottom -= opponentSpeed

    if opponent.top <=0:
        opponent.top = 0
    if opponent.bottom >= screenHeight:
        opponent.bottom = screenHeight

# reset ball position after player scores
def ballRestart():
    global ballSpeedX, ballSpeedY
    ball.center = (screenWidth / 2, screenHeight / 2)
    # random.choice returns a random value from the tuple passed into it
        # randomizes direction
    ballSpeedY *= random.choice((1,-1))
    ballSpeedX *= random.choice((1,-1))
        
# init() initiates all pygame modules (required for all pygame uses)
pygame.init()
# storing clock method in a variable
clock = pygame.time.Clock()

# Set up the window
screenWidth = 1600
screenHeight = 800
# display method controls the display window and screen
    # set_mode initializes the window
        # we're only passing in width and height since this is a simple game
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption('Pong')

# Drawing
# Display Surface - basic element, main screen we draw on (can only be a single one)
    # can draw directly on the surface with pygame.draw
# (Regular) Surface - Extra surface that holds material, can have as many as you want
    # regular surfaces must be attached to the display surface
# Rect - rectangle, you can put it around shapes and regular surfaces
    # makes it easier to measure and manipulate regular surfaces
    # origin of rectangle is top left, so you have to increase to move right and down

# Game Rectangles
    # pygame.Rect(startPosX, startPosY, rectWidth, rectHeight)
# startPos's are finding the screen midpoint and subtracting half our rect width
    # this is because of where the rectangle origin starts
ball = pygame.Rect(screenWidth/2 - 15, screenHeight/2 - 15, 30, 30) 
player = pygame.Rect(screenWidth - 20, screenHeight/2 - 70, 10, 140) # note, start height is half of our rect height
opponent = pygame.Rect(10, screenHeight/2 - 70, 10, 140)

# Drawing
# pygame.draw(surface, color, rect)
    # here surface will be our screen var, rect will be the vars we devined above
# pygame.draw() can use rgb colors or a string of a color name
bgColor = pygame.Color('grey12')
lightGrey = (200, 200, 200)
cyan = (126, 230, 210)
orange = (249, 174, 60)
ballColor = lightGrey

# define horizontal and vertical speed for ball
ballSpeedX = 13 * random.choice((1,-1))
ballSpeedY = 13 * random.choice((1,-1))
playerSpeed = 0
opponentSpeed = 11

# Text Variables
playerScore = 0
opponentScore = 0
gameFont = pygame.font.Font("freesansbold.ttf", 40) #calling pygame font method and size


# Loop Section
while True:
    # handle input
    # every cycle we get a list of user inputs with pygame.event.get()
        # event - any user action in pygame
    for event in pygame.event.get():
        # check if the user has clicked the X to close (pygame.QUIT)
        if event.type == pygame.QUIT:
            # these two combined reliably close the game
            pygame.quit()  # uninitializes Python module
            sys.exit()  # closes the window
        # pygame.KEYDOWN only checks if a key has been pressed, we need another if for specific keys
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN: # down arrow key
                # decalre player speed variable
                # add this speed to the player on every frame
                # no button pressed: speed = 0
                # button pressed: speed becomes positive or negative
                playerSpeed += 7
            if event.key == pygame.K_UP:
                playerSpeed -= 7
        if event.type == pygame.K_UP:
            if event.key == pygame.K_DOWN:
                playerSpeed -= 7
            if event.key == pygame.K_UP:
                playerSpeed += 7
    
    ballAnimation()
    playerAnimation()
    opponentAnimation() 

    

    # Visuals
        # note: these render in order, if you put screen.fill() at the bottom it's all you'd see
    screen.fill(bgColor)  # filling the display surface
    pygame.draw.rect(screen, cyan, player)
    pygame.draw.rect(screen, orange, opponent)
    pygame.draw.ellipse(screen, ballColor, ball)
    #aaline - anti alias line, takes display surface, color, start point, endpoint
    pygame.draw.aaline(screen, lightGrey, (screenWidth/2, 0), (screenWidth/2, screenHeight))

    # Text Display
    # render method takes the text itself, whether it's antialiase, and color as arguments
    playerText = gameFont.render(f"{playerScore}", False, cyan)
    #screen.blit() draws the text, takes the text variable and its position as arguments
    screen.blit(playerText, (860,400))
    opponentText = gameFont.render(f"{opponentScore}", False, orange)
    screen.blit(opponentText, (710, 400))

    # update the window
    pygame.display.flip()  # flip takes everything that came before it in the loop and draws it
    clock.tick(60)  # limits how fast loop runs (60 FPS)
    # computer will try to run code as fast as it can, so controlling the tick is important



# To make text in pygame
    # create a font (and font size)
    # write text on new surface
    # put text surface on the main surface