import numpy as np

class BoardManager:

    moves = []

    def __init__(self, current_board, previous_move=None,target_board = [1,2,3,4,5,6,7,8],previous_board = None, level=0):
        self.current_board = current_board
        self.previous_move = previous_move
        self.previous_board  = previous_board
        self.child_boards = []
        self.current_board_value = 0
        self.level = level
        self.target_board = target_board
        self.boardList = list(self.current_board)
        

        if self.previous_board!= None:
            self.level = self.previous_board.level + 1
        self.current_board_value = self.hammingDistCalc(self.current_board)

        if self.current_board_value != 0:
            self.checks = self.check_possible_child_board()

            # choose the child board with min value 
            self.child_hamming_values = self.min_child_board_check()

            min_value = min(self.child_hamming_values)
            min_index = self.child_hamming_values.index(min_value)
            
            print("current selected board is ")
            self.boardPrinter(self.current_board)
            print("with hamming distance",str(self.current_board_value))
            print("previous choice of action = "+str(self.previous_move))
            print("with childrens as ")
            for child in self.child_boards:
                self.boardPrinter(child)
                print(self.hammingDistCalc(child))
                

            print("printing selected child board with previous checks")
            print(self.child_boards[min_index])
            print(self.checks)
            BoardManager.moves.append(self.checks[min_index])
            self.child = BoardManager(current_board= self.child_boards[min_index],previous_move=self.checks[min_index],previous_board=self)
        else:
            pass


    def boardPrinter(self,arr):
        arr = np.array(arr)
        order = int(np.sqrt(len(arr)))
        print(arr.reshape(order,order))

    def min_child_board_check(self):

        child_hamming_values = []
        for board in self.child_boards:
            child_hamming_values.append(self.hammingDistCalc(board))
        return child_hamming_values
        
    def newboard(self,direction):
        index = self.boardList.index(0)

        row = int(index / 3) 
        col = index % 3
        new_row = row
        new_col = col

        if direction == "up":
            new_row-=1
        elif direction == "down":
            new_row+=1
        elif direction == "left":
            new_col-=1
        else:
            new_col+=1

        new_index = new_row*3 + new_col
        copyofboard = self.boardList.copy()
        copyofboard[index],copyofboard[new_index]= copyofboard[new_index],copyofboard[index]

        return copyofboard


    def hammingDistCalc(self,currentBoard):
        
        distance = 0
        # list banaye index nikalna sajilo ( aayena np bata :P)
        boardList = list(currentBoard)

        for i in self.target_board:
            # khojera number(i) given board ma index return garne
            index = boardList.index(i)
            
            # base board ma i bhanne number kun row ra column ma huncha calculate garne
            baseColumn = (i-1) % 3
            baseRow = int((i-1)/3)


            # tei number i kun row ra column ma chha calculate garne
            currentColumn = index % 3
            currentRow = int(index/3)

            # testo distance add up garne
            distance += abs(currentColumn - baseColumn) + abs(currentRow - baseRow)

        return distance

    
    def check_possible_child_board(self):
        # Your implementation for checking possible child board goes here
        checks = ["up","down","left","right"] 
        if self.previous_move == "left":
            checks.remove("right")
        elif self.previous_move == "right":
            checks.remove("left")
        elif self.previous_move == "up":
            checks.remove("down")
        elif self.previous_move == "down":
            checks.remove("up")

        # calculate row, column of board
        index = self.boardList.index(0)
        row = int(index / 3) 
        col = index % 3

        # remove mapping if on edges
        if row == 0:
            checks.remove("up")
        elif row == 2:
            checks.remove("down")

        if col == 0:
            checks.remove("left")
        elif col == 2:
            checks.remove("right")

        for check in checks:
            self.child_boards.append(self.newboard(check))

        return checks