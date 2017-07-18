import time
import global_vars
from getch import Getch
import animations
from board import Board
import helper as h

keys = [UP,DOWN,RIGHT,LEFT,QUIT,GOD] = [183,184,185,186,-1,ord('g')+ord('o')+ord('d')]
dict = {UP:"Up",DOWN:"Down",RIGHT:"Right",LEFT:"Left",QUIT:"quit",GOD:"god"}

def gameMode():
    """greet the player, shuffle and print the initial board"""
    board = Board()
    # greetings(board)
    board.shuffle()
    board.print_ascii()

    """while the game has not ended"""
    get_arrow = Getch()
    while True:
        choice = get_arrow()
        """ensure that the choice is valid"""
        if choice not in dict:
            print("INVALID CHOICE OF {}".format(str(chr(choice))))
            continue

        if choice == -1:
            print('Thanks for playing.')
            break
        elif dict[choice] == 'god':
            """find the path to the goal from the current board state"""
            global_vars.init(board.board)
            performance = time.time()
            path = []
            """path is a list which is a mutable object.
            Therefore the changes that occur in A* will reflect to this path,
            aka it is passed by reference"""
            board.ast(path) #choosing A* because it is the fastest
            h.clear_scr()
            performance = time.time() - performance

            """awesome presentation of GOD MODE and then follow the path to the goal"""
            animations.present_god_mode(stars=350) #handles all the complex printing
            time.sleep(2)
            board.print_ascii()
            time.sleep(2)
            board.follow(path)

            print('Thanks for playing.')
            break
        proccess(board,choice)
        h.clear_scr()
        board.print_ascii()

def proccess(board,choice):
    try:
        board.move(dict[choice])
    except ValueError as e:
        print("Invalid move")

def greetings(board):
    animations.present_puzzle()
    print("This is the classic 8-puzzle game.")
    time.sleep(3)
    print("Try to move the tile to get to the goal which is:")
    time.sleep(3)
    print(board)
    time.sleep(3)
    print("You can move the tile with the arrow buttons")
    time.sleep(3)
    print("Type the direction you want to move to and press enter to do so.")
    time.sleep(3)
    print("I will now shuffle the board.")
    time.sleep(3)
    print("One more thing before the game begins, type 'god' anytime for GOD mode.")
    time.sleep(4)

# Prints the given board 1,2,3,4,5,6,7,8


if(__name__ == "__main__"):
    gameMode()

