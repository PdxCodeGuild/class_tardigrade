"""
Connect 4 optional lab
Author: Travis Jackson
Date: Dec 8 21

"""


class GamePlayer:

    def __init__(self, player, player_color):

        self.player = player
        self.player_color = player_color


    def __repr__(self):

        rep = self.player + ' is ' + self.player_color

        return rep



class Board:

    def __init__(self):  

        self.board_layout = [' ', ' ', ' ', ' ', ' ', ' ', ' ',
                        ' ', ' ', ' ', ' ', ' ', ' ', ' ',
                        ' ', ' ', ' ', ' ', ' ', ' ', ' ',
                        ' ', ' ', ' ', ' ', ' ', ' ', ' ',
                        ' ', ' ', ' ', ' ', ' ', ' ', ' ',
                        ' ', ' ', ' ', ' ', ' ', ' ', ' '  
                        ]
        test = 0
        for i, coord in enumerate(self.board_layout):

            test += 1

            self.board_layout[i] = str(test)



    def __repr__(self):

        board_print = f"""{36 * '-'}\n|  {self.board_layout[0]} |  {self.board_layout[1]} |  {self.board_layout[2]} |  {self.board_layout[3]} |  {self.board_layout[4]} |  {self.board_layout[5]} |  {self.board_layout[6]} | \n{36 * '-'}\n|  {self.board_layout[7]} |  {self.board_layout[8]} | {self.board_layout[9]} | {self.board_layout[10]} | {self.board_layout[11]}| {self.board_layout[12]} |  {self.board_layout[13]} | \n{36 * '-'}\n| {self.board_layout[14]} | {self.board_layout[15]} | {self.board_layout[16]} | {self.board_layout[17]} | {self.board_layout[18]} | {self.board_layout[19]} | {self.board_layout[20]} | \n{36 * '-'}\n| {self.board_layout[21]} | {self.board_layout[22]} | {self.board_layout[23]} | {self.board_layout[24]} | {self.board_layout[25]} | {self.board_layout[26]} | {self.board_layout[27]} | \n{36 * '-'}\n| {self.board_layout[28]} | {self.board_layout[29]} | {self.board_layout[30]} | {self.board_layout[31]} | {self.board_layout[32]} | {self.board_layout[33]} | {self.board_layout[34]} | \n{36 * '-'}\n| {self.board_layout[35]} | {self.board_layout[36]} | {self.board_layout[37]} | {self.board_layout[38]} | {self.board_layout[39]} | {self.board_layout[40]} | {self.board_layout[41]} | \n{36 * '-'}  """

        return board_print

        ...





    def move(self, move_pick, player_token):
        self.board_layout[move_pick - 1] = player_token
        




    def game_over(self):
        ...

    

    def game_won(self):
        ...



    def game_tie(self):
        ...

    

piece_color1 = ""
piece_color2 = ""
# player1_name = ""
# player2_name = ""

# player1 = GamePlayer(player1_name, piece_color1)
# player2 = GamePlayer(player2_name, piece_color2)

players_picked = False

new_board = Board()

print(new_board)

#repl to pick player

while players_picked == False:

    player1_name = input("Enter the first player's name: ")


    piece_color1 = input("What color does player 1 want (red/black)? ")



    if piece_color1 == 'red' or piece_color1 == 'black':

        pass

    else:

        print("Enter a vaild color. (red/black)")
        continue


    player2_name = input("Enter the second player's name: ")

    if piece_color1 == "red":

        piece_color1 = "R"
        piece_color2 = "B"

    else:
        piece_color1 = "B"
        piece_color2 = "R"

  #  player1.player_color = piece_color1
  #  player2.player_color = piece_color2

    player1 = GamePlayer(player1_name, piece_color1)
    player2 = GamePlayer(player2_name, piece_color2)

    print(player1)
    print(player2)

    players_picked = True


game_over = False
count = 0
#game repl
while game_over == False:
    ...
        
    if count % 2 == 0:

        print(new_board)

        move_pick = int(input("What location would you like to place your piece? "))

        new_board.move(move_pick, piece_color1)

        print(new_board)


        ...






















