from tkinter import *

root = Tk()

label = Label(root, text = "검은색 턴")
label.grid(row = 0, column = 0)


row = 19
col = 19

turn = True
gameEnd = False

isClicked = []
buttons = []

dy = [-1, -1, 0, 1]
dx = [0, 1, 1, 1]


def inRange(y, x):
    """
    코딩해봅시다.
    해당 좌표가 오목판 안에 존재하면 True 리턴
    """
    return 

def isGameEnd(color):
    global gameEnd
    for y in range(row):
        for x in range(col):
            for d in range(4):
                yend = y + dy[d] * 4
                xend = x + dx[d] * 4
                if inRange(yend, xend):
                    """
                    코딩해봅시다.
                    반복문을 이용해 다섯개가 놓였다면 True 리턴
                    gameEnd를 True로

                    """


                    
    return False

def makeOnClick(i, j):

    def onClick():
        if isClicked[i][j] != 0 or gameEnd:
            return

        global turn        
        if turn:
            isClicked[i][j] = 1;
            buttons[i][j].configure(bg = "black")
            label.configure(text = "하얀색 턴")
            if isGameEnd(1):
                label.configure(text = "검정색 승리!!")
                
                
            
        else:
            isClicked[i][j] = 2;
            buttons[i][j].configure(bg = "white")
            label.configure(text = "검정색 턴")
            if isGameEnd(2):
                label.configure(text = "하얀색 승리!!")
        turn = not turn
    return onClick



for i in range(row):
    isClicked.append([])
    buttons.append([])
    for j in range(col):
        """ 구현해봅시다.
        0(아직 놓지않음)으로 isClicked 리스트를 채워주고
        버튼을 height 1, width 2, 배경색 gray로 생성하여
        (i, j + 1) 좌표로 grid를 이용해 배치하고
        onClick 이벤트 추가"""
        
        




root.mainloop()



