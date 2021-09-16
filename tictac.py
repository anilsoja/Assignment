import random

board = [' ' for x in range(10)]


def display_board():
    print(board[7] + '|' + board[8] + '|' + board[9])
    print(' ---')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print(' ---')
    print(board[1] + '|' + board[2] + '|' + board[3])



def check_winner(board, in_value):
    # winning_combos = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6],
    #                    [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6], ]

    return ((board[7] == in_value and board[8] == in_value and board[9] == in_value) or
            (board[4] == in_value and board[5] == in_value and board[6] == in_value) or
            (board[1] == in_value and board[2] == in_value and board[3] == in_value) or
            (board[7] == in_value and board[4] == in_value and board[1] == in_value) or
            (board[8] == in_value and board[5] == in_value and board[2] == in_value) or
            (board[9] == in_value and board[6] == in_value and board[3] == in_value) or
            (board[7] == in_value and board[5] == in_value and board[3] == in_value) or
            (board[9] == in_value and board[5] == in_value and board[1] == in_value))

def is_board_full(board):
    for item in board:
        if " " in item:
            return False
    return True


def insertLetter(letter, pos):
    if board[pos] == " ":
        board[pos] = letter


def choice(v):
    if v == 'X':
        return 'O'
    else:
        return 'X'


def main():
    global x
    players = ["X", "O"]
    turn = 0
    x = input("Enter your Choice X or O:")
    y = choice(x)
    while not is_board_full(board):
        print("\n")
        display_board()
        if turn == 0:
            print("\n")
            p1 = int(input("Enter the position:"))
            insertLetter(x, p1)
            # display_board()
        else:
            p2 = (random.randint(1, 9))
            print("Choice:", y , "position:", p2)
            insertLetter(y, p2)

        # Check if the player won
        s = check_winner(board, x)
        t = check_winner(board, y)
        if s == True:
            print("Player wins")
            display_board()
        elif s == True:
            print("Computer wins")
            display_board()
        else:
            print("Its Tie")
            display_board()

        # Select the next player
        turn = 1 - turn


main()
