f = open('sample.txt')

def tree_test(rise, run):
    pos = 0
    count = 0
    for index, line in enumerate(f):
        if index % rise != 0:
            # print(index, rise, index % rise)
            print(line.strip())
        else: 
            line_array = list(line.strip())
            if line_array[pos] == '.':
                line_array[pos] = 'O'
            else:
                line_array[pos] = 'X'
                count += 1

            print(''.join(line_array))
            pos = (pos + 3) % (len(line) -1)
    return count

print("Trees Encountered", tree_test(2,3))

