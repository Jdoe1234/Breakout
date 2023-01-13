import sys, time, msvcrt
import time

def playfieldbackground():
    global backgroundsymbol
    global playfieldlinelen

    #ORIGINAL = u'\u2591' , blank = u'\u2588'
    backgroundsymbol = u'\u2591'
    #PLAYFIELDLINE MAX VALUE = 115
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


def createplayer(playfield):
    global charactersymbol
    global charactersize

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
        

def characterupdate(playfield, direction):
    activelineofplayer = len(playfield) - 1

    characterlive = True
    for i in playfield[activelineofplayer]:
        if i == charactersymbol:
            characterlive = True
            break
        elif i != charactersymbol:
            characterlive = False

    if characterlive == False:
        gamelive = False

    #player moves left 
    if direction == b'a' and characterlive == True:
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
    elif direction == b'd' and characterlive == True: 
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


def createball(playfield):
    #ORIGINAL VALUE = u'\u2588'
    global ballsymbol
    ballsymbol = u'\u03BF'
    global ballalive
    ballalive = False

    
    playfield[-3] = [ballsymbol]
    i = 0
    while i < playfieldlinelen - 1:
        playfield[-3].append(backgroundsymbol)
        i += 1

    global balldirection
    balldirection = ['n', 'e']
        

def ballupdate(playfield):

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
    
    #detect collision
    if playfield[-1][ballpositionhorizontal] == charactersymbol and ballpositionvertical == len(playfield) - 2:
        balldirection[0] = 'n'


    #update direction of ball
    if ballpositionhorizontal == playfieldlinelen - 1:
        balldirection[1] = 'w'

    #   CAREFUL - CREATING A STRING OF PLAYFIELD   
    if ballpositionvertical == len(playfield) - 1:
        playfield[1] = [backgroundsymbol, backgroundsymbol, backgroundsymbol, backgroundsymbol, 'G', 'a', 'm', 'e', backgroundsymbol, 'o', 'v', 'e', 'r', '!', backgroundsymbol, backgroundsymbol, backgroundsymbol, backgroundsymbol]
        playfield[2] = [backgroundsymbol, backgroundsymbol, backgroundsymbol, backgroundsymbol, "'", 'S', 'p', 'a', 'c', 'e', 'b', 'a', 'r', "'", backgroundsymbol, backgroundsymbol, backgroundsymbol, backgroundsymbol]
        playfield[3] = [backgroundsymbol, backgroundsymbol, backgroundsymbol, 't', 'o', backgroundsymbol, 't', 'r', 'y', backgroundsymbol, 'a', 'g', 'a', 'i', 'n', backgroundsymbol, backgroundsymbol, backgroundsymbol]
        gamelive = False
        return playfield

    if ballpositionhorizontal == 0:
        balldirection[1] = 'e'

    if ballpositionvertical == 0:
        balldirection[0] = 's'
    
    


    

    
    # CODE CAN PROBABLY BE SHORTEND (pack all into 1 loop)

    #update placement of ball dependent on direction
    if balldirection[0] == 'n' and balldirection[1] == 'e':  
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
             
   
    
    return(playfield)

      
def blokcreation(playfield):
    global bloksymbol
    bloksymbol = 'M'
    for i in playfield[0]:
        if i != bloksymbol:
            print('create bloks')


def blokupdate(playfield):
    print('bloks are live')


def main ():
    input('\n         Hi\n   To reduce Screen\n      noise, pls\n   reduce the size\n    of the window\n    til this text\n     is centered\n\n')
    input('\n         Hi\n\n\n\n      Controls:\n        a & d\n     \n\n ')
    print('\n\n\n\n\n\n\n\n\n')

    
    global gamelive
    playfield = playfieldbackground()
    createplayer(playfield)
    createball(playfield)
    blokcreation(playfield)


    direction = ''        
    gamelive = True
    i = 0
    while i < 212:
        i += 1
        
        
        while gamelive == True:
            displaycmd(playfield)
            if gamelive == False:
                break    
            if msvcrt.kbhit():
                direction = msvcrt.getch()
                if direction == b'a' and gamelive == True:
                    characterupdate(playfield, direction)
                    break

                elif direction == b'd'and gamelive == True:
                    characterupdate(playfield, direction)
                    break

                elif direction == b' ':
                    main()
                    break
                else:
                    break

            else:
                # character position updated or created
                characterupdate(playfield, direction)
                ballupdate(playfield)
                
                #dblokupdate(playfield)

                

                
        #        print('')
        #        print('      no trouble before displaycmd on loop: ', i)
        #        print('')
                
            
            break


        time.sleep(0.08)
    

main()


print(u'\u25EC', '  TROUBLE  TROUBLE  TROUBLE ', u'\u25EC', ' value: ',                                 )

