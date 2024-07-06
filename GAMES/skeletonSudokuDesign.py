import pygame
import numpy as np

width = 550
background_color =(255,226,241)
original_grid_element_color = (0,0,0)
grid = [
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,0,0]
]

def main():
    pygame.init()
    win = pygame.display.set_mode((width, width))
    pygame.display.set_caption("Sudoku :)")
    win.fill(background_color)
    myfont = pygame.font.SysFont('Adobe Arabic', 28)
    global grid

    #set the divisions familiar to the game
    for i in range(0,10):
        #0, 3, 6 sections
        if (i%3 == 0):
            pygame.draw.line(win, (0,0,0),(50+ 50*i, 50), (50 + 50*i, 500),3)
            pygame.draw.line(win, (0,0,0),(50,50 + 50*i), (500,50+ 50*i),3)

        pygame.draw.line(win, (0,0,0),(50+ 50*i, 50), (50 + 50*i, 500),1)
        pygame.draw.line(win, (0,0,0),(50,50 + 50*i), (500,50+ 50*i),1)
        
    pygame.display.update()

    #Note:matrix[row_j][column_i]
    print(len(grid[0]))
    for i in range(0, 9):
        for j in range(0,9):
            if(0< grid[i][j]<10):
                value = myfont.render(str(grid[i][j]), True, original_grid_element_color)
                #add it to the screen
                win.blit(value, ((j+1)*50 +20,(i+1)*50 +20) )
    pygame.display.update()



    #for the external window of pygame to appear
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

main()
