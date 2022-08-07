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
        
        if self.active_player == self.player1:
            self.active_player = self.player2
        else:
            self.active_player = self.player1
        


class Player():
    def __init__(self, name, marker):
        self.name = name
        self.marker = marker
    
paul = Player("Paul", "X")
zach = Player("Zach", "O")
game = Game(paul, zach)



game.print_board()
game.play("tl")
game.print_board()


