def main():
# The main function
    introduction = intro()
    board = create_grid()
    pretty = printPretty(board)
    symbol_1, symbol_2 = sym()
    full = isFull(board, symbol_1, symbol_2) # The function that starts the game is also in here.
    

    


def intro():
# This function introduces the rules of the game Tic Tac Toe
    print("chào mừng chúng m đã đến với trò chơi bóng tối")
    print("\n")
    print("ko bt luật thì treo cổ đi")
    print("\n")
    input("ấn enter để chơi")
    print("\n")



def create_grid():
# This function creates a blank playboard
    print("bảng : ")
    board = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]        
    return board



def sym():
# This function decides the players' symbols
    symbol_1 = input("ng chơi 1, m muốn chọn X hay O ")
    if symbol_1 == "X":
        symbol_2 = "O"
        print("thg 2, m là O. ")
    else:
        symbol_2 = "X"
        print("thg 2, m là X. ")
    input("ấn enter để tiếp tục.")
    print("\n")
    return (symbol_1, symbol_2)



def startGamming(board, symbol_1, symbol_2, count):
# This function starts the game.

    # Decides the turn
    if count % 2 == 0:
        player = symbol_1
    elif count % 2 == 1:
        player = symbol_2
    print("thg "+ player + "đến m đánh. ")
    row = int(input("chọn hàng:"
                    "[hàng trên cùng: ấn 0, hàng giữa: ấn 1, đáy: ấn 2]:"))
    column = int(input("chọn cột "
                       "[trái: ấn 0, giữa: ấn 1, phải ấn 2]"))


    # Check if players' selection is out of range
    while (row > 2 or row < 0) or (column > 2 or column < 0):
        outOfBoard(row, column)
        row = int(input("chọn hàng[trên:"
                        "[ấn 0, giữa: ấn 1, đáy: ấn 2]:"))
        column = int(input("chọn cột:"
                            "[trái: ấn 0, giữa: ấn 1, phải : ấn 2]"))

        # Check if the square is already filled
    while (board[row][column] == symbol_1)or (board[row][column] == symbol_2):
        filled = illegal(board, symbol_1, symbol_2, row, column)
        row = int(input("chọn hàng[trên:"
                        "[ấn 0, giữa: ấn 1, đáy: ấn 2]:"))
        column = int(input("chọn cột:"
                            "[trái: ấn 0, giữa: ấn 1, phải : ấn 2]"))    
        
    # Locates player's symbol on the board
    if player == symbol_1:
        board[row][column] = symbol_1
            
    else:
        board[row][column] = symbol_2
    
    return (board)



def isFull(board, symbol_1, symbol_2):
    count = 1
    winner = True
# This function check if the board is full
    while count < 10 and winner == True:
        gaming = startGamming(board, symbol_1, symbol_2, count)
        pretty = printPretty(board)
        
        if count == 9:
            print("đầy bảng r")
            if winner == True:
                print("hoà ")

        # Check if here is a winner
        winner = isWinner(board, symbol_1, symbol_2, count)
        count += 1
    if winner == False:
        print("thua")
        
    # This is function gives a report 
    report(count, winner, symbol_1, symbol_2)



def outOfBoard(row, column):
# This function tells the players that their selection is out of range
    print("vị trí ko hợp lệ, chọn lại ")
    
    

def printPretty(board):
# This function prints the board nice!
    rows = len(board)
    cols = len(board)
    print("---+---+---")
    for r in range(rows):
        print(board[r][0], " |", board[r][1], "|", board[r][2])
        print("---+---+---")
    return board



def isWinner(board, symbol_1, symbol_2, count):
# This function checks if any winner is winning
    winner = True
    # Check the rows
    for row in range (0, 3):
        if (board[row][0] == board[row][1] == board[row][2] == symbol_1):
            winner = False
            print("số " + symbol_1 + "m thắng")
   
        elif (board[row][0] == board[row][1] == board[row][2] == symbol_2):
            winner = False
            print("số " + symbol_2 + "m thắng")
            
            
    # Check the columns
    for col in range (0, 3):
        if (board[0][col] == board[1][col] == board[2][col] == symbol_1):
            winner = False
            print("số " + symbol_1 + ", m thắng")
        elif (board[0][col] == board[1][col] == board[2][col] == symbol_2):
            winner = False
            print("số " + symbol_2 + ", m thắng")

    # Check the diagnoals
    if board[0][0] == board[1][1] == board[2][2] == symbol_1:
        winner = False 
        print("số " + symbol_1 + ", m thắng")

    elif board[0][0] == board[1][1] == board[2][2] == symbol_2:
        winner = False
        print("số " + symbol_2 + ", m thắng")

    elif board[0][2] == board[1][1] == board[2][0] == symbol_1:
        winner = False
        print("số " + symbol_1 + "m thắng")

    elif board[0][2] == board[1][1] == board[2][0] == symbol_2:
        winner = False
        print("số " + symbol_2 + ", m thắng")

    return winner
    


def illegal(board, symbol_1, symbol_2, row, column):
    print("ô m chọn bị điền r")

    
def report(count, winner, symbol_1, symbol_2):
    print("\n")
    input("ấn enter để xem tỉ số ")
    if (winner == False) and (count % 2 == 1 ):
        print("ng win : số " + symbol_1 + ".")
    elif (winner == False) and (count % 2 == 0 ):
        print("ng win : số " + symbol_2 + ".")
    else:
        print("hoà.")
# Call Main
main()
