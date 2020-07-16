import time

#These methods work to create a minimax algorithm
decision = None
def maximize(board, playerNum, depth):
    #Check if the game is over or we are at the depth of our search
    if checkVictory(board, -1, 4) or tieGame(board) or depth == 0:
        return (utility(board), None)
    else:
        depth -= 1
    v = -200
    for action in possibleMoves(board):
        result(board, action, playerNum)
        total = minimize(board, playerNum * -1, depth)[0]
        if (v < total):
            v = total
            decision = action
        result(board, action, 0)
    return (v, decision)

def minimize(board, playerNum, depth):
    if checkVictory(board, 1, 4) or tieGame(board) or depth == 0:
        return (utility(board), None)
    else:
        depth -= 1
    v = 200
    for action in possibleMoves(board):
        result(board, action, playerNum)
        total = maximize(board, playerNum * -1, depth)[0]
        if (v > total):
            v = total
            decision = action
        result(board, action, 0)
    return (v, decision)

#Returns the "value" of the current board
def utility(board):
    #Check if the player or the bot has won
    if checkVictory(board, 1, 4):
        return 100
    elif checkVictory(board, -1, 4):
        return -100
    #Check if the enemy has 3 in a row
    elif checkVictory(board, -1, 3):
        return -50
    #Check if the bot has 3 in a row
    elif checkVictory(board, 1, 3):
        return 50
    else:
        return 0

#These 4 methods are used to check if a player has won,
#and can also be used to evaluate the current board state
def horizontalAmount(board, playerNum, amount):
    for i in range(6):
        counter = 0
        onEmpty = False
        for j in range(7):
            if board[i + (j * 6)] == playerNum:
                counter += 1
                onEmpty = False
            elif board[i + (j * 6)] == 0 and not onEmpty:
                onEmpty = True
                continue
            else:
                counter = 0
                onEmpty = False
            if counter == amount:
                return True
    return False

def verticalAmount(board, playerNum, amount):
    for i in range(7):
        counter = 0
        for j in range(6):
            if board[(i * 6) + j] == playerNum:
                counter += 1
            elif board[(i * 6) + j] == 0:
                break
            else:
                counter = 0
            if counter == amount:
                return True
    return False

def diagonal45Amount(board, playerNum, amount):
    possibleIndex = [2, 1, 0, 6, 12, 18]
    possibleLengths = [4, 5, 6, 6, 5, 4]
    num = 0
    for i in possibleIndex:
        counter = 0
        onEmpty = False
        for j in range(possibleLengths[num]):
            if board[i + (j * 7)] == playerNum:
                counter += 1
            elif board[i + (j * 7)] == 0 and not onEmpty:
                onEmpty = True
                continue
            else:
                counter = 0
                onEmpty = False
            if counter == amount:
                return True
        num += 1
    return False

def diagonal135Amount(board, playerNum, amount):
    possibleIndex = [3, 4, 5, 11, 17, 23]
    possibleLengths = [4, 5, 6, 6, 5, 4]
    num = 0
    for i in possibleIndex:
        counter = 0
        onEmpty = False
        for j in range(possibleLengths[num]):
            if board[i + (j * 5)] == playerNum:
                counter += 1
            elif board[i + (j * 5)] == 0 and not onEmpty:
                onEmpty = True
                continue
            else:
                counter = 0
                onEmpty = False
            if counter == amount:
                return True
        num += 1
    return False

#These methods are used in conjunction to check if 
#the player that just went won, or if there was a tie
def checkVictory(board, playerNum, amount):
    return (horizontalAmount(board, playerNum, amount) or verticalAmount(board, playerNum, amount) or diagonal45Amount(board, playerNum, amount) or diagonal135Amount(board, playerNum, amount))


def tieGame(board):
    return (board.count(0) == 0)

#This returns the indices of possible moves available on the board
def possibleMoves(board):
    answer = []
    for i in range(7):
        for j in range(6):
            if board[(i * 6) + j] == 0:
                answer.append((i * 6) + j)
                break
    return answer

#Makes a move on the board
def result(board, action, playerNum):
    board[action] = playerNum
    return board

#Prints the game for testing purposes
def printBoard(board):
    for i in range(6):
        currentText = " | "
        for j in range(7):
            currentText += str(board[(5 - i) + (j * 6)])
            currentText += " | "
        print(currentText)
        print("------------------------------")

#Runs the game
def playConnect4(board):
    #When board comes from JS, check if tie or player won
    if checkVictory(board, -1, 4):
        return (-1, True)
    elif (tieGame(board)):
        return (-2, True)
    final = maximize(board, 1, 5)
    finalValue = final[0]
    final = final[1]
    board[final] = 1
    print(finalValue)
    if checkVictory(board, 1, 4):
        return (final, True)
    elif (tieGame(board)):
        return (-2, True)
    else:
        return (final, False)