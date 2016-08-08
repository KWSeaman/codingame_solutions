# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

road = int(input())  # the length of the road before the gap.
gap = int(input())  # the length of the gap.
platform = int(input())  # the length of the landing platform.

# game loop
while True:

    speed = int(input())  # the motorbike's speed.
    coord_x = int(input())  # the position on the road of the motorbike.

    dist_to_gap = road-coord_x
    action = None

    if dist_to_gap<0 or speed > gap+1:
        action = "SLOW"
    elif dist_to_gap < speed:
        action = "JUMP"
    elif speed < gap+1:
        action = "SPEED"
    else:
        action = "WAIT"

        # Write an action using print
        # To debug: print("Debug messages...", file=sys.stderr)

    print(action)
        # A single line containing one of 4 keywords: SPEED, SLOW, JUMP, WAIT.