import copy

def model_seats(input):
    floor = list(input)
    floor_plan = []
    size = len(floor[0])-1
    for l in floor:
        line = list(l.strip())
        floor_plan.append(line)
    print('Start')
    print('mutate1')
    floor_plan, delta = mutate(floor_plan)
    print('mutate2')
    floor_plan, delta = mutate(floor_plan)
    return 0

def print_floor(floor):
    for i in floor:
        print(i)

def mutate(new_thing):
    orig = copy.deepcopy(new_thing)
    floor_plan = new_thing
    delta = 0
    for row, c in enumerate(orig):
        # print('ccc-> ', row ,c)
        for column, seat in enumerate(c):
            # print('row, column, seat:', row, column, seat)
            if seat == 'L':
                floor_plan[row][column] = '#'
                delta += 1
            if seat == '#':
                if count_neighbors(row, column, orig) > 3:
                    floor_plan[row][column] = 'L'
                    delta += 1
    return floor_plan, delta

def check_left(row, col, floor):
    if col == 0:
        return 0
    if floor[row][col - 1] == '#':
        return 1
    return 0

def check_right(row, col, floor):
    if col == len(floor[row])-1:
        return 0
    if floor[row][col + 1] == '#':
        return 1
    return 0

def check_up(row, col, floor):
    if row == 0:
        return 0
    if floor[row -1][col] == '#':
        return 1
    return 0

def check_down(row, col, floor):
    if row == len(floor) -1:
        return 0
    if floor[row + 1][col] == '#':
        return 1
    return 0

def check_tl(row, col, floor):
    if row == 0 or col == 0: 
        return 0
    if floor[row -1][col - 1] == '#':
        return 1
    return 0

def check_tr(row, col, floor):
    if row == 0 or col == len(floor[row]) -1: 
        return 0
    if floor[row -1][col + 1] == '#':
        return 1
    return 0

def check_bl(row, col, floor):
    if row == len(floor[row])-1 or col == 0: 
        return 0
    if floor[row + 1][col - 1] == '#':
        return 1
    return 0

def check_br(row, col, floor):
    if row == len(floor[row])-1 or col == len(floor[row]) -1: 
        return 0
    if floor[row + 1][col + 1] == '#':
        return 1
    return 0

def count_neighbors(row, col, floor):
    sum = 0
    bl = check_bl(row, col, floor)
    br = check_br(row, col, floor)
    dn = check_down(row, col, floor)
    le = check_left(row, col, floor)
    ri = check_right(row, col, floor)
    tl = check_tl(row, col, floor)
    tr = check_tr(row, col, floor)
    up = check_up(row, col, floor)
    sum = tl + up + tr + le + ri + bl + dn + br
    print(row, col, tl , up , tr , le , ri , bl , dn , br, sum)
    return sum