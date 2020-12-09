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
    for index, value in enumerate(data):
        sum = value
        start = index
        pointer = start
        res = []
        while sum < target:
            sum += data[pointer]
            pointer += 1
            res.append(data[pointer])
            print(index, value, sum, res)
        if sum == target:
            return res
    return []



if __name__ == "__main__":
    f = open('input.txt','r')
    data = list(f)
    print('Weakness:', find(data, 25))