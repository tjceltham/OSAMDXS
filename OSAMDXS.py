
from re import I


class Game:
    def __init__(self):
        self.board = Board()
        self.count =0
    def display(self):
        self.board.printBoard()
    def play(self):
        winCode =4
        count=0
        self.board.printBoard()
        
        while(winCode==4):
           
            if self.count % 2 ==0: 
                OorX ="X"
            else :
                OorX="O"
            print(" {0}'s Move".format(OorX))
            pos=self.move()
            self.board.update(OorX,pos)
            
            self.board.printBoard()
            winCode=self.board.checkwin(OorX)
            self.count=self.count+1
        if winCode == 1 :
            print("Xs Win")
          
        if winCode == 2 :
            print("Os Win")
        if winCode == 3 :
            print("Draw")
           
    def move(self):
        while True:
            
            print("Please enter a valid position to move to")
            pos = int(input());
            if pos>0 and pos<10 and not(self.board.getValuePos(pos)=="X" or self.board.getValuePos(pos)=="O") :
                break
        return pos-1
            
            
            
            
            
        
    
    
class Board:
    def __init__(self):
        self.board =["1","2","3","4","5","6","7","8","9"]
        self.winnerlines=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    def printBoard(self):
        for x in range(0,3):
            for y in range(0,3):
                print(self.board[x*3+y],end="")
            print("",end="\n")
    def update(self,counter,pos):
        self.board[pos]=counter
    def getValuePos(self,p):
        return self.board[p]
    def checkwin(self,OorX):
        win_code=4
        draw_count =0
        if OorX=="X":
           winCode = 1
        else:
            winCode =2
        for x in range(0,8):
            if self.board[self.winnerlines[x][0]]==OorX and self.board[self.winnerlines[x][1]]==OorX and self.board[self.winnerlines[x][2]]==OorX:
                return winCode
            if self.board[x]==" " :
                draw_count=draw_count +1
        if draw_count ==9:
            winCode = 3
        return win_code
            
            
           
            
g = Game()
g.play()
        
        