#create a list called board, it is mutable
board = ["-", "-","-",
        "-", "-", "-",
        "-", "-", "-",]

currentPlayer = "X"
winner = None
gameRunning = True
boardIsFull = False

#print the game board
def printBoard(board):
    print(board[0] + " | " + board[1] + " | "+ board[2])
    print("----------")
    print(board[3] + " | " + board[4] + " | "+ board[5])
    print("----------")
    print(board[6] + " | " + board[7] + " | "+ board[8])

#take player input
def playerInput(board):
    move = int(input("Enter a number 1-9: "))
    #the input() function always returns a string value; the variable move is at this moment an int
    if move >= 1 and move<=9 and board[move-1] == "-":
        board[move-1] = currentPlayer
    #invalid move:
    else:
        print("Uh Oh, that position is already taken.")

#check for win or tie
#in tic tac toe there are three ways to win: horizontaly, verticaly and diagonaly.
#check horizontal function
def checkHorizontal(board):
    global winner

    if (board[0] == board[1] == board[2]) and board[0]!= "-":
        winner = board[0]
        return True
    elif (board[3] == board[4] == board[5]) and board[3]!= "-":
        winner = board[3]
        return True
    
    elif (board[6] == board[7] == board[8]) and board[6]!= "-":
        winner = board[6]
        return True
    
    else:
        return False

#check vertical function
def checkVertical(board):
    global winner

    if (board[0] == board[3] == board[6]) and board[0]!= "-":
        winner = board[0]
        return True
    elif (board[1] == board[4] == board[7]) and board[1]!= "-":
        winner = board[1]
        return True
    
    elif (board[2] == board[5] == board[8]) and board[2]!= "-":
        winner = board[2]
        return True
    
    else:
        return False

#check vertical function
def checkDiagonal(board):
    global winner

    if (board[0] == board[4] == board[8]) and board[0]!= "-":
        winner = board[0]
        return True
    elif (board[6] == board[4] == board[2]) and board[2]!= "-":
        winner = board[2]
        return True
    
    else:
        return False

#check for tie
def checkTie(board): 
    #check if board is Full:
    global boardIsFull 
    if "-" not in board:
        #board is full
        boardIsFull = True
    
    if boardIsFull and winner == None:
        print("It's a tie!")
        gameRunning = False
        return True

    else:
        return False

#switch the player
def switchPlayer():
    global currentPlayer

    if currentPlayer == "X":
        currentPlayer = "O"
    
    else:
        currentPlayer = "X"

#check for win or tie again
def checkWin():
    if checkDiagonal(board) or checkHorizontal(board) or checkVertical(board):
        print(f"The winner is {winner}!")

while gameRunning:
    printBoard(board)
    playerInput((board))
    checkWin()
    checkTie(board)
    switchPlayer()