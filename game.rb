class Board
    
    def initialize(player1, player2)
        @player1 = player1
        @player2 = player2
        @active_player = player1
        @board = [[nil, nil, nil],
                  [nil, nil, nil],
                  [nil, nil, nil]]
    end 

    def board
        @board.each do |i|
            p i 
            puts
        end
    end
end

class Player
    def initialize(marker)
        @marker = marker
    end
end

paul = Player.new("X")
zach = Player.new("O")
game = Board.new(paul, zach)
puts game.board