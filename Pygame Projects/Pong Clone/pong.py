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

    # update the window
    pygame.display.flip()  # flip takes everything that came before it in the loop and draws it
    clock.tick(60)  # limits how fast loop runs (60 FPS)
    # computer will try to run code as fast as it can, so controlling the tick is important