f = open('sample.txt')

pos = 0
for line in f:
    line[pos] = 'X'
    print(line)