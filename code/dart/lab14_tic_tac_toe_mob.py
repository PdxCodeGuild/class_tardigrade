
class Player: # ask player for their name and token
    def __init__(self, name, token):
        self.name = name
        self.token = token

class Game: # use this dictionary for the keys and values during the game
    def __init__(self):
        self.board = {"1": " ", "2": " ", "3": " ",
                      "4": " ", "5": " ", "6": " ",
                      "7": " ", "8": " ", "9": " "}

    def __repr__(self, board): # returns pretty string representation of game board
        print("  ", board["1"], "  |","  " ,board["2"], "  |", "  ",board["3"], "        1 | 2 | 3")
        print("-------+--------+--------")
        print("  ", board["4"], "  |","  " ,board["5"], "  |", "  ",board["6"], "        4 | 5 | 6")
        print("-------+--------+--------")
        print("  ", board["7"], "  |","  " ,board["8"], "  |", "  ",board["9"], "        7 | 8 | 9", "\n")

    def calc_winner(self, board):
        check = " "
        if board["1"] == board["2"] == board["3"] != " " : # row 1
           check = "win"
        elif board["4"] == board["5"] == board["6"] != " ": # row 2
           check = "win"
        elif board["7"] == board["8"] == board["9"] != " ": # row 3
           check = "win"
        elif board["1"] == board["4"] == board["7"] != " ": # column 1
           check = "win"
        elif board["2"] == board["5"] == board["8"] != " ": # column 2
           check = "win"
        elif board["3"] == board["6"] == board["9"] != " ": # column 3
           check = "win"
        elif board["7"] == board["5"] == board["3"] != " ": # diagnal forward slash
           check = "win"
        elif board["1"] == board["5"] == board["9"] != " ": # diagnal back slash
          check = "win"
        return check

