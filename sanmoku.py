from mimetypes import init
import random

GameBoard = [0,1,2,3,4,5,6,7,8] #〇 = 9 ✕ = 10とする
playerflag = 0
num = 0

def initBoard():
    global GameBoard, playerflag, num
    GameBoard = [0,1,2,3,4,5,6,7,8] #〇 = 9 ✕ = 10とする
    playerflag = 0
    num = 0
 

def check():
    global num
    winning = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    
    for item in winning:
          if GameBoard[item[0]] == GameBoard[item[1]] and GameBoard[item[0]] == GameBoard[item[2]]:
              return GameBoard[item[0]]
          
    if num == 8:
      return 11  
    return None    

def move(pos, type):
    if (pos < 0 or 8 < pos): #入力値チェック
        print(pos)
        raise ValueError("error!")
    
    if (type < 9 or 10 < type): #入力値チェック
        print(type)
        raise ValueError("error!")

    GameBoard[pos] = type
        
def randomChoise():
    while True:
        choisepos = random.randint(0,8)
        if 0 <= GameBoard[choisepos] <= 8:
            return choisepos
  
def playGame():
    global playerflag,num
    while True:
        choise = randomChoise()
        move(choise, playerflag + 9)
        a = check()
        if a is not None:
            print(GameBoard)
            if a == 9:
                print("〇の勝利")
            elif a == 10:
                print("✕の勝利")
            else:
                print("引き分け")
            return None
        if playerflag == 0:
            playerflag = 1
        else:
            playerflag = 0
        num += 1
        

for i in range(0,30):
    initBoard()
    playGame()

