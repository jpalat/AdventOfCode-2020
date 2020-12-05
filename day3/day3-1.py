f = open('sample.txt')

pos = 0
count = 0
for line in f:
    line_array = list(line.strip())
    if line_array[pos] == '.':
        line_array[pos] = 'O'
    else:
        line_array[pos] = 'X'
        count += 1

    print(''.join(line_array))
    pos = (pos + 3) % (len(line) -1)

print("Trees Encountered", count)