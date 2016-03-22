#Dylan Waters
#1343144
import random
#rand= random.randint(1,9)
class TicTacToe:
    def __init__(self):
        # "board" is a list of 10 strings representing the board (ignore index 0)      
        self.board = [" "]*10
        self.board[0]="#"
#------------------------------------------------------------- 
    def drawBoard(self):
    # This method prints out the board with current plays adjacent to a board with index.
        print(' '+self.board[7], "|", self.board[8],"|",self.board[9]+'\t'+" 7 | 8 | 9")
        print("-"*11, " "*4, "-"*11)
        print(' '+self.board[4],"|",self.board[5],"|",self.board[6]+'\t'+" 4 | 5 | 6")
        print("-"*11, " "*4, "-"*11)
        print(' '+self.board[1], "|", self.board[2], "|", self.board[3]+'\t'+" 1 | 2 | 3")
#------------------------------------------------------------- 
    def boardFull(self):
    # This method checks if the board is already full and returns True. Returns false otherwise       
        for x in self.board:
            if x==" ":
                return False
        return True
#------------------------------------------------------------- 
    def cellIsEmpty(self, cell):
        cell=int(cell)
        if self.board[cell]== " ":
            return True
        return False     
#------------------------------------------------------------- 
    def assignMove(self, cell,ch):
    # assigns the cell of the board to the character ch
        cell=int(cell)
        self.board[cell]=ch
        return self.board[cell]
#------------------------------------------------------------- 
    def whoWon(self):
    # returns the symbol of the player who won if there is a winner, otherwise it returns an empty string. 
        if self.isWinner("x"):
            return "x"
        elif self.isWinner("o"):
            return "o"
        else:
            return ''
#-------------------------------------------------------------   
    def isWinner(self, ch):
    # Given a player's letter, this method returns True if that player has won.
        if self.board[7]== self.board[8] and self.board[7]== self.board[9] and self.board[7] ==ch:
            return True
        elif self.board[4]== self.board[5] and self.board[4]== self.board[6]and self.board[4] ==ch:
            return True
        elif self.board[1]== self.board[2] and self.board[1]== self.board[3]and self.board[1] ==ch:
            return True    
        elif self.board[7]== self.board[5] and self.board[7]== self.board[3]and self.board[7]==ch:
            return True   
        elif self.board[1]== self.board[5] and self.board[1]== self.board[9]and self.board[1]==ch:
            return True           
        elif self.board[7]== self.board[4] and self.board[7]== self.board[1]and self.board[7]==ch:
            return True
        elif self.board[5]== self.board[8] and self.board[8]== self.board[2]and self.board[5]==ch:
            return True 
        elif self.board[9]== self.board[6] and self.board[6]== self.board[3]and self.board[9]==ch:
            return True   
        else:
            return False
        
    def smartmove(self,ch):
        #square1
        if self.board[7]== self.board[4] and self.board[7] ==ch and self.cellIsEmpty(1):
            return True,1
        elif self.board[5]== self.board[9] and self.board[5] ==ch and self.cellIsEmpty(1):
            return True,1
        elif self.board[2]== self.board[3] and self.board[3] ==ch and self.cellIsEmpty(1):
            return True,1
        #square2
        elif self.board[1]== self.board[3] and self.board[1] ==ch and self.cellIsEmpty(2):
            return True,2  
        elif self.board[5]== self.board[8] and self.board[5] ==ch and self.cellIsEmpty(2):
            return True,2
        #square3
        elif self.board[7]== self.board[5] and self.board[7] ==ch and self.cellIsEmpty(3):
            return True,3
        elif self.board[6]== self.board[9] and self.board[6] ==ch and self.cellIsEmpty(3):
            return True,3
        elif self.board[1]== self.board[2] and self.board[2] ==ch and self.cellIsEmpty(3):
            return True,3 
        #square4
        elif self.board[1]== self.board[7] and self.board[1] ==ch and self.cellIsEmpty(4):
            return True,4 
        elif self.board[5]== self.board[6] and self.board[5] ==ch and self.cellIsEmpty(4):
            return True,4        
        #square5
        #since Smart-Comp picks '5' 1st if its not taken, there is no need to write a block/win function for 5  
        #square6
        elif self.board[9]== self.board[3] and self.board[3] ==ch and self.cellIsEmpty(6):
            return True,6 
        elif self.board[5]== self.board[4] and self.board[5] ==ch and self.cellIsEmpty(6):
            return True,6          
        #square7
        elif self.board[3]== self.board[5] and self.board[5] ==ch and self.cellIsEmpty(7):
            return True,7
        elif self.board[9]== self.board[8] and self.board[8] ==ch and self.cellIsEmpty(7):
            return True,7
        elif self.board[4]== self.board[1] and self.board[1] ==ch and self.cellIsEmpty(7):
            return True,7         
        #square8
        elif self.board[9]== self.board[7] and self.board[7] ==ch and self.cellIsEmpty(8):
            return True,8 
        elif self.board[5]== self.board[2] and self.board[5] ==ch and self.cellIsEmpty(8):
            return True,8           
        #square9
        elif self.board[1]== self.board[5] and self.board[5] ==ch and self.cellIsEmpty(9):
            return True,9
        elif self.board[7]== self.board[8] and self.board[8] ==ch and self.cellIsEmpty(9):
            return True,9
        elif self.board[6]== self.board[3] and self.board[3] ==ch and self.cellIsEmpty(9):
            return True,9        
        else:
            return False,0   
#write some code here
def userplay():
    myBoard=TicTacToe()    
    turn= 1
    done= False
    myBoard.drawBoard()
    while  not done:
        while turn== 1 :
            move=0
            while move not in "1 2 3 4 5 6 7 8 9".split():
                move=input("What is your move? ")            
            #move= int(input("It is your turn x. What is your move? "))
            if myBoard.cellIsEmpty(move):
                myBoard.assignMove(move, "x")
                myBoard.drawBoard()  
                if myBoard.whoWon()== "x":
                    print("x wins!")
                    turn= 100
                    done= True
                elif myBoard.boardFull():
                    turn= 100
                    done = True
                    print("It is a tie")
                turn += 1 
            else:
                print("Illegal Move")
            
        while turn== 2:
            move=0
            while move not in "1 2 3 4 5 6 7 8 9".split():
                move=input("What is your move? ") 
            if myBoard.cellIsEmpty(move):
                myBoard.assignMove(move, "o")
                myBoard.drawBoard()   
                if myBoard.whoWon()=="o":
                    print("o wins!")
                    turn= 100
                    done= True
                elif myBoard.boardFull():
                    turn= 100
                    done= True
                    print("It is a tie")                
                turn -=1
            else:
                print("Illegal Move")
    return

def compplay(player,dumbcomp,randomcomp,smartcomp):
    print("User is player",player)
    if dumbcomp:
        print('User against dumb computer')
    if randomcomp:
        print('User against random computer')
        #print("Not implemented")
        #return
    if smartcomp:
        print('User against smart computer')
        print("Not implemented")
        #return       
    myBoard=TicTacToe()    
    turn= 1
    done= False
    myBoard.drawBoard()
    while  not done:
#~~~~~~~~~~~~~~~~~~~~~~~~~~1st Turn~~~~~~~~~~~~~~~~~
        while turn== 1 :
            move=0
#~~~~~~~~~~~~~~~~~~~~V~USERPLAY~V~~~~~~~~~~~~~~~~~~~~~~~~~~  
            if player=="X":
                while move not in "1 2 3 4 5 6 7 8 9".split():
                    move=input("What is your move? ")
                if myBoard.cellIsEmpty(move):
                    invalid,turn,done=XsTurn(move,myBoard)
#~~~~~~~~~~~~~~~~~~~V~Dumb~Computer~V~~~~~~~~~~~~~~~~~~~~~~~
            elif dumbcomp:
                invalid=True
                move=0
                while invalid:
                    move+=1
                    invalid,turn,done=XsTurn(move,myBoard)
            #Random
            elif randomcomp:
                invalid=True
                while invalid:
                    move= random.randint(1,9)
                    invalid,turn,done=XsTurn(move,myBoard)
            #Smart
            elif smartcomp:
                winr=False
                #print("oh my")
                winr,move=myBoard.smartmove("x")
                if winr:
                    #print("x has selected",move,"To win")
                    invalid,turn,done=XsTurn(move,myBoard)
                else:
                    winr,move=myBoard.smartmove("o")
                    if winr:
                        #print("x has selected",move,"To block")
                        invalid,turn,done=XsTurn(move,myBoard)
                
                    elif myBoard.cellIsEmpty(5):
                        move=5
                        invalid,turn,done=XsTurn(move,myBoard)
                    else:
                        if cornersisempty(myBoard):
                            move=whichcorner(myBoard)
                            invalid,turn,done=XsTurn(move,myBoard)
                        else:
                            move=whichedge(myBoard)
                            invalid,turn,done=XsTurn(move,myBoard)              
    
#~~~~~~~~~~~~~~~~~~~~~~~~~~2nd Turn~~~~~~~~~~~~~~~~~
        while turn== 2:
            move=0
#~~~~~~~~~~~~~~~~~~~~V~USERPLAY~V~~~~~~~~~~~~~~~~~~~~~~~~~~  
            if player=="O":
                while move not in "1 2 3 4 5 6 7 8 9".split():
                    move=input("What is your move? ") 
                if myBoard.cellIsEmpty(move):
                    invalid,turn,done=OsTurn(move,myBoard)
#~~~~~~~~~~~~~~~~~~~V~Dumb~Computer~V~~~~~~~~~~~~~~~~~~~~~~~   
            elif dumbcomp:
                invalid=True
                while invalid:
                    move+=1
                    invalid,turn,done=OsTurn(move,myBoard)
            #random
            elif randomcomp:
                invalid=True
                while invalid:
                    move= random.randint(1,9)
                    invalid,turn,done=OsTurn(move,myBoard)
            #Smart
            elif smartcomp:
                winr=False
                #print("oh my")
                winr,move=myBoard.smartmove("o")
                if winr:
                    #print("O has selected",move,"To win")
                    invalid,turn,done=OsTurn(move,myBoard)
                else:
                    winr,move=myBoard.smartmove("x")
                    if winr:
                        #print("O has selected",move,"To block")
                        invalid,turn,done=OsTurn(move,myBoard)
                
                    elif myBoard.cellIsEmpty(5):
                        move=5
                        invalid,turn,done=OsTurn(move,myBoard)
                    else:
                        if cornersisempty(myBoard):
                            move=whichcorner(myBoard)
                            invalid,turn,done=OsTurn(move,myBoard)
                        else:
                            move=whichedge(myBoard)
                            invalid,turn,done=OsTurn(move,myBoard)                
                                
                            
                        
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`                       
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`          
def cornersisempty(myBoard):
    if myBoard.cellIsEmpty(1):
        return True 
    elif myBoard.cellIsEmpty(3):
        return True 
    elif myBoard.cellIsEmpty(7):
        return True 
    elif myBoard.cellIsEmpty(9):
        return True 
    return False
def whichcorner(myBoard):
    loop=True
    while loop:
        move=random.randint(1,9)
        #print(move)
        if move == 9:
            if myBoard.cellIsEmpty(move):
                return move
        elif move == 7:
            if myBoard.cellIsEmpty(move):
                return move        
        elif move == 3:
            if myBoard.cellIsEmpty(move):
                return move
        elif move == 1:
            if myBoard.cellIsEmpty(move):
                return move
            
def whichedge(myBoard):
    loop=True
    while loop:
        move=random.randint(1,9)
        #print(move)
        if move == 8:
            if myBoard.cellIsEmpty(move):
                return move
        elif move == 4:
            if myBoard.cellIsEmpty(move):
                return move        
        elif move == 6:
            if myBoard.cellIsEmpty(move):
                return move
        elif move == 2:
            if myBoard.cellIsEmpty(move):
                return move    
        

def OsTurn(move,myBoard):
    turn=2
    done=False
    if myBoard.cellIsEmpty(move):
        turn-=1
        myBoard.assignMove(move, "o")
        print("")
        myBoard.drawBoard()  
        if myBoard.whoWon()== "o":
            print("O wins!")
            turn= 100
            done= True
        elif myBoard.boardFull():
            turn= 100
            done = True
            print("It is a tie")    
        return False,turn,done
    else:
        return True,turn,done
    
def XsTurn(move,myBoard):
    turn=1
    done=False
    if myBoard.cellIsEmpty(move):
        turn+=1
        myBoard.assignMove(move, "x")
        print("")
        myBoard.drawBoard()  
        if myBoard.whoWon()== "x":
            print("X wins!")
            turn= 100
            done= True
        elif myBoard.boardFull():
            turn= 100
            done = True
            print("It is a tie")    
        return False,turn,done
    else:
        return True,turn,done   




def testrun():
    myboard=TicTacToe()
    myboard.drawBoard()
    print(myboard.whoWon())

def dumb():
    print('User against dumb computer')
    player=turn()
    dumbcomp=True
    randomcomp=False
    smartcomp=False
    return  player,dumbcomp,randomcomp,smartcomp
        
def rand():
    print('User against random computer')
    player=turn()
    dumbcomp=False
    randomcomp=True
    smartcomp=False
    return  player,dumbcomp,randomcomp,smartcomp
def smart():
    print('User against smart computer')
    player=turn()
    dumbcomp=False
    randomcomp=False
    smartcomp=True
    return player,dumbcomp,randomcomp,smartcomp
    
    
    
def turn():
    loop=True
    #answer=input("Do you want to play X or O?").upper()
    while loop:
        answer=input("Do you want to play X or O? ").upper()
        if answer=="X":
            return 'X'
        elif answer=="O":
            return "O"
        else:
            print("Input must be 'X'or 'O'")
    
def main():
    loop=True
    while loop: 
        player="undefined"
        dumbcomp=False
        randomcomp=False
        smartcomp=False
        print('Welcome to Tic Tac Toe Series')
        print('User against user ...............1')
        print('User against dumb computer ......2')
        print('User against random computer ....3')
        print('User against smart computer......4')
        print('Quit ............................5')        
        try:
            answer=int(input('Enter your choice: '))
        except:
            print('Input must be in the range of 1 to 5')
        else:
            if answer==1:
                #loop=False
                print("Playing agianst user")
                userplay()
            elif answer==2:
                #loop=False
                #print('User against dumb computer')
                player,dumbcomp,randomcomp,smartcomp=dumb()
                compplay(player,dumbcomp,randomcomp,smartcomp)
            elif answer==3:
                #loop=False
                #print('User against random computer')
                player,dumbcomp,randomcomp,smartcomp=rand()
                compplay(player,dumbcomp,randomcomp,smartcomp)
            elif answer==4:
                #print('User against smart computer')  
                player,dumbcomp,randomcomp,smartcomp=smart()
                compplay(player,dumbcomp,randomcomp,smartcomp)
            elif answer==5:
                loop=False
                print('Quiting')
                break
            else:
                print('Input must be in the range of 1 to 5')
               
    #playgame()
    #testrun()

main()
