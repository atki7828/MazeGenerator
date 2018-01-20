import random
import time
import pygame

numRows = 20 
numCols = 15
cellWidth = 25
cellHeight = 25
margin = 10
sleepTime = 0.1

i = 0
BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)

def save():
    global i
    pygame.image.save(screen,'../mazeframes/' + str(i) + '.png')
    i += 1

def recurse(x,y,grid):
    nWall = [(margin + cellWidth) * y + margin, (margin + cellHeight) * x, cellWidth, margin]
    sWall = [(margin + cellWidth) * y + margin, (margin + cellHeight) * x + margin + cellHeight, cellWidth, margin]
    eWall = [(margin + cellWidth) * y + margin + cellWidth, (margin + cellHeight) * x + margin, margin, cellHeight]
    wWall = [(margin + cellWidth) * y, (margin + cellHeight) * x + margin, margin,cellHeight]
    currCell = [(margin + cellWidth) * y + margin, (margin + cellHeight) * x + margin, cellWidth, cellHeight]

    N = 1
    W = 1
    E = 1
    S = 1

    pygame.display.flip()
    #save()
    pygame.draw.rect(screen,RED,currCell)
    time.sleep(sleepTime)
    go = random.randint(0,4)
    while(N or S or E or W):
        #go = random.randint(0,4)
        if go % 4 == 0:
            if x > 0 and not grid[x-1][y]:
                pygame.draw.rect(screen,RED,nWall)
                grid[x-1][y] = 1
                recurse(x-1,y,grid)
                pygame.draw.rect(screen,GREEN,nWall)
                pygame.display.flip()
                #save()
            N = 0;
            go += 1

        if go % 4 == 1:
            if y > 0 and not grid[x][y-1]:
                pygame.draw.rect(screen,RED,wWall)
                grid[x][y-1] = 1
                recurse(x,y-1,grid)
                pygame.draw.rect(screen,GREEN,wWall)
                pygame.display.flip()
                #save()
            W = 0
            go += 1

        if go % 4 == 2:
            if y < numCols - 1 and not grid[x][y+1]:
                pygame.draw.rect(screen,RED,eWall)
                grid[x][y+1] = 1
                recurse(x,y+1,grid)
                pygame.draw.rect(screen,GREEN,eWall)
                pygame.display.flip()
                #save()
            E = 0
            go += 1

        if go % 4 == 3:
            if x < numRows - 1 and not grid[x+1][y]:
                pygame.draw.rect(screen,RED,sWall)
                grid[x+1][y] = 1
                recurse(x+1,y,grid)
                pygame.draw.rect(screen,GREEN,sWall)
                pygame.display.flip()
                #save()

            S = 0
            go += 1
    pygame.draw.rect(screen,GREEN,currCell)
    pygame.display.flip()
    #save()
    time.sleep(sleepTime)
    return

grid = []
for row in range(numRows):
    grid.append([])
    for column in range(numCols):
        grid[row].append(0)

pygame.init()

WINDOW_SIZE = [numCols * (cellWidth + margin) + margin, numRows * (cellHeight + margin) + margin]
screen = pygame.display.set_mode(WINDOW_SIZE)

done = False

screen.fill(BLACK)

for row in range(numRows):
    for column in range(numCols):
        pygame.draw.rect(screen,
                        WHITE,
                        [(margin + cellWidth) * column + margin,
                            (margin + cellHeight) * row + margin,
                            cellWidth,
                            cellHeight])
x = random.randint(0,numRows - 1)
y = random.randint(0,numCols - 1)
recurse(x,y,grid)
pygame.draw.rect(screen,GREEN,[pygame.display.get_surface().get_width() - margin - cellWidth, pygame.display.get_surface().get_height() - margin, cellWidth, margin])
pygame.draw.rect(screen,GREEN,[margin,0,cellWidth,margin])
pygame.display.flip()
#save()

 
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

pygame.image.save(screen,'../maze.png') 
pygame.quit()

