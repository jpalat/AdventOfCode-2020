def parseData(strings):
    return list(map(lambda x: int(x), strings))


def find(input, window):
    data = parseData(input)
    start = window 
    for i in range(start, len(data)):
        addSlice = slice(i - window, i,1)
        # print(data[i], data[addSlice])
        if checkrange(data[i], data[addSlice]) == False:
            return data[i]
    return 0

'''
Check the target is sum of 2 addends.
'''
def checkrange(target, addends):
    result = False
    for i in addends:
        if target - i in addends:
            result = True
            return result
    return result


'''
Part 2.
'''
def findContiguous(input, target):
    data = parseData(input)
    for index, _ in enumerate(data):
        found = False
        start = index
        end = index+1
        while not found:
            subset = data[slice(start, end)]
            # print('start', start, 'end', end, 'sub:',subset)
            end +=1
            subsum = sum(subset)
            found = subsum == target
            if subsum == target:
                return subset
            if end > len(data) or subsum > target:
                break

if __name__ == "__main__":
    f = open('input.txt','r')
    data = list(f)
    weakness_p1 = find(data, 25)
    print('Weakness:', weakness_p1)
    newset = findContiguous(data, weakness_p1)
    print(newset)
    weakness = max(newset) + min(newset)
    print('Weakness: (pt2):', weakness)

    