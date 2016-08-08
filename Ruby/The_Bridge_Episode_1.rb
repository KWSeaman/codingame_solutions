STDOUT.sync = true # DO NOT REMOVE
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

$R = gets.to_i # the length of the road before the gap.
$G = gets.to_i # the length of the gap.
$L = gets.to_i # the length of the landing platform.

# game loop
loop do
    $S = gets.to_i # the motorbike's speed.
    $X = gets.to_i # the position on the road of the motorbike.
    $Dist2Gap = $R-$X
    if $Dist2Gap<0
        puts 'SLOW'
    elsif $Dist2Gap <$S
        puts "JUMP"
    elsif $S < $G+1
        puts "SPEED"
    elsif $S > $G+1
        puts "SLOW"
    else
        puts "WAIT"
    end
    # Write an action using puts
    # To debug: STDERR.puts "Debug messages..."

    #puts "SPEED" # A single line containing one of 4 keywords: SPEED, SLOW, JUMP, WAIT.
end