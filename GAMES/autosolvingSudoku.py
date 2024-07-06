import numpy as np

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

print(np.matrix(grid))

def possible(row, column, number):
    #Note:matrix[row_x][column_y]
    global grid
    #1st check: Check the row: if the number appears already in the same row or not
    for i in range(0,9):
        if grid[row][i] == number:
            return False
    #2nd check: Check the column: if the number appears already in the column row or not
    for i in range(0,9):
        if grid[i][column] == number:
            return False
    #3rd check: Check the block: if the number appears already in the block or not
    #Notes:
    #0//3=0, 1//3=0, 2//3=0 (we divide it by 3 and then round it down)
    #4//3=1*3 = 3, 5//3=1*3,
    #7//3*3 = 6
    x0 = (column //3) * 3 # starting point
    y0 = (row //3)*3 #starting point
    #it will be always the starting point of our blocks, it can be 0, 3, 6
    #aaa|bbb|ccc
    #aaa|bbb|ccc -> section a: x0=0, y0=0
    #aaa|bbb|ccc -> section b: x0=3, y0=0
    #___________ -> section c: x0=6, y0=0
    #ddd|eee|fff -> section d: x0=0, y0=3
    #ddd|eee|fff -> section e: x0=3, y0=3
    #ddd|eee|fff -> section f: x0=6, y0=3
    #___________ -> section g: x0=0, y0=6
    #ggg|hhh|iii -> section h: x0=3, y0=6
    #ggg|hhh|iii -> section i: x0=6, y0=6
    #ggg|hhh|iii
    #___________
    for i in range(0,3):
        for j in range(0,3):
            if grid[y0+i][x0+i] == number:
                return False

    return True

def solve():
    global grid
    for row in range(0,9):
        for column in range(0,9):
            #is it empty?
            if grid[row][column] == 0:
                for number in range(1,10): #1 up 9
                    if possible(row,column,number):
                        #if the move is possible, assign the number
                        grid[row][column]  = number
                        #call the function again to solve next one
                        solve()
                        # if it gets stuck, do backtracking/ go back " a few steps" and put element to empty which equals to zero ("0") in this case 
                        grid[row][column] = 0
        
                return

    #Print the solved sudoku grid
    print(np.matrix(grid))
    input('More solutions')

solve()
