"""
Connect 4 optional lab
Author: Travis Jackson
Date: Dec 10 21

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
        self.column_header = ['1', '2', '3', '4', '5', '6', '7']



    def __repr__(self):


        column_header_print = f"""{29 * '_'}\n| {self.column_header[0]} | {self.column_header[1]} | {self.column_header[2]} | {self.column_header[3]} | {self.column_header[4]} | {self.column_header[5]} | {self.column_header[6]} | \n{29 * '_'} \n"""


        board_print = f"""{29 * '-'}\n| {self.board_layout[0]} | {self.board_layout[1]} | {self.board_layout[2]} | {self.board_layout[3]} | {self.board_layout[4]} | {self.board_layout[5]} | {self.board_layout[6]} | \n{29 * '-'}\n| {self.board_layout[7]} | {self.board_layout[8]} | {self.board_layout[9]} | {self.board_layout[10]} | {self.board_layout[11]} | {self.board_layout[12]} | {self.board_layout[13]} | \n{29 * '-'}\n| {self.board_layout[14]} | {self.board_layout[15]} | {self.board_layout[16]} | {self.board_layout[17]} | {self.board_layout[18]} | {self.board_layout[19]} | {self.board_layout[20]} | \n{29 * '-'}\n| {self.board_layout[21]} | {self.board_layout[22]} | {self.board_layout[23]} | {self.board_layout[24]} | {self.board_layout[25]} | {self.board_layout[26]} | {self.board_layout[27]} | \n{29 * '-'}\n| {self.board_layout[28]} | {self.board_layout[29]} | {self.board_layout[30]} | {self.board_layout[31]} | {self.board_layout[32]} | {self.board_layout[33]} | {self.board_layout[34]} | \n{29 * '-'}\n| {self.board_layout[35]} | {self.board_layout[36]} | {self.board_layout[37]} | {self.board_layout[38]} | {self.board_layout[39]} | {self.board_layout[40]} | {self.board_layout[41]} | \n{29 * '-'}  """

        return column_header_print + board_print

        


    def move(self, move_pick, player_token):

        if self.board_layout[move_pick - 1] != " ":
            return False


        every_seven = move_pick - 1
        while True:

                if self.board_layout[every_seven] == " " and every_seven < ((move_pick - 1) + (7 * 5)):


                    if len(self.board_layout) > (every_seven + 7):

                        if self.board_layout[every_seven + 7] != " ":

                            self.board_layout[every_seven] = player_token
                            break

                        else:

                            every_seven += 7 

                    else:
                        
                        every_seven += 7

                else:

                    self.board_layout[every_seven] = player_token

                    break
     



#column 1 = 1 8 15 22 29 36
#column 2 = 2 9 16 23 30  37
#column 3 = 3 10 17 24 31 38
#column 4 = 4 11 18 25 32 39
#column 5 = 5 12 19 26 33 40
#column 6 = 6 13 20 27 34 41
#column 7 = 1 17 21 26 35 42


    def is_game_over(self):
        ...

    

    def calc_winner(self):
        ...



    def is_full(self):
        ...

    

piece_color1 = ""
piece_color2 = ""
player1_name = ""
player2_name = ""

player1 = GamePlayer(player1_name, piece_color1)
player2 = GamePlayer(player2_name, piece_color2)

players_picked = False

new_board = Board()

print("Welcome to Connect Four")

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



    player1 = GamePlayer(player1_name, piece_color1)
    player2 = GamePlayer(player2_name, piece_color2)

    print(player1)
    print(player2)

    players_picked = True


game_over = False
count = 0

#game repl
player1 = GamePlayer(player1_name, piece_color1)
player2 = GamePlayer(player2_name, piece_color2)
piece_color1 = "B"
piece_color2 = "R"


while game_over == False:
    ...
        
    if count % 2 == 0:

        move_pick = int(input(f"{player1_name} What column would you like to place your piece? ")) 


        if new_board.board_layout[move_pick - 1] != " ":

            print("column full")
            
        else:    
            new_board.move(move_pick, piece_color1)
            print(new_board)

        count += 1
        
    elif count % 2 != 0:

        move_pick = int(input(f"{player2_name} What column would you like to place your piece? ")) 

        if new_board.board_layout[move_pick - 1] != " ":

            print("column full")
            
        else:    
            new_board.move(move_pick, piece_color1)
            print(new_board)

        count += 1

        

