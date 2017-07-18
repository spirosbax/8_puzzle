import global_vars
import os

def heuristic_value(board,pred):
    return  manhattan_distance(board) + distance_from_start(board,pred)


#self explanatory
def distance_from_start(board,pred):
    distance = 0
    while to_tuple(board) != global_vars.start:
        board = pred[to_tuple(board)][0]
        distance+=1
    return distance


#calcutes and retruns manhattan distance between of board from goal
def manhattan_distance(board):
    goal = global_vars.start_1d
    board = to_1d_list(board)
    return sum(abs(board_index//3 - goal_index//3) + abs(board_index%3 - goal_index%3)
               for board_index, goal_index in ((board.index(i), i) for i in range(1, 9)))


#converts a board to a one-dimensional list
def to_1d_list(board):
    x = []
    for i in board:
        for j in i:
            x.append(j)
    return x


# converts given config ex. 1,2,3,...,8 and turns it into a 2 by 2 list board
def getValues(args):
    temp = []
    for i in args.split(","):
        temp.append(ord(i) - 48)
    temp = [temp[0:3], temp[3:6], temp[6:9]]
    return temp


# conver a board to LIST and return it
def to_list(board):
    result = []
    for i in board:
        result.append(list(i))
    return result


# conver a board to TUPLE and return it
def to_tuple(board):
    result = []
    for i in board:
        result.append(tuple(i))
    return tuple(result)


# return True if the state represented by obj is sovlable, and false if it's not
def solvable(obj):
    temp = []
    for i in obj.board:
        temp+=i
    temp.remove(0)

    inversions = 0
    # Count number of inversions
    for index, i in enumerate(temp):
        for j in range(index+1, 8):
            if(i > temp[j]):
                inversions+=1

    # print("Inversions : {}".format(inversions))
    if(inversions%2 == 1):
        return False

    return True


# returns a copy to a given board
def copyBoard(board):
    x = []
    for i in board:
        sub = []
        for j in i:
            sub.append(j)
        x.append(sub)
    return x


def clear_scr():
    os.system('cls' if os.name == 'nt' else 'clear') #clear the screen for windows and linux

