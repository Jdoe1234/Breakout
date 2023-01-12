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

        
        print(u'\u25EC', '  TROUBLE  TROUBLE  TROUBLE ', u'\u25EC',       '         character spawned'                        )    
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
    global ballsymbol
    ballsymbol = u'\u03BF'
    ballalive = False

    # checks if the ball symbol is already on the playingfield
    # taking each individuel line in playfield and assigns them to x, counting times loop is running to locate playfield[0]
    i = - 1
    for x in playfield:
        i += 1
        # takes each indvidual varaible of each individual line and assign them to y
        for y in x:
            # checks each individual variable if it is the symbol of the ball, if the ball is found, location is stored as "[playfield[], playfieldline[]]"
            if y == ballsymbol:
                ballalive = True
                ballpositionvertical = i
                ballpositionhorizontal = x.index(ballsymbol)
                break

    # creating a ball at its spawn location if there is no ballsymbol detected on the playingfield
    if ballalive == False:
        print(u'\u25EC', '  TROUBLE  TROUBLE  TROUBLE ', u'\u25EC',       '         ball spawned'                        )
        playfield[-3] = [ballsymbol]
        i = 0
        while i < playfieldlinelen - 1:
            playfield[-3].append(backgroundsymbol)
            i += 1
        global balldirection
        balldirection = ['n', 'e']
        

    #if ball is present, cordinates are send to functions needing location
    if ballalive == True:
        print('ballposition cord: ', ballpositionvertical, ballpositionhorizontal)
    # detect collision and update placement of the ball dependent on direction
        movementupdate(playfield, ballpositionvertical, ballpositionhorizontal)

    return(playfield)

        
def movementupdate(playfield, ballpositionvertical, ballpositionhorizontal):



    
    #detect collision      MISSING
    if ballpositionvertical == len(playfield) - 2: # ADDD " and "player below = True" "
        balldirection[0] = 'n'

    #update direction of ball      MISSING
    if ballpositionhorizontal == playfieldlinelen - 1:
        balldirection[1] = 'w'
        print('moving bk west')

    #   NOT WORKING
    if ballpositionvertical == len(playfield) - 1:
        print('you lost')
        # currently respawns player because of load order, overwriting ball, meaning a new ball gets spawned aswell as it is loaded afterwards

    if ballpositionhorizontal == 0:
        balldirection[1] = 'e'
        print('moving bk east')

    if ballpositionvertical == 0:
        balldirection[0] = 's'
        print('moving bk south')
    
    


    

    
    # CODE CAN PROBABLY BE SHORTEND (pack all into 1 loop)

    #update placement of ball dependent on direction
    print('balldirection: ', balldirection)
    if balldirection[0] == 'n' and balldirection[1] == 'e':  
        print('ball going up and right')
        i = -1
        temporaryplayfieldline = []
        for playfieldline in playfield:
            i += 1
            #alters vertical position of ball: "-" equels up, "+" equals down
            if i == ballpositionvertical - 1:
                for ii in range(len(playfieldline)):
                #alters horizontal position of ball: "-" equels left, "+" equals right
                    if ii < ballpositionhorizontal + 1:
                        temporaryplayfieldline.insert(0, backgroundsymbol)
                    if ii == ballpositionhorizontal:
                        temporaryplayfieldline.append(ballsymbol)
                    if ii > ballpositionhorizontal + 1:
                        temporaryplayfieldline.append(backgroundsymbol)
                playfield[i] = temporaryplayfieldline
                break

    if balldirection[0] == 's' and balldirection[1] == 'e':  
        print('ball going down and right')
        i = -1
        temporaryplayfieldline = []
        for playfieldline in playfield:
            i += 1
            #alters vertical position of ball: "-" equels up, "+" equals down
            if i == ballpositionvertical + 1:
                for ii in range(len(playfieldline)):
                #alters horizontal position of ball: "-" equels left, "+" equals right
                    if ii < ballpositionhorizontal + 1:
                        temporaryplayfieldline.insert(0, backgroundsymbol)
                    if ii == ballpositionhorizontal:
                        temporaryplayfieldline.append(ballsymbol)
                    if ii > ballpositionhorizontal + 1:
                        temporaryplayfieldline.append(backgroundsymbol)
                playfield[i] = temporaryplayfieldline
                break

    if balldirection[0] == 'n' and balldirection[1] == 'w':  
        print('ball going up and left')
        i = -1
        temporaryplayfieldline = []
        for playfieldline in playfield:
            i += 1
            #alters vertical position of ball: "-" equels up, "+" equals down
            if i == ballpositionvertical - 1:
                for ii in range(len(playfieldline)):
                #alters horizontal position of ball: "-" equels left, "+" equals right
                    if ii < ballpositionhorizontal - 1:
                        temporaryplayfieldline.insert(0, backgroundsymbol)
                    if ii == ballpositionhorizontal:
                        temporaryplayfieldline.append(ballsymbol)
                    if ii > ballpositionhorizontal - 1:
                        temporaryplayfieldline.append(backgroundsymbol)
                playfield[i] = temporaryplayfieldline
                break

    if balldirection[0] == 's' and balldirection[1] == 'w':  
        print('ball going down and left')
        i = -1
        temporaryplayfieldline = []
        for playfieldline in playfield:
            i += 1
            #alters vertical position of ball: "-" equels up, "+" equals down
            if i == ballpositionvertical + 1:
                for ii in range(len(playfieldline)):
                #alters horizontal position of ball: "-" equels left, "+" equals right
                    if ii < ballpositionhorizontal - 1:
                        temporaryplayfieldline.insert(0, backgroundsymbol)
                    if ii == ballpositionhorizontal:
                        temporaryplayfieldline.append(ballsymbol)
                    if ii > ballpositionhorizontal - 1:
                        temporaryplayfieldline.append(backgroundsymbol)
                playfield[i] = temporaryplayfieldline
                break
    

    #updating ball position regardles of direction
    playfield[i] = temporaryplayfieldline       

    # replaces(removes) ball from prevoious location   
    i = -1
    for playfieldline in playfield:
        # i is the number of current playfield list in int passes from 0 to 5
        # playfieldline is the actual list
        i += 1
        if i == ballpositionvertical:
            # ii is the variable in the current list of playfieldline, loop is needed to detect if ii is a certain object
            for ii in range(len(playfieldline)):
                if ii == ballpositionhorizontal and i == ballpositionvertical:
                    playfieldline[ii] = backgroundsymbol
             
    

    return(playfield, balldirection)
    

def main ():
    input('\n         Hi\n   To reduce Screen\n      noise, pls\n   reduce the size\n    of the window\n    til this text\n     is centered\n\n')
    input('\n         Hi\n\n\n\n      Controls:\n        a & d\n     \n\n ')
    print('\n\n\n\n\n\n\n\n\n')


    
    
    playfield = playfieldbackground()
    
    # playfield [playfieldline[], playfieldline[], playfieldline[]...]


    direction = ''        

    i = 0
    while i < 212:
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

# ball creation trigger new creation of player

