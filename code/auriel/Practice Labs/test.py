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

    def move(self, player, token):
        moves = {'top left'       :  0,
                 'top middle'     :  1,
                 'top right'      :  2,
                 'left middle'    :  3,
                 'middle'         :  4,
                 'right middle'   :  5,
                 'bottom left'    :  6,
                 'bottom middle'  :  7,
                 'bottom right'   :  8,
        }

        user_move = input(f'Where would you like to place {token}')
        user_move = moves[user_move]
        self.board[user_move] = token
        return self.board



