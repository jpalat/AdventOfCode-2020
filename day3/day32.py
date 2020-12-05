import unittest



def navigator(file_handle, rise, run):
    pos = 0
    count = 0
    print("rise, run", rise, run)
    for index, line in enumerate(file_handle):
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
            pos = (pos + run) % (len(line) -1)
    print("Count", count)
    return count

