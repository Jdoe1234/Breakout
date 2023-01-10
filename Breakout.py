import sys, time, msvcrt
import time

def playfieldbackground():
    global backgroundsymbol
    #ORIGINAL = u'\u2591' , blank = ' '
    backgroundsymbol = u'\u2591'
    #PLAYFIELDLINE MAX VALUE = [u'\u2591']*115
    global playfieldlinelen
    playfieldlinelen = 18
    playfieldline = [backgroundsymbol]*playfieldlinelen
    #PLAYGIELD HEIGHT DEFINED BY NUMBER OF LINES, OPTIMAL VALUE IS = [u'\u2591']*6, MAXIMAL VALUE IS = [u'\u2591']*28
    playfield = ['']*6

    rowsofplayfieldlines = 0
    while rowsofplayfieldlines < len(playfield):
        playfield[rowsofplayfieldlines] = playfieldline
        rowsofplayfieldlines += 1
    
    return(playfield)


def displaycmd(playfield):
    #strplayfield = ['placeholder spot 0']
    #strcounter = 1

    # test
    for x in playfield:
        print(x)
    # test





    # SCREENTEARING ISSUE
    print('\n\n\n\n\n\n')
    for i in playfield:
        strplayfieldline = ''.join(i)
        print(' ', strplayfieldline)
    # SCREENTEARING ISSUE     
    #
    #        if  30 >= len(playfield):
    #            strplayfield[0]
    #            strplayfieldline = ''.join(i)
    #            print(strplayfieldline)
    #            strplayfield.append(strplayfieldline)
    #            strcounter += 1


    # 1. attemptint to avoid screen tearing by making 1 big print command
    #   
    #    print('\n\n\n   Breakout:\n \n', strplayfield[1], '\n', strplayfield[2], '\n', strplayfield[3], '\n', strplayfield[4], '\n', strplayfield[5], '\n', strplayfield[6], '\n', #strplayfield[7], '\n', strplayfield[8],)
    #
    #
    # 2. attemptint to avoid screen tearing by relying on window width of cmd to put all prints at teh same time
    #
    #    print('\n\n\n', strplayfield[1],'                                                                                                                                                \
    #            strplayfield[2], '                                                                                                                                                ',\
    #            strplayfield[3], '                                                                                                                                                ',\
    #            strplayfield[4], '                                                                                                                                                ',\
    #            strplayfield[5], '                                                                                                                                                ',\
    #            strplayfield[6], '                                                                                                                                                ',\
    #            strplayfield[7], '                                                                                                                                                ',\
    #            strplayfield[8],)



def characterupdate(playfield, direction):
    #ORIGINAL VALUE = u'\u2588'
    charactersymbol = u'\u2588'
    #MINIMUM VALUE = 1
    charactersize = 5

    # Sætter sidste linje i araet som spillerens position
    activelineofplayer = len(playfield) - 1

    

    
    
    # set startingposition of player "creating player"
    if charactersymbol not in playfield[activelineofplayer]:
        i = 0
        playfield[activelineofplayer] = [charactersymbol]
        i += 1
        while i < charactersize:
            playfield[activelineofplayer].append(charactersymbol) 
            i += 1
        while i < len(playfield[0]):
            playfield[activelineofplayer].append(backgroundsymbol) 
            i += 1
            
        return(playfield)  
        
        
        

    #player moves left 
    elif direction == b'a':
        # så længe spiller ikke er opped ad venstre væg
        if playfield[activelineofplayer].index(charactersymbol) != 0:
            # tag placering fra current playfield før overskrivning begynder
            originalspaceofplayer = playfield[activelineofplayer].index(charactersymbol)
            # counter som tjekker correct antal opretelser af liste items
            i = 0
            # opret første liste item som blankspot og add til counter
            playfield[activelineofplayer] = [backgroundsymbol]
            i += 1
            #building right of player indtil før tidligere character postion er ramt
            while i < len(playfield[0]) - charactersize - originalspaceofplayer + 1:
                playfield[activelineofplayer].insert(0, backgroundsymbol)
                i += 1
            #building player   WRONG
            while i < len(playfield[0]) - originalspaceofplayer  + 1:
                playfield[activelineofplayer].insert(0, charactersymbol)
                i += 1
            #building left of player - 1 fordi spilleren skal rykke 1 længere mod venstre
            while i < len(playfield[0]):
                playfield[activelineofplayer].insert(0, backgroundsymbol)
                i += 1


    # player moves right
    elif direction == b'd': 
        # så længe spiller ikke er opped ad højre væg
        if playfield[activelineofplayer].index(charactersymbol) != len(playfield[0]) - charactersize:
            originalspaceofplayer = playfield[activelineofplayer].index(charactersymbol)
            i = 0
            # opret første liste item som blankspot og add til counter
            playfield[activelineofplayer] = [backgroundsymbol]
            i += 1
            #building left of player + 1 fordi spilleren skal rykke 1 længere mod højre
            while i < originalspaceofplayer + 1:
                playfield[activelineofplayer].append(backgroundsymbol)
                i += 1
            #building player
            while i < originalspaceofplayer + charactersize + 1:
                playfield[activelineofplayer].append(charactersymbol)
                i += 1
            #building right of player
            while i < len(playfield[0]):
                playfield[activelineofplayer].append(backgroundsymbol)
                i += 1
    else:
        return playfield
    


    return playfield


def ballupdate(playfield):
    #ORIGINAL VALUE = u'\u2588'
    global ballalive
    ballsymbol = u'\u03BF'
    balldirection = 'upright'
    
    for x in playfield:
        for y in x:
            if y != ballsymbol:
                ballalive = False
    if ballalive == False:
        playfield[-2] = [ballsymbol]
        i = 0
        while i < playfieldlinelen - 1:
            playfield[-2].append(backgroundsymbol)
            i += 1
        
    i = -1
    for x in playfield:
        i += 1
        for y in x:
            if y == ballsymbol:
                ballalive = True
                ballpositionvertical = i
                ballpositionhorizontal = x.index(ballsymbol)
                break
    print(ballpositionvertical, ballpositionhorizontal)



    # detect collision and update placement of the ball dependent on direction
    if ballalive == True:
        movementupdate(playfield, balldirection, ballpositionvertical, ballpositionhorizontal)
    print(u'\u25EC', '  TROUBLE  TROUBLE  TROUBLE ', u'\u25EC'                               )
    return(playfield)

        
def movementupdate(playfield, balldirection, ballpositionvertical, ballpositionhorizontal):
    #detect collision and update direction of ball



    #update placement of ball dependent on direction
    if balldirection == 'upright':
    
    #UNDER CONSTRUCTION
        playfield[ballpositionvertical - 1]
        print(playfield[ballpositionvertical - 1])
        i = 0
        for i in playfield[ballpositionvertical - 1]:
            i += 1
            if i == ballpositionvertical:
                print('i: ', i)
                tall = playfield[i]


        print('ball going up and right')
    if balldirection == 'downright':
        print('ball going down and right')
    if balldirection == 'upleft':
        print('ball going up and left')
    if balldirection == 'downleft':
        print('ball going down and left')
    


    return(playfield)
    

def main ():
    input('\n         Hi\n   To reduce Screen\n      noise, pls\n   reduce the size\n    of the window\n    til this text\n     is centered\n\n')
    input('\n         Hi\n\n\n\n      Controls:\n        a & d\n     \n\n ')
    print('\n\n\n\n\n\n\n\n\n')


    
    
    playfield = playfieldbackground()
    
    # playfield [playfieldline[], playfieldline[], playfieldline[]...]

    #ACTIVATE THIS DIRECTION FOR MOVEMENT TO BE CONTINUES
    direction = ''        

    i = 0
    while i < 3:
        i += 1


        while True:
            displaycmd(playfield)
            if msvcrt.kbhit():
                direction = msvcrt.getch()
                if direction == b'a':
                    characterupdate(playfield, direction)
                    break

                elif direction == b'd':
                    characterupdate(playfield, direction)
                    break
                else:
                    break

            else:
                # character position updated or created
                
                characterupdate(playfield, direction)

                
                ballupdate(playfield)

                
        #        print('')
        #        print('      no trouble before displaycmd on loop: ', i)
        #        print('')
                
            
            break


        time.sleep(0.1)
    






    input()
    
main()



print(u'\u25EC', '  TROUBLE  TROUBLE  TROUBLE ', u'\u25EC', ' value: ',                                 )

# use for ball = u'\u03BF'

