# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
horses = [None] * n
for i in range(n):
    horses[i] = int(input())
horses.sort()
min_value = horses[1]-horses[0]
for i in range(n):
    if i>0:
        diff = horses[i]-horses[i-1]
        if diff < min_value:
            min_value = diff
# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

print(min_value)