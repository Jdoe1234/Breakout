import sys, time, msvcrt
import time

def playfieldbackground():
    #ORIGINAL = u'\u2591' , blank = ' '  (remember to change backgroundsymbol in playerline aswell if you want a matching line behind the bottom bar)
    backgroundsymbol = ' '
    #PLAYFIELDLINE MAX VALUE = [u'\u2591']*115
    playfieldline = [backgroundsymbol]*18
    #PLAYGIELD HEIGHT DEFINED BY NUMBER OF LINES, OPTIMAL VALUE IS = [u'\u2591']*6, MAXIMAL VALUE IS = [u'\u2591']*28
    playfield = ['']*6

    rowsofplayfieldlines = 0
    while rowsofplayfieldlines < len(playfield):
        playfield[rowsofplayfieldlines] = playfieldline
        rowsofplayfieldlines += 1
    return(playfield)


def displaycmd(playfield):
#    strplayfield = ['placeholder spot 0']
#    strcounter = 1

    print('\n\n\n\n\n\n')

    # SCREENTEARING ISSUE
    for i in playfield:
        strplayfieldline = ''.join(i)
        print(' ', strplayfieldline)
    # SCREENTEARING ISSUE     
    
    
    
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
    #REDOMENDED VALUE = 3
    charactersize = 5
    #ORIGINAL VALUE = 2
    characterstartingpoint = 0
    #ORIGINAL VALUE = u'\u2591', FOR BLANK = ' ' 
    backgroundsymbol = ' '

    activelineofplayer = len(playfield) - 1
    player = charactersymbol * charactersize
    playerbackroundright = len(playfield[0]) - charactersize - characterstartingpoint


    # set startingposition of player "create player"
    if charactersymbol not in playfield[activelineofplayer]:
        playfield[activelineofplayer] = (characterstartingpoint * backgroundsymbol) + player + (playerbackroundright * backgroundsymbol)
        


        



    elif direction == b'a':
        playerbackroundright = len(playfield[0]) - charactersize - playfield[activelineofplayer].index(charactersymbol)
        if playfield[activelineofplayer].index(charactersymbol) != 0:
            playerbackroundright = len(playfield[0]) - charactersize - playfield[activelineofplayer].index(charactersymbol)        
            playfield[activelineofplayer] = ((playfield[activelineofplayer].index(charactersymbol) - 1) * backgroundsymbol) + player + ((playerbackroundright + 1) * backgroundsymbol)

    elif direction == b'd':
        playerbackroundright = len(playfield[0]) - charactersize - playfield[activelineofplayer].index(charactersymbol)
        if playerbackroundright != 0:
            playerbackroundright = len(playfield[0]) - charactersize - playfield[activelineofplayer].index(charactersymbol)        
            playfield[activelineofplayer] = ((playfield[activelineofplayer].index(charactersymbol) + 1) * backgroundsymbol) + player + ((playerbackroundright - 1) * backgroundsymbol)

        


        
# position update for player character



# IMPORTANT REAL CODE FOR UPDATING POSITION
#
#        playerbackroundright = len(playfield[0]) - charactersize - playfield[activelineofplayer].index(charactersymbol)        
#        playfield[activelineofplayer] = (playfield[activelineofplayer].index(charactersymbol) * u'\u2591') + player + (playerbackroundright * u'\u2591')







#    for x in playfield:
#        playfieldline = playfield[x]
#        print(playfieldline)
    return playfield


def main ():
    input('\n         Hi\n   To reduce Screen\n      noise, pls\n   reduce the size\n    of the window\n    til this text\n     is centered\n\n')
    input('\n         Hi\n\n\n\n      Controls:\n        a & d\n     \n\n ')
    print('\n\n\n\n\n\n\n\n\n')














    playfield = playfieldbackground()
    # playfield [playfieldline[], playfieldline[], playfieldline[]...]



















    #ACTIVATE THIS DIRECTION FOR MOVEMENT TO BE CONTINUES
    direction = ''        

    
    i = 0
    while i < 155:
        i += 1


        #ACTIVATE THIS DIRECTION FOR MOVEMENT TO REQUIRE HOLDING DOWN BUTTON (causing some issues)
        #direction = ''        
        while True:
            if msvcrt.kbhit():


#               ________________________________________________________________ dont unders function necesity
#                timeout = 0.1
#               ________________________________________________________________ dont unders function necesity
#                startTime = time.time()

                direction = msvcrt.getch()
#                                    ___________________________________________ dont unders function necesity
                if direction == b'a': #and time.time() - startTime > timeout:
                    playfield = characterupdate(playfield, direction)
                    break

#                                      _________________________________________ dont unders function necesity
                elif direction == b'd': #and time.time() - startTime > timeout:
                    playfield = characterupdate(playfield, direction)
                    break

                else:
                    break

            else:
                playfield = characterupdate(playfield, direction)
                # character position updated or created


                
        #        print('')
        #        print('      no trouble before displaycmd on loop: ', i)
        #        print('')
                
                displaycmd(playfield)
                # playfield is unchanged but printed as a string
            
            time.sleep(0.1)



    






    input()
    
main()



print(u'\u25EC', '  TROUBLE  TROUBLE  TROUBLE ', u'\u25EC', ' value: ',                                 )

# use for ball = u'\u03BF'

