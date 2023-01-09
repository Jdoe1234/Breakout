import sys
import time

def playfieldbackground():
    playfieldline = [u'\u2591']*115
    playfield = ['']*28
    playfieldcounter = 0
    while playfieldcounter < len(playfield):
        playfield[playfieldcounter] = playfieldline
        playfieldcounter += 1
    return(playfield)


def displaycmd(playfield):
    print('')
    print('')
    print('')
    for i in playfield:
        playfieldline = ''.join(i)
        print(playfieldline)
            


def main ():
    i = 0
    while i < 1:
        playfield = playfieldbackground()
        # playfield [playfieldline[], playfieldline[], playfieldline[]...]
        displaycmd(playfield)
        # playfield is unchanged but printed as a string
        i += 1





    







    
    input()
    
    
main()


