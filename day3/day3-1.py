f = open('sample.txt')

pos = 0
for line in f:
    line_array = list(line)
    line_array[pos] = 'X'
    print(''.join(line_array))
    pos = (pos + 3) % len(line)