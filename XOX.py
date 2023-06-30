#!/usr/bin/python3


#TODO : Score Board
#TODO : Two-Player-Network or AI
#TODO : GUI


class Fg :
    BLACK   = '\033[30m'
    RED     = '\033[31m'
    GREEN   = '\033[32m'
    YELLOW  = '\033[33m'
    BLUE    = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN    = '\033[36m'
    WHITE   = '\033[37m'
    RESET   = '\033[39m'

class Bg :
    BLACK   = '\033[40m'
    RED     = '\033[41m'
    GREEN   = '\033[42m'
    YELLOW  = '\033[43m'
    BLUE    = '\033[44m'
    MAGENTA = '\033[45m'
    CYAN    = '\033[46m'
    WHITE   = '\033[47m'
    RESET   = '\033[49m'

class Style :
    BRIGHT    = '\033[1m'
    DIM       = '\033[2m'
    NORMAL    = '\033[22m'
    RESET = '\033[0m'


class Text_Modify() :

    def __init__(self) :

        self.design = {
                        "fg"  : Fg(),
                        "bg"  : Bg(),
                        "stl" : Style(),
                    }

        self.m1 = self.modify_1()
        self.m2 = self.modify_2()
        self.m3 = self.modify_3()
        self.m4 = self.modify_4()
        self.mX = self.modify_X()
        self.mO = self.modify_O()
        self.mN = self.modify_N


    def modify_X(self) :
        return  self.design["stl"].BRIGHT + self.design["fg"].BLUE + "X" +\
                self.design["fg"].RESET + self.design["stl"].RESET

    def modify_O(self) :
        return  self.design["stl"].BRIGHT + self.design["fg"].GREEN + "O" +\
                self.design["fg"].RESET + self.design["stl"].RESET

    def modify_N(self, text) :
        return  self.design["stl"].BRIGHT + self.design["fg"].RED + text +\
                self.design["fg"].RESET + self.design["stl"].RESET

    def modify_1(self) :
        return  self.design["stl"].BRIGHT + self.design["fg"].YELLOW + "|  " +\
                self.design["fg"].RESET + self.design["stl"].RESET

    def modify_2(self) :
        return  self.design["stl"].BRIGHT + self.design["fg"].YELLOW + "  |  " +\
                self.design["fg"].RESET + self.design["stl"].RESET

    def modify_3(self) :
        return  self.design["stl"].BRIGHT + self.design["fg"].YELLOW + "  |" +\
                self.design["fg"].RESET + self.design["stl"].RESET

    def modify_4(self) :
        return  self.design['stl'].BRIGHT + self.design['fg'].YELLOW +\
                "|-----|-----|-----|" +\
                self.design['fg'].RESET + self.design['stl'].RESET


import os
class XOX() :

    def __init__(self) :

        self.tm = Text_Modify()
        self.turn = 1

        self.xox = {
                        "X" : 0,
                        "O" : 0,
                    }
        self.board = {
                        0 : ["1", "2", "3"],
                        1 : ["4", "5", "6"],
                        2 : ["7", "8", "9"],
                    }
        self.plot = {
                        1 : (0,0), 2 : (0,1), 3 : (0,2),
                        4 : (1,0), 5 : (1,1), 6 : (1,2),
                        7 : (2,0), 8 : (2,1), 9 : (2,2),
                    }
        self.check = {
                        "row" : {
                            "X" : [0, 0, 0],
                            "O" : [0, 0, 0],
                        },
                        "column" : {
                            "X" : [0, 0, 0],
                            "O" : [0, 0, 0],
                        },
                        "diagonal" : {
                            "X" : [0, 0],
                            "O" : [0, 0],
                        },
                    }


    def xox_update(self, row, col, who) :

        self.check["row"][who][row] += 1
        self.check["column"][who][col] += 1
        if row == col == 1 :
            self.check["diagonal"][who][0] += 1
            self.check["diagonal"][who][1] += 1
        elif row == col :
            self.check["diagonal"][who][0] += 1
        elif row + col == 2 :
            self.check["diagonal"][who][1] += 1


    def board_update(self) :

        print("-"*35)
        print(f"{self.tm.mX}", end = " ") if self.turn else print(f"{self.tm.mO}", end = " ")
        print("to Play.")

        try :
            num = int( input(f"Enter a {self.tm.mN('Number')} : "))
            if (num < 1 or num > 9) :
                raise IOError

        except IOError :
            print("Out of Bounce: Numbers 1 to 9 only!")
            return self.board_update()

        except ValueError :
            print("Wrong Number: Numbers 1 to 9 only!")
            return self.board_update()

        except (KeyboardInterrupt, EOFError) :
            print("\nPlz Play: Numbers 1 to 9, Ezy.")
            return self.board_update()

        row, col = self.plot.get(num)
        if self.board[row][col] in ["X", "O"] :
            print("Same Number, Try Again !")
            return self.board_update()

        self.board[row][col] = "X" if self.turn else "O"
        self.xox_update(row, col, self.board[row][col])
        self.turn ^= 1

        return


    def board_print(self) :

        print()
        for idx in range(3) :
            row = tuple( self.board[idx])
            print("\t|-----|-----|-----|")
            print("\t|  %s  |  %s  |  %s  |" % row)
        print("\t|-----|-----|-----|")
        print()

        return


    # define our clear function
    def clear_screen(self) :
        # for windows
        if os.name == 'nt' :
            os.system('cls')
        # for mac and linux(here, os.name is 'posix')
        else :
            os.system('clear')


    def board_design(self) :

        self.clear_screen()

        print()
        for i in range(3) :

            row = []
            for j in range(3) :
                if self.board[i][j] == "X" :
                    row += [ self.tm.mX]

                elif self.board[i][j] == "O" :
                    row += [ self.tm.mO]

                else :
                    row += [ self.tm.mN( self.board[i][j])]

            row = tuple(row)
            print("\t" + self.tm.m4)
            print(f"\t{self.tm.m1}{f'{self.tm.m2}'.join(row)}{self.tm.m3} ")

        print("\t" + self.tm.m4)
        print()

        # print()
        # for i in range(3) :

        #     row = []
        #     for j in range(3) :
        #         if self.board[i][j] == "X" :
        #             row += [ self.tm.modify_X()]

        #         elif self.board[i][j] == "O" :
        #             row += [ self.tm.modify_O()]

        #         else :
        #             row += [ self.tm.modify_N( self.board[i][j])]

        #     row = tuple(row)
        #     print("\t" + c4)
        #     print(f"\t{c1}{f'{c2}'.join(row)}{c3} ")

        # print("\t" + c4)
        # print()

        return


    def xox_check(self, name, who, idx) :
        for i in idx :
            if self.check[name][who][i] == 3 :
                self.check[name][who][i] = 0
                self.xox[who] += 1


    def board_check(self, who) :

        self.xox_check("row", who, [0, 1, 2])
        self.xox_check("column", who, [0, 1, 2])
        self.xox_check("diagonal", who, [0, 1])

        if self.xox[who] >= 1 :
            return [True, True]
        if sum( self.check["row"]["X"]) + sum( self.check["row"]["O"]) == 9 :
            return [False, True]
        return [False]


    def winner_print(self) :

        winner = self.board_check("X" if self.turn^1 else "O")

        if winner.pop() :
            import time
            if winner.pop() :
                print(">"*35)
                print(f"The Winner is: {self.tm.mX}") if self.turn^1\
                        else print(f"The Winner is: {self.tm.mO}")
                print("<"*35, "\n")

            else :
                print("="*35)
                print(f"It's a { self.tm.mN('Draw')} !")
                print("="*35, "\n")

            time.sleep(5)
            return True

        return False


if __name__ == "__main__" :

    game = XOX()

    # game.board_print()
    game.board_design()
    while True :

        game.board_update()
        # game.board_print()
        game.board_design()
        if game.winner_print() :
            break


# pyinstaller.exe --onefile --windowed --icon=app.ico app.py --name=app

