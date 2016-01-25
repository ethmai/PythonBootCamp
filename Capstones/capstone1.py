#Tic Tac Toe

#creating a board

board = ['a1','a2','a3','b1','b2','b3','c1','c2','c3']

for x in range(3):
    board.append(["|__"] * 3)

def print_board(board):
    for row in board:
        print " ".join(row)

print "Let's play Tic Toc Toe!"
print_board(board)

"""
for turn in range(5)
    your_row = raw_input("Enter your row (1, 2, or 3): ")
    your_col = raw_input("Enter your column (1, 2, or 3): ")

"""
# Everything from here on should go in your for loop!
# Be sure to indent four spaces!

"""
for turn in range(4):
    print "Your turn is: "
    print (turn + 1)
    guess_row = int(raw_input("Guess Row:"))
    guess_col = int(raw_input("Guess Col:"))

    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk my battleship!"
        break

    if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
        print "Oops, that's not even in the ocean."
        if turn >=3:
            print "Game Over."
    elif board[guess_row][guess_col] == "X":
        print "You guessed that one already."
        if turn >=3:
            print "Game Over."
    else:
        print "You missed my battleship!"
        board[guess_row][guess_col] = "X"
# Print (turn + 1) here!
        print print_board(board)
        if turn >=3:
            print "Game Over"
"""