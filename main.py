initial = [2,8,3,
           1,6,4,
           0,5,7]
goal =[2,0,8,1,6,3,7,5,4]

def main():
    stateSTree = StateSpaceTree(initial,goal)
    TravelNode = stateSTree._root
    goalNode = stateSTree._goal
    i=0
    # while (TravelNode.array != goalNode.array):
    print(TravelNode.array)
    while(i!=1):
        n = locateSpace(TravelNode.array)
        print(n)
        if(n==0):
            TravelNode.right = SSTnode(right(TravelNode.array,n))
            TravelNode.down = SSTnode(down(TravelNode.array,n))
            
            heuristicList = (TravelNode.down.heuristics,TravelNode.right.heuristics)
            h_index = heuristicList.index(min(heuristicList))

            if(h_index == 0):
                TravelNode = TravelNode.down
            elif(h_index == 1):
                TravelNode = TravelNode.right
            
        elif(n==1):
            TravelNode.right = SSTnode(right(TravelNode.array,n))
            TravelNode.down = SSTnode(down(TravelNode.array,n))
            TravelNode.left = SSTnode(left(TravelNode.array,n))

            heuristicList = (TravelNode.down.heuristics,TravelNode.right.heuristics,TravelNode.left.heuristics)
            h_index = heuristicList.index(min(heuristicList))

            if(h_index == 0):
                TravelNode = TravelNode.down
            elif(h_index == 1):
                TravelNode = TravelNode.right
            elif(h_index == 2):
                TravelNode = TravelNode.left
        elif(n==2):
            TravelNode.left = SSTnode(left(TravelNode.array,n))
            TravelNode.down = SSTnode(down(TravelNode.array,n))

            heuristicList = (TravelNode.down.heuristics,TravelNode.left.heuristics)
            h_index = heuristicList.index(min(heuristicList))

            if(h_index == 0):
                TravelNode = TravelNode.down
            elif(h_index == 1):
                TravelNode = TravelNode.left
        elif(n==3):
            TravelNode.right = SSTnode(right(TravelNode.array,n))
            TravelNode.down = SSTnode(down(TravelNode.array,n))
            TravelNode.up = SSTnode(up(TravelNode.array,n))

            heuristicList = (TravelNode.right.heuristics,TravelNode.down.heuristics,TravelNode.up.heuristics)
            h_index = heuristicList.index(min(heuristicList))

            if(h_index == 0):
                TravelNode = TravelNode.right
            elif(h_index == 1):
                TravelNode = TravelNode.down
            elif(h_index == 2):
                TravelNode = TravelNode.up
        elif(n==4):
            TravelNode.right = SSTnode(right(TravelNode.array,n))
            TravelNode.down = SSTnode(down(TravelNode.array,n))
            TravelNode.up = SSTnode(up(TravelNode.array,n))
            TravelNode.left = SSTnode(left(TravelNode.array,n))

            heuristicList = (TravelNode.right.heuristics,TravelNode.down.heuristics,TravelNode.up.heuristics,TravelNode.left.heuristics)
            h_index = heuristicList.index(min(heuristicList))

            if(h_index == 0):
                TravelNode = TravelNode.right
            elif(h_index == 1):
                TravelNode = TravelNode.down
            if(h_index == 2):
                TravelNode = TravelNode.up
            elif(h_index == 3):
                TravelNode = TravelNode.left
        elif(n==5):
            TravelNode.down = SSTnode(down(TravelNode.array,n))
            TravelNode.up = SSTnode(up(TravelNode.array,n))
            TravelNode.left = SSTnode(left(TravelNode.array,n))

            heuristicList = (TravelNode.down.heuristics,TravelNode.up.heuristics,TravelNode.left.heuristics)
            h_index = heuristicList.index(min(heuristicList))

            if(h_index == 0):
                TravelNode = TravelNode.down
            elif(h_index == 1):
                TravelNode = TravelNode.up
            elif(h_index == 2):
                TravelNode = TravelNode.left
        elif(n==6):
            
            TravelNode.right = SSTnode(right(TravelNode.array,n))
            TravelNode.up = SSTnode(up(TravelNode.array,n))

            heuristicList = (TravelNode.right.heuristics,TravelNode.up.heuristics)
            h_index = heuristicList.index(min(heuristicList))

            if(h_index == 0):
                TravelNode = TravelNode.right
            elif(h_index == 1):
                TravelNode = TravelNode.up
        elif(n==7):
            TravelNode.right = SSTnode(right(TravelNode.array,n))
            TravelNode.up = SSTnode(up(TravelNode.array,n))
            TravelNode.left = SSTnode(left(TravelNode.array,n))

            heuristicList = (TravelNode.right.heuristics,TravelNode.up.heuristics,TravelNode.left.heuristics)
            h_index = heuristicList.index(min(heuristicList))

            if(h_index == 0):
                TravelNode = TravelNode.right
            elif(h_index == 1):
                TravelNode = TravelNode.up
            elif(h_index == 2):
                TravelNode = TravelNode.left
        elif(n==8):
            TravelNode.up = SSTnode(up(TravelNode.array,n))
            TravelNode.left = SSTnode(left(TravelNode.array,n))
            print(TravelNode.array)
            # print(TravelNode.up.array)
            # print(TravelNode.left.array)

            heuristicList = (TravelNode.up.heuristics,TravelNode.left.heuristics)
            print(heuristicList)
            h_index = heuristicList.index(min(heuristicList))
            print(h_index)

            if(h_index == 0):
                TravelNode = TravelNode.up
            elif(h_index == 1):
                TravelNode = TravelNode.left
        i=1
        
        

    # print(TravelNode.array)



    # root = node(initial,None,None,None,None)

""" this also for user input """
#    initial = valueInput("initial")
#    goal = valueInput("goal")

""" this code for user input  """
# def valueInput(s):
#     arr = []
#     print(f"Enter the {s} state with space as 0")
#     for i in range(9):
#         temp = int(input(f"Enter {i+1}: "))
#         arr.append(temp)

#     return arr

def swapPositions(list, pos1, pos2):
     
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list

# where n is the location of empty state
def up(array,n):
    return swapPositions(array,n,n-3)
def down(array,n):
    return swapPositions(array,n,n+3)
def right(array,n):
    return swapPositions(array,n,n+1)
def left(array,n):
    return swapPositions(array,n,n-1)

def heuristics(goal,current):#goalnode vs currentnode
    h=0
    for i in range(9):
        if goal[i]!=current[i]:
            h=h+1
    return h


def locateSpace(array):
    for i in range(9):
        if(array[i]==0):
            return i

class SSTnode:
        def __init__(self,Array):
            self.array = Array    
            self.heuristics = heuristics(goal,self.array)
            self.left = None
            self.up = None
            self.down = None
            self.right = None

class StateSpaceTree:
    def __init__(self,initial,goal):
        self._root = SSTnode(initial)
        self._goal = SSTnode(goal)

            
main()