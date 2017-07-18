from pyfiglet import Figlet
import copy
import time
import random
import global_vars
import helper as h
from orderedSet import OrderedSet
from heap import heap

# board class describing a board configuration
class Board:
    # Initialize a Board object
    def __init__(self, board=None):
        if board is None:
            self.board = [list(range(0, 3)), list(range(3, 6)), list(range(6, 9))]
            self.goal = h.to_tuple(h.copyBoard(self.board))
            self.empty = (0, 0)
        else:
            self.board = h.copyBoard(board)
            self.goal = h.to_tuple(h.copyBoard(board))

            #udpate empty variable
            for row in range(0, 3):
                for col in range(0, 3):
                    if self.board[row][col] == 0:
                        self.empty = [row, col]


    #overload print operator
    def __repr__(self):
        str = ''
        count=0
        for i in self.board:
            count+=1
            for j in i:
                if(j!=0):
                    str+= (("{}|").format(j))
                else:
                    str+="_|"
            str += "\b  \n"
            if(count != 3):
                str+="-+-+-\n"
        return str


    # Breadth First search implementation
    def bfs(self):
        if not h.solvable(self):
            raise ValueError("STATE IS UNSOLVABLE")
        frontier = OrderedSet()
        frontier.add(h.to_tuple(self.board))
        pred = {}
        explored = set()
        nodes = max_depth = 0
        while(frontier):
            perForNode = time.time()
            temp = frontier.pop(last=False)
            explored.add(temp)

            if temp == self.goal:
                path = []
                while h.to_tuple(temp) != start:
                    path.append(pred[h.to_tuple(temp)][1])
                    temp = pred[h.to_tuple(temp)][0]
                print("path_to_goal = {}".format(path[::-1]))
                print("cost_of_path = {}".format(len(path)))
                print("nodes_expanded = {}".format(nodes))
                print("goal_depth = {}".format(len(path)))
                print("max_search_depth = {}".format(max_depth))
                return True

            # temp_depth = 0
            # temp2 = h.copyBoard(to_list(temp))
            # while h.to_tuple(temp2) != start:
            #     temp_depth+=1
            #     temp2 = pred[h.to_tuple(temp2)][0]
            # if temp_depth > max_depth:
            #     max_depth = temp_depth

            tempObj = Board(board=temp)

            for neighbor in tempObj.neighbors(pred):
                if(h.to_tuple(neighbor) not in explored):
                    frontier.add(h.to_tuple(neighbor))
            nodes+=1
            perForNode = time.time() - perForNode
            # print("Performance For One Node = {}".format(perForNode))
        return False


    # Depth First search implementation
    def dfs(self,depth_limit=-1):
        if not h.solvable(self):
            raise ValueError("STATE IS UNSOLVABLE")
        frontier = OrderedSet()
        frontier.add(h.to_tuple(self.board))
        pred = {}
        explored = set()
        nodes = max_depth = 0
        while(frontier):
            print("Depth limit = {}".format(depth_limit))
            print("Elements in frontier {}".format(len(frontier)))
            print("Nodes_expanded = {}".format(nodes))
            perForNode = time.time()
            temp = frontier.pop()
            explored.add(temp)

            if temp == self.goal:
                path = []
                while h.to_tuple(temp) != start:
                    path.append(pred[h.to_tuple(temp)][1])
                    temp = pred[h.to_tuple(temp)][0]
                print("path_to_goal = {}".format(path[::-1]))
                print("cost_of_path = {}".format(len(path)))
                print("nodes_expanded = {}".format(nodes))
                print("goal_depth = {}".format(len(path)))
                print("max_search_depth = {}".format(max_depth))
                return True


            if(depth_limit != -1):
                depth = 0
                tempB = h.copyBoard(temp)
                while h.to_tuple(tempB) != start:
                    depth+=1
                    tempB = pred[h.to_tuple(tempB)][0]
                if(depth >= depth_limit):
                    continue

            tempObj = Board(board=temp)

            for neighbor in reversed(tempObj.neighbors(pred)):
                if(h.to_tuple(neighbor) not in explored):
                    frontier.add(h.to_tuple(neighbor))

            nodes+=1
            perForNode = time.time() - perForNode
            print("Performance For One Node = {}".format(perForNode))
        return False


    # A* (star) search implementation
    def ast(self,path):
        if not h.solvable(self):
            raise ValueError("STATE IS UNSOLVABLE")
        nodes = max_depth = 0
        frontier = heap()
        pred = {}
        explored = set()
        frontier.push(h.heuristic_value(self.board, pred), self.board)
        while(frontier):
            perForNode = time.time()
            temp = frontier.pop() # pop should return a TUPLE
            explored.add(temp)

            if temp == self.goal:
                while h.to_tuple(temp) != global_vars.start:
                    path.append(pred[h.to_tuple(temp)][1])
                    temp = pred[h.to_tuple(temp)][0]
                print("path_to_goal = {}".format(path[::-1]))
                print("cost_of_path = {}".format(len(path)))
                print("nodes_expanded = {}".format(nodes))
                print("goal_depth = {}".format(len(path)))
                print("max_search_depth = {}".format(max_depth))
                return True

            tempObj = Board(board=temp)

            for neighbor in tempObj.neighbors(pred):
                neighbor = h.to_tuple(neighbor)
                if (neighbor not in explored) and (neighbor not in frontier):
                    frontier.push(h.heuristic_value(neighbor,pred), neighbor)
                # elif neighbor in frontierSet:
                #     frontier.decrease_key(neighbor)
            nodes+=1
            perForNode = time.time() - perForNode
            # print("Nodes Expored = {}".format(nodes))
            # print("Performance For One Node = {}".format(perForNode))
        return False


    # moveUP,moveDown,moveLeft, moveRight functions
    def move(self, direction):
        row, col = self.getBlank()
        if(direction == "Up"):
            if(row-1 < 0):
                raise ValueError("INVALID MOVE\nCannot Move Up, position out of board bounds\n")

            self.board[row][col] , self.board[row-1][col] = self.board[row-1][col], self.board[row][col]
            self.empty = (self.empty[0]-1,self.empty[1])

        elif(direction == "Down"):
            if(row+1 > 2):
                raise ValueError("INVALID MOVE\nCannot Move Down, position out of board bounds\n")

            self.board[row][col] , self.board[row+1][col] = self.board[row+1][col], self.board[row][col]
            self.empty = (self.empty[0]+1,self.empty[1])

        elif(direction == "Left"):
            if(col-1 < 0):
                raise ValueError("INVALID MOVE\nCannot Move Left, position out of board bounds\n")

            self.board[row][col] , self.board[row][col-1] = self.board[row][col-1], self.board[row][col]
            self.empty = (self.empty[0],self.empty[1]-1)

        elif(direction == "Right"):
            if(col+1 > 2):
                raise ValueError("INVALID MOVE\nCannot Move Right, position out of board bounds\n")

            self.board[row][col] , self.board[row][col+1] = self.board[row][col+1], self.board[row][col]
            self.empty = (self.empty[0],self.empty[1]+1)

        else:
            raise ValueError("INVALID MOVE\nCannot Move {}, unknown direction\n".format(move))


    # retruns list with neighbooring boards
    def neighbors(self, pred):
        # b1 = copy.deepcopy(self)
        # b2 = copy.deepcopy(self)
        # b3 = copy.deepcopy(self)
        # b4 = copy.deepcopy(self)

        b1 = self.copy()
        b2 = self.copy()
        b3 = self.copy()
        b4 = self.copy()

        neighbors = []

        try:
            b1.move("Up")
        except ValueError:
            pass
        else:
            neighbors.append(b1.board)
            if not h.to_tuple(b1.board) in pred:
                pred[h.to_tuple(b1.board)]=[self.board, 'Up']

        try:
            b2.move("Down")
        except ValueError:
            pass
        else:
            neighbors.append(b2.board)
            if not h.to_tuple(b2.board) in pred:
                pred[h.to_tuple(b2.board)]=[self.board, 'Down']

        try:
            b3.move("Left")
        except ValueError:
            pass
        else:
            neighbors.append(b3.board)
            if not h.to_tuple(b3.board) in pred:
                pred[h.to_tuple(b3.board)]=[self.board, 'Left']

        try:
            b4.move("Right")
        except ValueError:
            pass
        else:
            neighbors.append(b4.board)
            if not h.to_tuple(b4.board) in pred:
                pred[h.to_tuple(b4.board)]=[self.board, 'Right']

        return neighbors


    # return a copy of self
    def copy(self):
        # return Board(board=self.board)
        x = Board()
        x.board = h.copyBoard(self.board)
        x.empty = self.empty
        return x


    # returns a tuple of coordinates coresponding to the blank's potision (X,y)
    def getBlank(self):
        # print(self)
        return self.empty


    """just a different print method.
    this one prints the board without seperators"""
    def alt_print(self):
        string = ''
        for row in self.board:
            for num in row:
                if(num):
                    string += '    ' + str(num)
                else:
                    string += '    _'
            string += '\n'
        return string


    def shuffle(self):
        while True:
            lst = list(range(9))
            for i in range(3):
                for j in range(3):
                    x = lst[random.randint(0,len(lst)-1)]
                    lst.remove(x)
                    self.board[i][j] = x
            if h.solvable(self):
                for i in range(3):
                    for j in range(3):
                        if self.board[i][j] == 0:
                            self.empty = (i,j)
                break


    def follow(self,path):
        for i in reversed(path):
            self.move(i)
            h.clear_scr()
            self.print_ascii()
            time.sleep(1)


    # #print the board with awesome ascii art
    def print_ascii(self):
        f = Figlet()
        print(f.renderText(self.alt_print()))

