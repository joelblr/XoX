
# array: list[str]
def check(array) :
    if array[0] == "X" :
        return (1, 1)
    return (1, 0)


# board: dict[int] = list[str]
def board_validate(board) :

    diagonal1 = board[0][0] + board[1][1] + board[2][2]
    if diagonal1 in ["XXX", "OOO"] :
        return check(diagonal1)

    diagonal2 = board[0][2] + board[1][1] + board[2][0]
    if diagonal2 in ["XXX", "OOO"] :
        return check(diagonal2)

    flag = False
    for i in board :

        row = "".join(board[i])
        if row in ["XXX", "OOO"] :
            return check(row)

        col = board[0][i] + board[1][i] + board[2][i]
        if col in ["XXX", "OOO"] :
            return check(col)

        if "." in row :
            flag = True

    if flag :
        return (0, 0)

    return (0, 1)


def printBoard(board) :
    for i in board :
        print("\t%s" % ("."*19))
        print("\t|  %s  |  %s  |  %s  |" % (board[i][0], board[i][1], board[i][2]))
    print("\t%s" % ("."*19))


def printWinner(winner) :
    if winner[0] :
        print(">"*35)
        print("The Winner is X") if winner[1] else print("The Winner is O")
        print("<"*35, "\n")
        exit()

    if winner[1] :
        print("="*35)
        print("It's a Draw !")
        print("="*35, "\n")
        exit()


if __name__ == "__main__" :

    board = {
        0 : [".", ".", "."],
        1 : [".", ".", "."],
        2 : [".", ".", "."],
        }

    print()
    printBoard(board)

    turn = 1
    moves = set()
    while True :

        print("-"*35)
        print("X", end = " ") if turn else print("O", end = " ")
        print("to Play.")

        row, col = map(int, input("Enter Row, Column : ").split())
        if (row, col) in moves or not (0 <= row < 3 and 0 <= col < 3) :
            if (row, col) in moves :  print("Same Input, Try Again !")
            else :  print("Wrong Input, Try Again !")
            continue

        moves.add( (row, col))
        board[row][col] = "X" if turn % 2 else "O"

        printBoard(board)
        winner = board_validate(board)
        printWinner(winner)

        turn ^= 1

