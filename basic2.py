#!/usr/bin/python3

#TODO : Convert 2D to 1D Board
#TODO : Score Board
#TODO : Two-Player or AI
#TODO : GUI


class XOX :

    def __init__(self) :
        #board: dict[int] = list[str]
        self.board = { 0 : [".", ".", "."], 1 : [".", ".", "."], 2 : [".", ".", "."]}
        self.moves = set()
        self.turn = 1

    # array: list[str]
    def check(self, array) :
        if array[0] == "X" :
            return (1, 1)
        return (1, 0)


    def board_validate(self) :

        diagonal1 = self.board[0][0] + self.board[1][1] + self.board[2][2]
        if diagonal1 in ["XXX", "OOO"] :
            return self.check(diagonal1)

        diagonal2 = self.board[0][2] + self.board[1][1] + self.board[2][0]
        if diagonal2 in ["XXX", "OOO"] :
            return self.check(diagonal2)

        flag = False
        for i in self.board :

            row = "".join( self.board[i])
            if row in ["XXX", "OOO"] :
                return self.check(row)

            col = self.board[0][i] + self.board[1][i] + self.board[2][i]
            if col in ["XXX", "OOO"] :
                return self.check(col)

            if "." in row :
                flag = True

        if flag :
            return (0, 0)

        return (0, 1)


    def board_update(self) :

        print("-"*35)
        print("X", end = " ") if self.turn else print("O", end = " ")
        print("to Play.")

        try :
            row, col = map(int, input("Enter Row, Column : ").split())
        except :
            print("\nWrong Input, Try Again !")
            return self.board_update()

        if (row, col) in self.moves or not (0 <= row < 3 and 0 <= col < 3) :
            if (row, col) in self.moves :  print("Same Input, Try Again !")
            else :  print("Wrong Input, Try Again !")
            return self.board_update()

        self.moves.add( (row, col))
        self.board[row][col] = "X" if self.turn else "O"
        self.turn ^= 1

        return


    def printBoard(self) :

        print()
        for i in self.board :
            print("\t%s" % ("."*19))
            t = tuple(self.board[i][j] for j in range(3))
            print("\t|  %s  |  %s  |  %s  |" % t)
        print("\t%s" % ("."*19))

        return


    def printWinner(self) :

        winner = self.board_validate()

        if winner[0] :
            print(">"*35)
            print("The Winner is X") if winner[1] else print("The Winner is O")
            print("<"*35, "\n")
            return 1

        if winner[1] :
            print("="*35)
            print("It's a Draw !")
            print("="*35, "\n")
            return 1

        return 0


if __name__ == "__main__" :

    game = XOX()

    game.printBoard()
    while True :

        game.board_update()
        game.printBoard()
        if game.printWinner() :
            break



# pyinstaller.exe --onefile --windowed --icon=app.ico app.py --name=app
