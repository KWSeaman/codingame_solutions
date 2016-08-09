# built-in inputs
width = int(input())  # the number of cells on the X axis
height = int(input())  # the number of cells on the Y axis
lines = [None]*height
for i in range(height):
    lines[i] = input()  # width characters, each either 0 or .

# # mock inputs
# width = 2
# height = 2
# lines = ["00","0."]
#
# width = 1
# height = 4
# lines = ["0","0","0","0"]

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)
for i in range(height):
    for j in range(width):
        if lines[i][j] == '0':
            #look right
            rightx = -1
            righty = -1
            if lines[i][j+1:].count('0')>0:
                rightx = lines[i][j+1:].find('0')+j+1
                righty = i
            #look down
            leftx = -1
            lefty = -1
            for l in range(i+1,height):
                if lines[l][j] == '0':
                    leftx = j
                    lefty = l
                    break
            print(j,i,rightx,righty,leftx,lefty,' ')

# Three coordinates: a node, its right neighbor, its bottom neighbor
