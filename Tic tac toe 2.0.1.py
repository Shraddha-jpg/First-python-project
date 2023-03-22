from tkinter import *
from tkinter import messagebox

count=0
board=[['','','',''],
           ['','','',''],
           ['','','',''],
           ['','','','']]
score1=0
score2=0
draw=0
buttons=[]
#Whenever user clicks rule button,the rules are displayed
def Rule():
    global t    
    msg1=messagebox.showinfo("RULES","(i)The first player is X and the second player is O\n(ii)The two players take turns alternately and put their marks in the desired place by pressing the button in that place\n(iii)The first player to get four of their marks in a single row, single column or diagonally gets 1 point\n(iv)In the event of a 'draw' game, none of the players get a point\n(v)The player with the highest points at the end of 3 rounds wins the game\nENJOY THE GAME!!!!")   

#Whenever the user selects the quit option, this message is displayed
def Quit():
    global t    
    msg=messagebox.askquestion("Confirm","Do you want to Quit? You still have chances!")
    if msg=='yes':
        t.destroy()

#Destructs the winner window and game window
def renew():             
    global t,winnerWindow
    winnerWindow.destroy()
    if score1+score2+draw==3:
        scoreboard()
        
        
    else:
        reset()
def gamefinish():
    global t
    scoreboards.destroy()
    t.destroy()
def newgame():
    global score2,score1,draw
    scoreboards.destroy()
    score1=score2=draw=0
    reset()
def scoreboard():
    global scoreboards
    scoreboards=Tk()
    scoreboards.title("Scoreboard")
    scoreboards.configure(bg="pink")
    z="Player X:"+str(score1)
    y="Player O:"+str(score2)
    if score1>score2:
        x="Player X is the winner"
    elif score2>score1:
        x="Player O is the winner"
    else:
        x="IT'S A DRAW"
    w="SCOREBOARD"
    l0=Label(scoreboards,text=w,height=3,font=("COMIC SANS MS",20,"underline"),bg="pink",fg="white")
    l0.pack()
    l1=Label(scoreboards,text=z,height=3,font=("COMIC SANS MS",20,"bold"),bg="pink",fg="white")
    l1.pack()
    l2=Label(scoreboards,text=y,height=3,font=("COMIC SANS MS",20,"bold"),bg="pink",fg="white")
    l2.pack()
    l3=Label(scoreboards,text=x,height=3,font=("COMIC SANS MS",20,"bold"),bg="pink",fg="white")
    l3.pack()
    endbutton=Button(scoreboards,text="Finish Game",font=("COMIC SANS MS",20,"bold"),command=gamefinish)
    endbutton.pack()
    newgamebutton=Button(scoreboards,text="New Game",font=("COMIC SANS MS",20,"bold"),command=newgame)
    newgamebutton.pack()
#Displays the winning condition
def displayWinner(winner):
    global winnerWindow    
    winnerWindow=Tk()
    winnerWindow.title("Winner Window")
    winnerWindow.configure(bg="violet")
    l1=Label(winnerWindow,text="GAME: ",font=("COMIC SANS MS",25,"underline"),bg="violet",fg="White")
    l1.pack()
    l2=Label(winnerWindow,text=str(score1+score2+draw),font=("COMIC SANS MS",25),bg="violet",fg="White")
    l2.pack()
    l3=Label(winnerWindow,text="THE WINNER IS: ",font=("COMIC SANS MS",25,"underline"),bg="violet",fg="White")
    l3.pack()
    l4=Label(winnerWindow,text=winner,font=("COMIC SANS MS",25),bg="violet",fg="White")
    l4.pack()
    lsc=Label(winnerWindow,text="SCORES",font=("COMIC SANS MS",25,"underline"),bg="violet",fg="White")
    lsc.pack()
    l5=Label(winnerWindow,text="X: ",font=("COMIC SANS MS",25),bg="violet",fg="White")
    l5.pack()
    l6=Label(winnerWindow,text=str(score1),font=("COMIC SANS MS",25),bg="violet",fg="White")
    l6.pack()
    l7=Label(winnerWindow,text="O: ",font=("COMIC SANS MS",25),bg="violet",fg="White")
    l7.pack()
    l8=Label(winnerWindow,text=str(score2),font=("COMIC SANS MS",25),bg="violet",fg="White")
    l8.pack()
    bproceed=Button(winnerWindow,text="Proceed",font=("COMIC SANS MS",20,"bold"),command=renew)
    bproceed.pack()
#Checks for the winner        
def checkWinner():
    global count,board,score1,score2,draw
    if (board[0][0]==board[0][1]==board[0][2]==board[0][3]=="X" or board[1][0]==board[1][1]==board[1][2]==board[1][3]=="X" or board[2][0]==board[2][1]==board[2][2]==board[2][3]=="X" or board[3][0]==board[3][1]==board[3][2]==board[3][3]=="X" or 
        board[0][0]==board[1][0]==board[2][0]==board[3][0]=="X" or board[0][1]==board[1][1]==board[2][1]==board[3][1]=="X" or board[0][2]==board[1][2]==board[2][2]==board[3][2]=="X" or board[0][3]==board[1][3]==board[2][3]==board[3][3]=="X" or
        board[0][0]==board[1][1]==board[2][2]==board[3][3]=="X" or board[0][3]==board[1][2]==board[2][1]==board[3][0]=="X"):
            score1+=1
            
            displayWinner("X")
            
    elif (board[0][0]==board[0][1]==board[0][2]==board[0][3]=="O" or board[1][0]==board[1][1]==board[1][2]==board[1][3]=="O" or board[2][0]==board[2][1]==board[2][2]==board[2][3]=="O" or board[3][0]==board[3][1]==board[3][2]==board[3][3]=="O" or  
          board[0][0]==board[1][0]==board[2][0]==board[3][0]=="O" or board[0][1]==board[1][1]==board[2][1]==board[3][1]=="O" or board[0][2]==board[1][2]==board[2][2]==board[3][2]=="O" or board[0][3]==board[1][3]==board[2][3]==board[3][3]=="O" or
          board[0][0]==board[1][1]==board[2][2]==board[3][3]=="O" or board[0][3]==board[1][2]==board[2][1]==board[3][0]=="O"):
            score2+=1
            
            displayWinner("O")
            
    elif count==16:
        draw+=1
        displayWinner("IT'S A DRAW")  
def reset():
    global board,buttons,count
    count=0
    board=[
           ["","","",""],
           ["","","",""],
           ["","","",""],
           ["","","",""],
           ]
    for b in buttons:
        b["text"]=""
    l1=Label(t,text="PLAYER: 1(X)",height=3,font=("COMIC SANS MS",10,"bold"),bg="white")
    l1.grid(row=0,column=0)
#Changes the value of the button
def changeVal(button,boardValRow,boardValCol):
    global count

    #Checking if button is available
    #if even count(0,2,4), It's X to play, else O
    if button["text"]=="":
        if count%2==0:
            button["text"]="X"
            l1=Label(t,text="PLAYER: 2(O)",height=3,font=("COMIC SANS MS",10,"bold"),bg="white").grid(row=0,column=0)
            board[boardValRow][boardValCol]="X"
        else:
            button["text"]="O"
            l1=Label(t,text="PLAYER: 1(X)",height=3,font=("COMIC SANS MS",10,"bold"),bg="white").grid(row=0,column=0)
            board[boardValRow][boardValCol]="O"
        count=count+1
        if count>=7:
            checkWinner()
    else:
        messagebox.showerror("Error","This box already has a value!")

#Displays the GUI 
def TicTacToeGUI():
    global t#main window
    
    t=Tk()#Creates a window
    t.title("TIC TAC TOE")
    t.configure(bg="white")  #Making the background of the window as white
    #Displaying the player
    l1=Label(t,text="PLAYER: 1(X)",height=3,font=("COMIC SANS MS",10,"bold"),bg="white")
    l1.grid(row=0,column=0)
    #Rule button
    ruleButton=Button(t,text="Rules",command=Rule,font=("COMIC SANS MS",10,"bold"))
    ruleButton.grid(row=0,column=2)
    #Quit button
    exitButton=Button(t,text="Quit",command=Quit,font=("COMIC SANS MS",10,"bold"))
    exitButton.grid(row=0,column=3)
    
    global buttons
    #Grid buttons
    b1=Button(t,text="",height=4,width=8,bg="mediumvioletred",activebackground="white",fg="white",font="Times 15 bold",command=lambda: changeVal(b1,0,0))
    b2=Button(t,text="",height=4,width=8,bg="mediumvioletred",activebackground="white",fg="white",font="Times 15 bold",command=lambda: changeVal(b2,0,1))
    b3=Button(t,text="",height=4,width=8,bg="mediumvioletred",activebackground="white",fg="white",font="Times 15 bold",command=lambda: changeVal(b3,0,2))
    b4=Button(t,text="",height=4,width=8,bg="mediumvioletred",activebackground="white",fg="white",font="Times 15 bold",command=lambda: changeVal(b4,0,3))
    b5=Button(t,text="",height=4,width=8,bg="deeppink",activebackground="white",fg="white",font="Times 15 bold",command=lambda: changeVal(b5,1,0))
    b6=Button(t,text="",height=4,width=8,bg="deeppink",activebackground="white",fg="white",font="Times 15 bold",command=lambda: changeVal(b6,1,1))
    b7=Button(t,text="",height=4,width=8,bg="deeppink",activebackground="white",fg="white",font="Times 15 bold",command=lambda: changeVal(b7,1,2))
    b8=Button(t,text="",height=4,width=8,bg="deeppink",activebackground="white",fg="white",font="Times 15 bold",command=lambda: changeVal(b8,1,3))
    b9=Button(t,text="",height=4,width=8,bg="hotpink",activebackground="white",fg="white",font="Times 15 bold",command=lambda: changeVal(b9,2,0))
    b10=Button(t,text="",height=4,width=8,bg="hotpink",activebackground="white",fg="white",font="Times 15 bold",command=lambda: changeVal(b10,2,1))
    b11=Button(t,text="",height=4,width=8,bg="hotpink",activebackground="white",fg="white",font="Times 15 bold",command=lambda: changeVal(b11,2,2))
    b12=Button(t,text="",height=4,width=8,bg="hotpink",activebackground="white",fg="white",font="Times 15 bold",command=lambda: changeVal(b12,2,3))
    b13=Button(t,text="",height=4,width=8,bg="pink",activebackground="white",fg="white",font="Times 15 bold",command=lambda: changeVal(b13,3,0))
    b14=Button(t,text="",height=4,width=8,bg="pink",activebackground="white",fg="white",font="Times 15 bold",command=lambda: changeVal(b14,3,1))
    b15=Button(t,text="",height=4,width=8,bg="pink",activebackground="white",fg="white",font="Times 15 bold",command=lambda: changeVal(b15,3,2))
    b16=Button(t,text="",height=4,width=8,bg="pink",activebackground="white",fg="white",font="Times 15 bold",command=lambda: changeVal(b16,3,3))
    #Command is what it should execute once clicked. Lambda is the function and it's calling changeVal.
    buttons=[b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16]
    b1.grid(row=2,column=0)
    b2.grid(row=2,column=1)
    b3.grid(row=2,column=2)
    b4.grid(row=2,column=3)
    b5.grid(row=3,column=0)
    b6.grid(row=3,column=1)
    b7.grid(row=3,column=2)
    b8.grid(row=3,column=3)
    b9.grid(row=4,column=0)
    b10.grid(row=4,column=1)
    b11.grid(row=4,column=2)
    b12.grid(row=4,column=3)
    b13.grid(row=5,column=0)
    b14.grid(row=5,column=1)
    b15.grid(row=5,column=2)
    b16.grid(row=5,column=3)

    
TicTacToeGUI()#starts everything
