# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
ALPHA = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
         'W', 'X', 'Y', 'Z', 'QM']
chars = dict()
for letter in ALPHA:
    chars[letter] = list()

l = int(raw_input())
h = int(raw_input())
t = raw_input()
for i in xrange(h):
    row = raw_input()
    position = 0
    for letter in ALPHA:
        chars[letter].append(row[position:position + l])
        position += l

text = t.upper()
# Write an action using print
# To debug: print >> sys.stderr, "Debug messages..."
# for letter in text:
output = list()

for i in xrange(h):
    row = ""
    for char in text:
        if char in ALPHA:
            row += chars[char][i]
        else:
            row += chars['QM'][i]
    output.append(row)

for row in output:
    print(row)
