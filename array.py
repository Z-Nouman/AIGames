import time


array = [1, 0, 0, 0, 0, 0, -1, 1, 0, 0, 0, 0, -1, -1, 1, 0, 0, 0, -1, -1, -1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
array2 = [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, -1, 1, -1, -1, 0, 0, -1, -1, -1, 1, 0, 0, 1, 1, -1, 0, 0, 0, -1, 1, 1, -1, 0, 0, 1, 0, 0, 0, 0, 0]


start_time = time.time()


def checkHorizontalWin(array):
    for i in range(6):
        counter = 1
        for j in range(6):
            if array[i + (6 * j)] == 0:
                continue
            if counter == 4:
                return True
            elif array[i + (6 * j)] == array[i + (6 * (j + 1))]:
                counter += 1
            else:
                counter = 1
    return False

def checkVerticalWin(array):
    for i in range(7):
        counter = 1
        for j in range(6):
            if array[(i * 6) + j] == 0:
                continue
            if counter == 4:
                return True
            elif array[(i * 6) + j] == array[(i * 6) + j + 1]:
                counter += 1
            else:
                counter = 1
    return False

def check45DiagonalWin(array):
    possibleIndex = [2, 1, 0, 6, 12, 18]
    possibleLengths = [4, 5, 6, 6, 5, 4]
    num = 0
    for i in possibleIndex:
        counter = 1
        for j in range(possibleLengths[num]):
            if array[(i + (7 * j))] == 0:
                continue
            if counter == 4:
                return True
            elif array[(i + (7 * j))] == array[(i + (7 * (j + 1)))]:
                counter += 1
            else:
                counter = 1
        num += 1
    return False

def check135DiagonalWin(array):
    possibleIndex = [3, 4, 5, 11, 17, 23]
    possibleLengths = [4, 5, 6, 6, 5, 4]
    num = 0
    for i in possibleIndex:
        counter = 1
        for j in range(possibleLengths[num]):
            if array[(i + (5 * j))] == 0:
                continue
            if counter == 4:
                return True
            elif array[(i + (5 * j))] == array[(i + (5 * (j + 1)))]:
                counter += 1
            else:
                counter = 1
        num += 1
    return False

def endGame(board):
    return (check135DiagonalWin(board) or check45DiagonalWin(board) or checkHorizontalWin(board) or checkVerticalWin(board))

def possibleMoves(board):
    answer = []
    for i in range(7):
        for j in range(6):
            if board[(i * 6) + j] == 0:
                answer.append((i * 6) + j)
                break
        if len(answer) != (i + 1):
            answer.append(-1)
    return answer

def result(board, action, player):
    board[action] = player
    return board
def maximize(board, depth):
    depth = depth
    if depth < 1:
        return 200
    else:
        depth -= 1
    player = -1
    if endGame(board):
        return utility(board)
    v = -200
    for action in possibleMoves(board):
        v = max(v, minimize(result(board, action, player), depth))
    return v

def minimize(board, depth):
    if depth < 1:
        return -200
    else:
        depth -= 1
    player = 1
    if endGame(board):
        return utility(board)
    v = 200
    for action in possibleMoves(board):
        v = min(v, maximize(result(board, action, player), depth))

def utility(board):
    if endGame(board):
        return 100
    else:
        return 0

board = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] 
while True:
    x = int(input("Enter an index >>> "))
    board[x] = 1
    maximize(board, 4)


