class Player:

    def __init__(self, player, token):
        self.player = player
        self.token = token 


class Game:

    def __init__(self):
        self.board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']

    def __str__(self):
        print(self.board[0] + '|' + self.board[1] + '|' + self.board[2] + '|' )
        print(self.board[3] + '|' + self.board[4] + '|' + self.board[5] + '|' )
        print(self.board[6] + '|' + self.board[7] + '|' + self.board[8] + '|' )



test = Game()

print(test)