class Board
    
    def initialize(player1, player2)
        @player1 = player1
        @player2 = player2
        @active_player = player1
        @board = [[nil, nil, nil],
                  [nil, nil, nil],
                  [nil, nil, nil]]
        @key = {"tl" => [0, 0],
                "t" => [0, 1],
                "tr" => [0, 2],
                "l" => [1, 0],
                "m" => [1, 1],
                "r" => [1, 2],
                "bl" => [2, 0],
                "b" => [2, 1],
                "br" => [2, 2],}
    end 

    def board
        @board.each do |i|
            p i 
            puts
        end
    end

    def play(player, position)
        marker = player.marker

end

class Player
    attr_reader :marker

    def initialize(marker)
        @marker = marker
    end
end

paul = Player.new("X")
zach = Player.new("O")
game = Board.new(paul, zach)
puts game.board