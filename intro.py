decision = None
def maximize(board, playerNum):
    if endGame(board):
        return (utility(board), None)
    v = -200
    for action in possibleMoves(board):
        result(board, action, playerNum)
        total = (minimize(board, playerNum * -1))[0]
        if (v < total):
            v = total
            decision = action
        result(board, action, 0)
    return (v, decision)

def minimize(board, playerNum):
    if endGame(board):
        return (utility(board), None)
    v = 200
    for action in possibleMoves(board):
        result(board, action, playerNum)
        total = (maximize(board, playerNum * -1))[0]
        if (v > total):
            v = total
            decision = action
        result(board, action, 0)
    return (v, decision)

def horizontalAmount(board, playerNum, amount):
    for i in range(3):
        counter = 0
        for j in range(3):
            if board[i + (j * 3)] == playerNum:
                counter += 1
            elif board[i + (j * 3)] == 0:
                continue
            else:
                counter = 0
            if counter == amount:
                return True
    return False

def verticalAmount(board, playerNum, amount):
    for i in range(3):
        counter = 0
        for j in range(3):
            if board[(i * 3) + j] == playerNum:
                counter += 1
            elif board[(i * 3) + j] == 0:
                continue
            else:
                counter = 0
            if counter == amount:
                return True
    return False

def diagonal45Amount(board, playerNum, amount):
    for i in range(1):
        counter = 0
        for j in range(3):
            if board[i + (j * 4)] == playerNum:
                counter += 1
            elif board[i + (j * 4)] == 0:
                continue
            else:
                counter = 0
            if counter == amount:
                return True
    return False

def diagonal135Amount(board, playerNum, amount):
    for i in range(1):
        counter = 0
        for j in range(3):
            if board[(i + 2) + (j * 2)] == playerNum:
                counter += 1
            elif board[(i + 2) + (j * 2)] == 0:
                continue
            else:
                counter = 0
            if counter == amount:
                return True
    return False

def checkVictory(board, playerNum):
    return (horizontalAmount(board, playerNum, 3) or verticalAmount(board, playerNum, 3) or diagonal45Amount(board, playerNum, 3) or diagonal135Amount(board, playerNum, 3))

def endGame(board):
    return (checkVictory(board, 1) or checkVictory(board, -1) or len(possibleMoves(board)) == 0)

def possibleMoves(board):
    answer = []
    for i in range(len(board)):
        if board[i] == 0:
            answer.append(i)
    return answer

def result(board, action, playerNum):
    board[action] = playerNum
    return board

def utility(board):
    if checkVictory(board, 1):
        return 100
    elif checkVictory(board, -1):
        return -100
    else:
        return 0

def playGame(board):
    if board.count(0) == 9:
        return (0, False)
    if checkVictory(board, -1):
        return (-1, True)
    elif (endGame(board)):
        return (-2, True)
    final = maximize(board, 1)[1]
    board[final] = 1
    if checkVictory(board, 1):
        return (final, True)
    elif (endGame(board)):
        return (-2, True)
    else:
        return (final, False)