#Neal Kaviratna
#Nkaviratna@gatech.edu
#I used the free textbook located at http://inventwithpython.com/makinggames.pdf
#requires installation of pygame module available at: http://pygame.org/download.shtml
#coded in python 2

#-----------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------
try:
    import pygame, sys, time
    from pygame.locals import *
except:
    print 'please install pygame to run program'
    sys.exit()
    
FPS = 30 #frames per second
WINDOWWIDTH = 189
WINDOWHEIGHT = 189
BOXSIZE = 53
BOXCORNERS = ( ((10, 10), (68, 10), (126, 10)), ((10, 68), (68, 68), (126, 68)), ((10, 126), (68, 126), (126, 126)) )

#             R    G    B
GRAY      = (100, 100, 100)
NAVYBLUE  = ( 60,  60, 100)
WHITE     = (255, 255, 255)
RED       = (255,   0,   0)
GREEN     = (  0, 255,   0)
BLUE      = (  0,   0, 255)
YELLOW    = (255, 255,   0)
ORANGE    = (255, 128,   0)
PURPLE    = (255,   0, 255)
CYAN      = (  0, 255, 255)

PLAYER1 = 'player1'
PLAYER2 = 'player2'


#-----------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------
# Main game run through
def main():
    activePlayer = PLAYER1
    global FPSCLOCK, DISPLAYSURF
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))

    mousex = 0 #mouses y pos.
    mousey = 0 #mouses y pos.
    pygame.display.set_caption('Tic-Tac-Toe')

    selectedBoxes = [[False, False, False],[False, False, False],[False, False, False]]
    boxOwners = [[0,1,2],[3,4,5],[6,7,8]] #these numbers are placeholders. 

    DISPLAYSURF.fill(WHITE)
    setUpBoard()

    while True: #main game loop
        mouseClicked = False

        for event in pygame.event.get(): #event loop
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                mousex, mousey = event.pos
                #print ((mousex, mousey))
            elif event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                mouseClicked = True

                boxx, boxy = getBoxAtPixel(mousex, mousey)
                if boxx != None and boxy != None: #Then the mouse is over a box
                    if not selectedBoxes[boxx][boxy] and mouseClicked:
                        if activePlayer == PLAYER1:
                            drawX(boxx , boxy)
                            selectedBoxes[boxx][boxy] = True
                            boxOwners[boxx][boxy] = PLAYER1
                            activePlayer = PLAYER2

                        elif activePlayer == PLAYER2:
                            drawO(boxx , boxy)
                            selectedBoxes[boxx][boxy] = True
                            boxOwners[boxx][boxy] = PLAYER2
                            activePlayer = PLAYER1

        #Game win conditions
        for x in range(3): #vertical lines
            if boxOwners[x][0] == boxOwners[x][1] == boxOwners[x][2]:
                gameOver(boxOwners[x][0])
        for y in range(3): #horizontal lines
            if boxOwners[0][y] == boxOwners[1][y] == boxOwners[2][y]:        
                gameOver(boxOwners[0][y])
        if boxOwners[0][0] == boxOwners[1][1] == boxOwners[2][2]:
            gameOver(boxOwners[0][0])
        if boxOwners[2][0] == boxOwners[1][1] == boxOwners[0][2]:
            gameOver(boxOwners[2][0])
        if False not in selectedBoxes[0] and False not in selectedBoxes[1] and False not in selectedBoxes[2]: #Draw check
            gameOver(None)
                
        
        pygame.display.update()
        FPSCLOCK.tick(FPS)


#-----------------------------------------------------------------------------------------------------------------
# Draws a red X
def drawX(boxx , boxy):
    pointX , pointY = leftTopCoordsOfBox(boxx, boxy)
    pygame.draw.line(DISPLAYSURF , RED , ((pointX + 5),(pointY + 5)) , ((pointX + 48),(pointY + 48)), 4)
    pygame.draw.line(DISPLAYSURF , RED , ((pointX + 48),(pointY + 5)) , ((pointX + 5),(pointY + 48)), 4)


#-----------------------------------------------------------------------------------------------------------------
# Draws a blue O
def drawO(boxx , boxy):
    pointX , pointY = leftTopCoordsOfBox(boxx, boxy)
    pygame.draw.circle(DISPLAYSURF, BLUE, ((pointX + 26),(pointY + 26)), 21, 4)

#-----------------------------------------------------------------------------------------------------------------
# Shows what box a pixel is in
def getBoxAtPixel(pointX, pointY):
    if pointX >= 10 and pointX <= 63:
        X = 0
    elif pointX >= 68 and pointX <= 121:
        X = 1
    elif pointX >= 126 and pointX <= 179:
        X = 2
    else:
        X = None
    if pointY >= 10 and pointY <= 63:
        Y = 0
    elif pointY >= 68 and pointY <= 121:
        Y = 1
    elif pointY >= 126 and pointY <= 179:
        Y = 2
    else:
        Y = None
    return X , Y

#-----------------------------------------------------------------------------------------------------------------
# Convert board coordinates to pixel coordinates
def leftTopCoordsOfBox(boxx, boxy):
    return BOXCORNERS[boxy][boxx]

#-----------------------------------------------------------------------------------------------------------------
# Sets up the game board
def setUpBoard():
    #vertical lines
    pygame.draw.line(DISPLAYSURF , (0,0,0), (65,10) , (65,179) , 5)
    pygame.draw.line(DISPLAYSURF , (0,0,0), (123,10) , (123,179) , 5)
    
    #horizontal lines
    pygame.draw.line(DISPLAYSURF , (0,0,0), (10,65) , (179,65) , 5)
    pygame.draw.line(DISPLAYSURF , (0,0,0), (10,123) , (179,123) , 5)

#-----------------------------------------------------------------------------------------------------------------
# Victory Screen
def gameOver(winner):
    if winner == PLAYER1:
        print ('Player 1 Wins!')
        
    elif winner == PLAYER2:
        print ('Player 2 Wins!')
    elif winner == None:
        print ('Cats!(Draw) Maybe next time!')
    
    pygame.quit()
    time.sleep(3)
    sys.exit()
    
#-----------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------

print("""
Hello there!
Tic-Tac-Toe:
Player 1 is X's
Player 2 is O's
Win by placing three of your own shape in a row taking turns


""")
main()
