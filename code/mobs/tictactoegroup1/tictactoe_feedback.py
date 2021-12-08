'''
Tic Tac Toe mob
Authors: Dart, Travis, Auriel, Alnardo
Date:

'''

print("\t--------------------------------")
print("\t|         Tic Tac Toe          |")
print("\t--------------------------------")


class Player:

    def __init__(self, player, token):
        
        self.player = player
        self.token = token

    def __str__(self):
        return f"{self.player} is {self.token}."
        

# player1 = Player('Auriel', 'X')


class Game:

    def __init__(self):
        self.board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']

    def __str__(self):
        return   f"{self.board[0]}  |  {self.board[1]}  |  {self.board[2]}\n{self.board[3]}  |  {self.board[4]}  |  {self.board[5]}\n{self.board[6]}  |  {self.board[7]}  |  {self.board[8]}"


    def move(self, player, user_move): # pass the player object in
        moves = {'top left'       :  0,
                 'top middle'     :  1,
                 'top right'      :  2,
                 'middle left'    :  3,
                 'middle'         :  4,
                 'middle right'   :  5,
                 'bottom left'    :  6,
                 'bottom middle'  :  7,
                 'bottom right'   :  8,
        }

        user_move = moves[user_move]
        if self.board[user_move] != ' ':
            return False
        else:
            self.board[user_move] = player.token # and use its token attribute here
            return True


    def calc_winner(self, token):
        return (self.board[0] == token and self.board[1] == token and self.board[2] == token or
                self.board[3] == token and self.board[4] == token and self.board[5] == token or
                self.board[6] == token and self.board[7] == token and self.board[8] == token or


                self.board[0] == token and self.board[3] == token and self.board[6] == token or
                self.board[1] == token and self.board[4] == token and self.board[7] == token or
                self.board[2] == token and self.board[5] == token and self.board[8] == token or


                self.board[0] == token and self.board[4] == token and self.board[8] == token or
                self.board[2] == token and self.board[4] == token and self.board[6] == token)



    def is_full(self):
        if " " not in self.board:
            print('Tied game.')
            return True


    def is_game_over(self, token):

        full_board = self.is_full()

        winner = self.calc_winner

        if winner(token) or winner(token):
            print('Game has a winner!')
            return True
        elif full_board == True:
            print('Tied game')
            return True


game_over = False




while True:
    player1_name = input("\nEnter player 1's name: ")

    player1_token = input("\nEnter player 1's token (X or O): ").upper()

    if player1_token != "X" and player1_token != "O":

        print("\nYou can only choose either X or O.")
    
    else:
        player2_name = input("\nEnter player 2's name: ")
    player2_token = ""


    if player1_token == "X":
        
        player2_token = "O"
        break

    if player1_token == "O":
        player2_token = "X"
        break



player_1 = Player(player1_name, player1_token)
player_2 = Player(player2_name, player2_token)


turn = 0
new_board = Game()

# make a list of players
players = [player_1, player_2]

possible_moves = ['top left', 'top middle','top right','middle left','middle','middle right','bottom left','bottom middle','bottom right']
while game_over == False:
    player = players[turn % 2] # alternate between players using this

    while True:
        user_move = input(f"{player.player}: choose an empty spot to place your token: ")
        if user_move not in possible_moves:
            print('Move not valid, try again.')              
        elif new_board.move(player, user_move) == True:
            break
        else:
            print('Move already played, try again.')

    turn += 1
    

    print(new_board)

    if new_board.is_game_over(player1_token) or new_board.is_game_over(player2_token):
        print('Game over')

        print('Thanks for losing.')

        break












