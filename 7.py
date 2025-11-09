#Tic Toc Toe
theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

def printBoard(board):
    print(board['top-L'] + ' | ' + board['top-M'] + ' | ' + board['top-R'])
    print('- + - + -')
    print(board['mid-L'] + ' | ' + board['mid-M'] + ' | ' + board['mid-R'])
    print('- + - + -')
    print(board['low-L'] + ' | ' + board['low-M'] + ' | ' + board['low-R'])

def checkWinner(board, turn):
    winConditions = [
        ['top-L', 'top-M', 'top-R'],
        ['mid-L', 'mid-M', 'mid-R'],
        ['low-L', 'low-M', 'low-R'],
        ['top-L', 'mid-L', 'low-L'],
        ['top-M', 'mid-M', 'low-M'],
        ['top-R', 'mid-R', 'low-R'],
        ['top-L', 'mid-M', 'low-R'],
        ['top-R', 'mid-M', 'low-L']
    ]
    for condition in winConditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == turn:
            return True
    return False

turn = 'X'
for i in range(9):
    printBoard(theBoard)
    print('Turn for ' + turn + '. Move on which space? (e.g., top-L, mid-M)')
    move = input()
    if move in theBoard and theBoard[move] == ' ':
        theBoard[move] = turn
        if checkWinner(theBoard, turn):
            printBoard(theBoard)
            print('Player ' + turn + ' wins!')
            break
        turn = 'O' if turn == 'X' else 'X'
    elif move in theBoard and theBoard[move] != ' ':
        print('That space is already taken. Try again.')
    else:
        print('Invalid move. Please enter a valid space.')
else:
    printBoard(theBoard)
    print("It's a draw!")
#water jug problem
print("enter jug problem")
x = int(input("enter x: "))
y = int(input("enter y: "))
while true:
    rno = int(input("enter the rule no: "))
if rno == 1:
    if x < 4:
     x = 4
if rno == 2:
    if y < 3:
     y = 3
if rno == 5:
    if x > 0:
     x = 0
if rno == 6:
    if y > 0:
     y = 0
if rno == 7:
    if x + y < = 4 & y > o:
     x,y = 4,y-(4-x)
if rno == 8:
    if  x + y > = 3 & x > o:
     x,y = x-(3-y),3
if rno == 9:
    if x + y < = 4 & y > o:
     x,y = x + y,0
if rno == 10:
    if  x + y < = 3 & x > o:
     x,y = 0,x + y
print(f"current state: x={x},y={y}")