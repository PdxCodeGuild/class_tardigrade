class Player:
    def __init__(self, name='', token=''):
        self.name=name
        self.token=token
    def __repr__(self):
        return f'Player("{self.name}","{self.token}")'

class Game:
    def __init__(self, turn=0):
        
        self.turn = turn
        self.board = {1: " ",
                2: " ",
                3: " ",
                4: " ",
                5: " ",
                6: " ",
                7: " ",
                8: " ",
                 9: " "}

    def __str__(self):
        '''Returns a pretty string representation of the game board'''
       
        b = self.board
        line1 = b[1] + '|' + b[2] + '|' + b[3]
        line2 = '-+-+-'
        line3 = b[4] + '|' + b[5] + '|' + b[6]
        line4 = '-+-+-'
        line5 = b[7] + '|' + b[8] + '|' + b[9]
        return line1 + '\n' + line2 + '\n' + line3 + '\n' + line4 + '\n' + line5
    def move(self,command, player):
        b = self.board
        b[command] = player.token
        return command

        '''Moves a token through the x an y axes'''
    
        self.turn += 1
        if self.turn >= 9:
            self.is_full()

    def calc_winner(self):
        '''Determines which player has won the game'''
        b = self.board
      
        
        wins = [[1,2,3],[4,5,6], [7,8,9], [1,4,7], [2,5,8], [3,6,9], [1,5,9], [7,5,3]]
        for win in wins:
            wincount1 = 0
            wincount2 = 0
            for num in win:
                if b[num] == "X":
                    wincount1 += 1
                elif [b] == "O":
                    wincount2 += 1
        if wincount1 == 3:
            return "X"
        elif wincount2 == 3:
            return "O"
        else:
            return "no winner"
        
                
                     
                

    def is_full(self):
        if self.turn == 9 and self.calc_winner == "no winner":
            
            return True

        '''Determines if the board is full with no winner'''
       
    def is_game_over(self):
        finewinner = self.calc_winner()
        ful = self.is_full()
        if finewinner != "no winner":
            return True
        else:
            return False
        '''Returns true if the board is full or a player has won'''


    # def printBoard(board):

game = Game()
def main():
    print("Welcome to tic-tac-toe!")
    players = []
    player1=Player(input("X what is your name? "), "X")
    player2=Player(input("O What is your name? "), "O")
    players.append(player1)
    players.append(player2)
    active_player = players[game.turn %2]


    print(game)
    # while not game.is_game_over() == True:
    #     print(game)
    #     command= input("What is your move? ")
    command = int(input(f'{active_player.name} enter a number position (1-9) to place your token: '))
    print(game.move(command, player1))
    print(game.calc_winner())
    print(game)
main()

