import pygame, sys

# PyGame primarily has  2 sections 
    # Setup section (game logic and data) and a 
    # Loop section (continually drawing and updating what's onscreen)
# sys is being used to close the game here

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

# define horizontal and vertical speed for ball
ballSpeedX = 17
ballSpeedY = 17

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
    
    # we want the ball to move every frame by the ball speed we've defined
    ball.x += ballSpeedX
    ball.y += ballSpeedY

    # collissions with ends of screen
        # <= and >= are more useful than == here because px movement each cycle may not be strictly equal
    if ball.top <= 0 or ball.bottom >= screenHeight:
        ballSpeedY *= -1
    if ball.left <= 0 or ball.right >= screenWidth:
        ballSpeedX *= -1

    # Visuals
        # note: these render in order, if you put screen.fill() at the bottom it's all you'd see
    screen.fill(bgColor)  # filling the display surface
    pygame.draw.rect(screen, lightGrey, player)
    pygame.draw.rect(screen, lightGrey, opponent)
    pygame.draw.ellipse(screen, lightGrey, ball)
    #aaline - anti alias line, takes display surface, color, start point, endpoint
    pygame.draw.aaline(screen, lightGrey, (screenWidth/2, 0), (screenWidth/2, screenHeight))

    # update the window
    pygame.display.flip()  # flip takes everything that came before it in the loop and draws it
    clock.tick(60)  # limits how fast loop runs (60 FPS)
    # computer will try to run code as fast as it can, so controlling the tick is important