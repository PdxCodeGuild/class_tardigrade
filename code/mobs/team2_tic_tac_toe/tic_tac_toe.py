class Player:
    def __init__(self, name='', token=''):
        self.name=name
        self.token=token

class Game:
    def __init__(self, board=[], moves=0):
        self.board = board
        self.moves = moves

    def __str__(self):
        '''Returns a pretty string representation of the game board'''
        top = {1: " ",
                2: " ",
                3: " "}
        middle = {4: " ",
                  5: " ",
                  6: " "}
        bottom = {7: " ",
                    8: " ",
                    9: " "}
        self.board.append(top)
        self.board.append(middle)
        self.board.append(bottom)
        print(top[1] + '|' + top[2] + '|' + top[3])
        print('-+-+-')
        print(middle[4] + '|' + middle[5] + '|' + middle[6])
        print('-+-+-')
        print(bottom[7] + '|' + bottom[8] + '|' + bottom[9])

    def move(self,x, y, player):
        '''Moves a token through the x an y axes'''
    
        self.moves += 1
        if self.moves >= 9:
            self.is_full()

    def calc_winner():
        '''Determines which player has won the game'''

    def is_full():
        '''Determines if the board is full with no winner'''
       
    def is_game_over():
        '''Returns true if the board is full or a player has won'''


    # def printBoard(board):

game = Game()
def main():
    while True:
        print("Welcome to tic-tac-toe!")
        player1=Player(input("X what is your name? "), "X")
        player2=Player(input("O What is your name? "), "O")
        command= input("What is your move? ")

print(game)
