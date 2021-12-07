'''
Tic Tac Toe mob
Authors: Dart, Travis, Auriel, Alnardo
Date:

'''




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
        return   f"{self.board[0]} + '|' + {self.board[1]} + '|' + {self.board[2]}\n{self.board[3]} + '|' + {self.board[4]} + '|' + {self.board[5]}\n{self.board[6]} + '|' + {self.board[7]} + '|' + {self.board[8]}"


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

        user_move = input(f"Choose an empty spot to place your token: ")
        user_move = moves[user_move]
        self.board[user_move] = token
        print(self.board[0] + '|' + self.board[1] + '|' + self.board[2])
        print(self.board[3] + '|' + self.board[4] + '|' + self.board[5])
        print(self.board[6] + '|' + self.board[7] + '|' + self.board[8])
        return self.board


    def calc_winner():
        ...


    def is_full():
        ...


    def is_game_over():
        ...



test = Game()
# print(test)


while True: # ask for player 1's name and preferred token
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

test.move(player1_name, player1_token)


# print(player_1)
# print(player_2)












