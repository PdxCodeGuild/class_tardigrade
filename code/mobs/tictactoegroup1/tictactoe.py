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


    def move(self, player, token, user_move):
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
            self.board[user_move] = token
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

        full_board = self.is_full

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

while game_over == False:

    if turn % 2 == 0:
        while True:
            user_move = input(f"{player1_name}: choose an empty spot to place your token: ")
            if new_board.move(player1_name, player1_token, user_move) == True:
                break
            else:
                print('Move already played, try again.')
   
        turn += 1
    
    elif turn % 2 == 1:
        
        while True:
            user_move = input(f"{player2_name}: choose an empty spot to place your token: ")
            if new_board.move(player2_name, player2_token, user_move) == True:
                break
            else:
                print('Move already played, try again.')
   
        turn += 1

    print(new_board)

    if new_board.is_game_over(player1_token) or new_board.is_game_over(player2_token):
        print('Game over')

        print('Thanks for losing.')

        break
    # if new_board.calc_winner(player1_token) or new_board.calc_winner(player2_token):
    #     print('You did it')
    #     game_over == True
    #     break
    if new_board.is_full() == True:
        print('Tiiiiiiiiiiiiied game')
        break
        












