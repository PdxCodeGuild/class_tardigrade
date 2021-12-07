'''
Tic Tac Toe mob
Authors: Dart, Travis, Auriel, Alnardo
Date:

'''




class Player:

    def __init__(self, player, token):
        
        self.player = player
        self.token = token
        


class Game:

    def __init__(self):

        self.board = board

        # self.board = { 1: “ “, “2”: “ “, “3”: “ “,
        #               “4”: “ “, “5”: “ “, “6”: “ “,
        #               “7”: “ “, “8”: “ “, “9”: “ “}
        ...        


    def __str__(self, board):

        board = [
                ['', '|', '', '|', ''],
                ['', '|', '', '|', ''],
                ['', '|', '', '|', '']
                ]
    

    def move(x, y, player):
        ...


    def calc_winner():
        ...


    def is_full():
        ...


    def is_game_over():
        ...







#player_o = Player("O", "o")



while True: # ask for player 1's name and preferred token
    player1_name = input("\nEnter player 1's name: ")

    player1_token = input("\nEnter player 1's token (X or O): ").upper()

    if player1_token != "X" and player1_token != "O":

        print("\nYou can only choose either X or O.")
    
    player2_name = input("\nEnter player 2's name: ")
    player2_token = ""


    if player1_token == "X":
        
        #player_x = Player("X", "x")

        player2_token = "O"

        print("You  ")

        break
        













