f = open('sample.txt')

pos = 0
for line in f:
    line_array = list(line)
    line_array[pos] = 'X'
    print(line_array.join(''))
    pos = (pos + 3) % len(line)