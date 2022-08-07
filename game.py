from ast import While


class Game():
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.active_player = player1
        self.board = [[None, None, None],
                      [None, None, None],
                      [None, None, None]]
        self.key = {"tl": [0,0],
                    "t": [0,1],
                    "tr": [0,2],
                    "l": [1,0],
                    "m": [1,1],
                    "r": [1,2],
                    "bl": [2,0],
                    "b": [2,1],
                    "br": [2,2],}

    def print_board(self):
        for row in self.board:
            print(row)
            print()
        print("-" * 20)
        print()

    def play(self, position):
        marker = self.active_player.marker
        location = self.key[position]
 
        if self.board[location[0]][location[1]]== None:
            self.board[location[0]][location[1]] = marker
        else:
            print("That place is taken. Please try again.")
            return
        
        if self.is_winner():
            print(f"{self.active_player.name} won!\n")
            self.new_game()

        if self.is_full():
            print("No winner this time!\n")
            self.new_game()
        
        if self.active_player == self.player1:
            self.active_player = self.player2
        else:
            self.active_player = self.player1

        

    def is_winner(self):
        li = self.board

        #horizontal wins
        if li[0][0] == li[0][1] and li[0][1] == li[0][2] and li[0][0] != None:
            return True
        if li[1][0] == li[1][1] and li[1][1] == li[1][2] and li[1][0] != None:
            return True
        if li[2][0] == li[2][1] and li[2][1] == li[2][2] and li[2][0] != None:
            return True
        #vertical wins
        if li[0][0] == li[1][0] and li[1][0] == li[2][0] and li[0][0] != None:
            return True
        if li[0][1] == li[1][1] and li[1][1] == li[2][1] and li[0][1] != None:
            return True
        if li[0][2] == li[1][2] and li[1][2] == li[2][2] and li[0][2] != None:
            return True
        #diagonal wins
        if li[0][0] == li[1][1] and li[1][1] == li[2][2] and li[0][0] != None:
            return True
        if li[0][2] == li[1][1] and li[1][1] == li[2][0] and li[0][2] != None:
            return True
        
        return False

    def is_full(self):
        for row in self.board:
            for i in row:
                if i == None:
                    return False
        return True
        
    def new_game(self):
            self.active_player = self.player1
            self.board = [[None, None, None],
                          [None, None, None],
                          [None, None, None]]
            



class Player():
    def __init__(self, name, marker):
        self.name = name
        self.marker = marker
    
paul = Player("Paul", "X")
zach = Player("Zach", "O")
game = Game(paul, zach)
options = ["tl", "t", "tr", "l", "m", "r", "bl", "b", "br"]

while True:
    game.print_board()
    move = input(f"It's {game.active_player.name}'s turn.\n")
    if move == 'quit':
        break
    if move not in options:
        print("Not a valid move. Please try again.\n")
        
    game.play(move)




