
import random
import re
import tkinter as tk
from tkinter import ttk
import time

import datetime
from wsgiref.util import setup_testing_defaults

class Game:
    def __init__(self, mode):
        self.board = Board()
        self.winCode = STILL_PLAYING
        self.count =0
        if mode ==1:
            self.players = [AIPlayer(self.board), Humanplayer(self.board)]
        if mode ==2:    
            self.players = [Humanplayer(self.board), Humanplayer(self.board)]
        if mode ==3:    
            self.players = [AIPlayer(self.board), AIPlayer(self.board)]  
        if mode ==4:
            self.players = [Humanplayer(self.board), AIPlayer(self.board)] 
        
    def restart(self):
        self.board.restart()
        self.count=0
    def display(self):
        self.board.printBoard()
        
    def get_game_state(self):
        return self.board.checkwin()
        
    def get_value_at_pos(self,pos):
        return self.board.getValuePos(pos)
    def play(self):
        winCode =STILL_PLAYING
        
        pos = self.players[self.count%2].move()
        if(pos>=0):
            self.move(pos)
    
    def move(self,pos):
        if(self.count %  2 ==0):
            self.board.update("X",pos)
        else:
            self.board.update("O",pos)
        self.count=self.count+1
            
            
           
    
            
            
            
            
            
        
    
    
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
        self.board[pos-1]=counter
    def getValuePos(self,p):
        return self.board[p-1]
    def restart(self):
        self.board=["1","2","3","4","5","6","7","8","9"];
        
        
    def checkwin(self):
        OorX =["X","O"]
        win_code= STILL_PLAYING
        draw_count =0
                   
        for counter in OorX:
            for x in range(0,8):
                if self.board[self.winnerlines[x][0]]==counter and self.board[self.winnerlines[x][1]]==counter and self.board[self.winnerlines[x][2]]==counter:
                    if counter == "X":
                        win_code=XS_WIN
                    else:
                        win_code=OS_WIN
                        
        if(win_code ==STILL_PLAYING):
            for x in range(0,9):
                if(self.board[x]=="X" or self.board[x]=="O"):
                    draw_count=draw_count+1
                if (draw_count ==9):
                    win_code=DRAW
                
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
        # doesn't do anything yet
        return -1
        

    
class AIPlayer:
     def __init__(self, b):
        self.board =b
     def move(self):
       
         while True:
            
            pos = random.randrange(1,10);
            if pos>0 and pos<10 and not(self.board.getValuePos(pos)=="X" or self.board.getValuePos(pos)=="O") :
                break
         return pos
 
class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.clock()
        
    #initiate_move- - calls play function in model that asks a player to move
    # if the player is an AI a move will be made
    # if the player is a human the UI will await a move
    def initiate_move(self):
        self.model.play()
        win_state =self.model.get_game_state()
        if( win_state == OS_WIN):
            print("Os Win")
          #  self.model.restart()
            self.view.update_game_label("Os Win")
            self.view.disable()
        if( win_state == XS_WIN):
            print("Xs Win")
          #  self.model.restart()
            self.view.update_game_label("Xs Win")
            self.view.disable()
        if(win_state == DRAW):
            print ("DRAW")
            self.view.update_game_label("DRAW")
            
         #   self.model.restart()
            self.view.disable()
        
            
        
   
    # move initiated via ui
    def move(self,pos):
        print(pos)
        state=self.model.move(pos)
        # updating from users move
        self.view.set_board_pos(self.model.get_value_at_pos(pos),pos)
        win_state =self.model.get_game_state()
        if( win_state == OS_WIN):
            print("Os Win")
            self.view.update_game_label("Os Win")
            
           
            #self.model.restart()
            self.view.disable()
        if( win_state == XS_WIN):
            print("Xs Win")
            self.view.update_game_label("Xs Win")
           
           
            #self.model.restart()
            self.view.disable()
        if(win_state == DRAW):
            print ("DRAW")
            self.view.update_game_label("DRAW")
           # self.model.restart()
            self.view.disable()
        if(win_state==STILL_PLAYING):
            self.initiate_move()
            
        
        
        
    def start(self):
        self.model.restart()
        self.view.enable()
        self.view.update_game_label("-----------")
        self.initiate_move()
    
        
    def update_ui(self):
        print("update UI")
        for x in range(1,10):
            v=self.model.get_value_at_pos(x)
            self.view.set_board_pos(v,x)
        
    
    def clock(self):
        time = datetime.datetime.now().strftime("Time: %H:%M:%S")
        self.update_ui()
            
        self.view.after(100, self.clock) 
    
   

        
        
        
class View(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # create widgets
        # label
        self.label = ttk.Label(self, text='Os and Xs')
        self.label.grid(row=1, column=2)  
        
        self.start_button = ttk.Button(self, text='Start', command= self.start_button_clicked)
        self.start_button["state"]="disabled"
        self.start_button.grid(row=2, column=1, padx=0)
        
        self.move_button1 = ttk.Button(self, text='1', command=lambda: self.move_button_clicked(1))
        self.move_button1.grid(row=3, column=1, padx=0)
        
        self.move_button2 = ttk.Button(self, text='2', command=lambda: self.move_button_clicked(2))
        self.move_button2.grid(row=3, column=2, padx=0)
        
        self.move_button3 = ttk.Button(self, text='3', command=lambda: self.move_button_clicked(3))
        self.move_button3.grid(row=3, column=3, padx=0)
        
        self.move_button4 = ttk.Button(self, text='4', command=lambda: self.move_button_clicked(4))
        self.move_button4.grid(row=4, column=1, padx=0)
        
        self.move_button5 = ttk.Button(self, text='5', command=lambda: self.move_button_clicked(5))
        self.move_button5.grid(row=4, column=2, padx=0)
        
        self.move_button6 = ttk.Button(self, text='6', command=lambda: self.move_button_clicked(6))
        self.move_button6.grid(row=4, column=3, padx=0)
        
        self.move_button7 = ttk.Button(self, text='7', command=lambda: self.move_button_clicked(7))
        self.move_button7.grid(row=5, column=1, padx=0)
        
        self.move_button8 = ttk.Button(self, text='8', command=lambda: self.move_button_clicked(8))
        self.move_button8.grid(row=5, column=2, padx=0)
        
        self.move_button9 = ttk.Button(self, text='9', command=lambda: self.move_button_clicked(9))
        self.move_button9.grid(row=5, column=3, padx=0)
        self.win_label = ttk.Label(self, text='-----------')
        self.win_label.grid(row=7,column=1)
        
        self.board=[self.move_button1,self.move_button2,self.move_button3,self.move_button4,self.move_button5,self.move_button6,self.move_button7,self.move_button8,self.move_button9]
        self.disable()
        self.controller=None
        

    def disable(self):
        for x in range(0,9):
            self.board[x]["state"]="disabled"
            self.start_button["state"]="enabled"
    def enable(self):
        for x in range(0,9):
            self.board[x]["state"]="enable"
            self.start_button["state"]="disable"
    
    def update_game_label(self,state):
        self.win_label["text"]=state
        

    def start_button_clicked(self):
        self.controller.start()
        
    def move_button_clicked(self,pos):
        self.controller.move(pos)
        
    def set_board_pos(self,counter,pos):
        print(counter)
        print(pos)
       # btnMyButton["text"] = "Im not button"
        self.board[pos-1]["text"]= counter
                                
          
    def set_controller(self, controller):
        """
        Set the controller
        :param controller:
        :return:
        """
        self.controller = controller
        
class App(tk.Tk):
    def __init__(self):
        super().__init__()
       # self.root =tk.Tk()
        self.title('Tkinter MVC Demo')
        # create a model
        model = Game(4)

        # create a view and place it on the root window
        view = View(self)
        view.grid(row=0, column=0, padx=10, pady=10)

        # create a controller
        controller = Controller(model, view)

        # set the controller to view
        view.set_controller(controller)
            
     

# constants for game status - no const keyword in python 
XS_WIN = 1
OS_WIN =2
DRAW = 3
STILL_PLAYING = 4 
if __name__ == '__main__':
    app = App()
    app.mainloop()  

        
         
            
        
        