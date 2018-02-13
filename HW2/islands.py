#!/usr/bin/python3
import os
import sys

if( len(sys.argv) == 2): 
    file = open(sys.argv[1])
else:
    file = open("tiles.txt")


text = file.read()
print(text)
lineLen=text.find('\n')
totalLen=len(text)

islands=[0]
visited=[]
canVisit=[]

#must convert string to list to do it the way my mind wants to
textArr=list(text)

def islandFinder(block,lineSize,blockSize,lastTile='',index=0):
    '''
        Depth first from position 0 (default) to expand on the first visited tile in N,S,E,W directions 
        if tile is found to be a . and the previous tile was a number then, label that tile with that 
        number. If the previous tile was also numbered, but the new tile dont do nothin. If the last tile 
        was a tilde, and the current tile is a . check list of numbers for next number to use.
        For every current move add index to visited, and do not move to tile if the number is in visited

    '''
    if(block[index]=='.'):
        if(lastTile!=''):
            block[index]=lastTile
        else:
            # print(islands)
            block[index]=str(len(islands))
            lastTile=block[index]
            islands.append(block[index])
    else:
        lastTile=''    
    
    visited.append(index)
    #Calculate where we can move
    for nsew in [-lineSize,lineSize,1,-1]:
        if( index+nsew not in visited and index+nsew not in canVisit and index+nsew<blockSize and index+nsew>0 and block[index+nsew]!='\n'):
            #order canVisit list to prioritize '.' tiles
            if(block[index+nsew]=='.'):
                canVisit.insert(0,index+nsew)
            else:
                canVisit.append(index+nsew)
    #preform the move
    for moveTo in canVisit:
        canVisit.remove(moveTo)
        islandFinder(block,lineSize,blockSize,lastTile,index=moveTo)

islandFinder(textArr,lineLen,totalLen)

print()
print(''.join(textArr))
