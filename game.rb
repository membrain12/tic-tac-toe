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

    def play(position)
        marker = @active_player.marker
        location = @key[position]
        if @board[location[0]][location[1]] == nil
            @board[location[0]][location[1]] = marker
        else 
            console.log("Sorry you can't go there. Try again")
        end
        if winner?
            new_game()
            return
        end
        
        
    end

    def winner?()
        li = @board
        #horizontal wins
        return true if li[0][0] == li[0][1] && li[0][1] == li[0][2]
        return true if li[1][0] == li[1][1] && li[1][1] == li[1][2]
        return true if li[2][0] == li[2][1] && li[2][1] == li[2][2]
        #vertical wins
        return true if li[0][0] == li[1][0] && li[1][0] == li[2][0]
        return true if li[0][1] == li[1][1] && li[1][1] == li[2][1]
        return true if li[0][2] == li[1][2] && li[1][2] == li[2][2]
        #diagonal wins
        return true if li[0][0] == li[1][1] && li[1][1] == li[2][2]
        return true if li[0][2] == li[1][1] && li[1][1] == li[2][0]

        return false
    end

    def board_full()
        g
    
    def new_game()
        @board = [[nil, nil, nil],
                  [nil, nil, nil],
                  [nil, nil, nil]]
    end
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
game.board



