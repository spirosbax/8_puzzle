from helper import to_tuple
from helper import to_1d_list

def init(board):
    global start
    global start_1d
    start = to_tuple(board)
    start_1d = to_1d_list(board) #will be used in manhattan distance calculations

