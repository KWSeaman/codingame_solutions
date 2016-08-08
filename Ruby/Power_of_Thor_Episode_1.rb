STDOUT.sync = true # DO NOT REMOVE
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# LX: the X position of the light of power
# LY: the Y position of the light of power
# TX: Thor's starting X position
# TY: Thor's starting Y position
$LX, $LY, $TX, $TY = gets.split(" ").collect {|x| x.to_i}
$CX=$TX
$CY=$TY
# game loop
loop do
    $E = gets.to_i # The level of Thor's remaining energy, representing the number of moves he can still make.

    $DeltaX = $CX-$LX
    $DeltaY = $CY-$LY

    if $DeltaX>0
        if $DeltaY>0
            puts "NW"
            $CX+=1
            $CY--1
        elsif $DeltaY<0
            puts "SW"
            $CX-=1
            $CY+=1
        else
            puts "W"
            $CX-=1
        end
    elsif $DeltaX<0
        if $DeltaY>0
          puts "NE"
          $CX+=1
          $CY-=1
        elsif $DeltaY<0
          puts "SE"
          $CX+=1
          $CY+=1
        else
            puts "E"
            $CX+=1
        end
    else
        if $DeltaY>0
          puts "N"
          $CY-=1
        elsif $DeltaY<0
          puts "S"
          $CY+=1
      end
    end

    # Write an action using puts
    # To debug: STDERR.puts "Debug messages..."

    #puts "SE" # A single line providing the move to be made: N NE E SE S SW W or NW
end