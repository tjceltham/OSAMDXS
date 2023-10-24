
import random


class Game:
    def __init__(self, mode):
        self.board = Board()
        self.count =0
        if mode ==1:
            self.players = [AIPlayer(self.board), Humanplayer(self.board)]
        else:
            self.players = [Humanplayer(self.board), Humanplayer(self.board)]
        
    def display(self):
        self.board.printBoard()
    def play(self):
        winCode =STILL_PLAYING
        count=0
        self.board.printBoard()
        
        while(winCode==STILL_PLAYING):
           
            if self.count % 2 ==0: 
                OorX ="X"
            else :
                OorX="O"
            print(" {0}'s Move".format(OorX))
            pos=self.players[self.count % 2].move()
            self.board.update(OorX,pos)
            
            self.board.printBoard()
            winCode=self.board.checkwin(OorX)
            self.count=self.count+1
        if winCode == XS_WIN :
            print("Xs Win")
          
        if winCode == OS_WIN :
            print("Os Win")
        if winCode == DRAW :
            print("Draw")
           
    
            
            
            
            
            
        
    
    
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
        return self.board[p-1]
    def checkwin(self,OorX):
        win_code= STILL_PLAYING
        draw_count =0
        if OorX=="X":
           winCode = XS_WIN
        else:
            winCode =OS_WIN
        for x in range(0,8):
            if self.board[self.winnerlines[x][0]]==OorX and self.board[self.winnerlines[x][1]]==OorX and self.board[self.winnerlines[x][2]]==OorX:
                return winCode
            if self.board[x]==" " :
                draw_count=draw_count +1
        if draw_count ==9:
            winCode = DRAW
        return win_code
# polymorphism - data types must hold references to objects - no abstract classes as such
# 
# use super().__init__(param1,param2)    to call super class constructor
class Player :
     def move(self):
        raise NotImplementedError("Subclass must implement this method")
    
class Humanplayer:
    def __init__(self, b):
        self.board =b 
    def move(self):
        while True:
            
            print("Please enter a valid position to move to")
            pos = int(input());
            if pos>0 and pos<10 and not(self.board.getValuePos(pos)=="X" or self.board.getValuePos(pos)=="O") :
                break
        return pos-1
    
class AIPlayer:
     def __init__(self, b):
        self.board =b
     def move(self):
       
         while True:
            
            pos = random.randrange(1,10);
            if pos>0 and pos<10 and not(self.board.getValuePos(pos)=="X" or self.board.getValuePos(pos)=="O") :
                break
         return pos-1
        

 # constants for game status - no const keyword in python        
XS_WIN = 1
OS_WIN =2
DRAW = 3
STILL_PLAYING = 4          
            
g = Game(1)
g.play()
        
        