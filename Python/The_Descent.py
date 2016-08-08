# The while loop represents the game.
# Each iteration represents a turn of the game
# where you are given inputs (the heights of the mountains)
# and where you have to print an output (the index of the moutain to fire on)
# The inputs you are given are automatically updated according to your last actions.


# game loop
while True:
    target_mountain = dict()
    for i in xrange(8):
        mountain_h = int(raw_input())  # represents the height of one mountain.
        if i == 0 or mountain_h > target_mountain['height']:
            target_mountain['id'] = i
            target_mountain['height'] = mountain_h

    # Write an action using print
    # To debug: print >> sys.stderr, "Debug messages..."

    # The index of the mountain to fire on.
    print(target_mountain['id'])
