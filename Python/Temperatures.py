# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(raw_input())  # the number of temperatures to analyse
temps = raw_input()  # the n temperatures expressed as integers ranging from -273 to 5526

# Write an action using print
# To debug: print >> sys.stderr, "Debug messages..."

lowest_num = 99999
if n == 0:
    print("0")
else:
    temps = temps.split(' ')
    int_temps = [int(x) for x in temps]

    for num in int_temps:
        if abs(num) < abs(lowest_num):
            lowest_num = num
        elif abs(num) == abs(lowest_num):
            if num > 0:
                lowest_num = num

    print(lowest_num)
