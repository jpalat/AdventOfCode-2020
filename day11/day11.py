import copy

def model_seats(input):
    floor = list(input)
    floor_plan = []
    size = len(floor[0])-1
    for l in floor:
        line = list(l.strip())
        floor_plan.append(line)
    delta = 1
    while delta > 0:
        floor_plan, delta = mutate(floor_plan)
    return count_passengers(floor_plan)

def model_seats2(input):
    floor = list(input)
    floor_plan = []
    size = len(floor[0])-1
    for l in floor:
        line = list(l.strip())
        floor_plan.append(line)
    delta = 1
    # while delta > 0:
    #     floor_plan, delta = mutate2(floor_plan)
    # return count_passengers(floor_plan)
    for i in range(5):
        floor_plan, delta = mutate2(floor_plan)
        print('Run:', i)
        print_floor(floor_plan)

def print_floor(floor):
    for i in floor:
        for j in i:
            print(j, end =" ")
        print()

def count_passengers(floor):
    count = 0
    for row in floor:
        for seat in row:
            if seat == '#':
                count += 1
    return count

def mutate(new_thing):
    orig = copy.deepcopy(new_thing)
    floor_plan = new_thing
    delta = 0
    for row, c in enumerate(orig):
        for column, seat in enumerate(c):
            if seat == 'L' and count_neighbors(row, column, orig) < 1:
                floor_plan[row][column] = '#'
                delta += 1
            if seat == '#':
                if count_neighbors(row, column, orig) > 3:
                    floor_plan[row][column] = 'L'
                    delta += 1
    return floor_plan, delta

def mutate2(new_thing):
    orig = copy.deepcopy(new_thing)
    floor_plan = new_thing
    delta = 0
    for row, c in enumerate(orig):
        for column, seat in enumerate(c):
            if seat == 'L' and count_neighbors2(row, column, orig) < 1:
                floor_plan[row][column] = '#'
                delta += 1
            if seat == '#':
                if count_neighbors2(row, column, orig) > 4:
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
    if row == len(floor)-1 or col == 0: 
        return 0
    if floor[row + 1][col - 1] == '#':
        return 1
    return 0

def check_br(row, col, floor):
    if row == len(floor) -1 or col == len(floor[row]) -1: 
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
    # print(row, col, tl , up , tr , le , ri , bl , dn , br, sum)
    return sum

def count_neighbors2(row, col, floor):
    sum = 0
    bl = check_bl2(row, col, floor)
    br = check_br2(row, col, floor)
    dn = check_down2(row, col, floor)
    le = check_left2(row, col, floor)
    ri = check_right2(row, col, floor)
    tl = check_tl2(row, col, floor)
    tr = check_tr2(row, col, floor)
    up = check_up2(row, col, floor)
    sum = tl + up + tr + le + ri + bl + dn + br
    # print(row, col,'\n', tl , up , tr ,'\n', le , 'L', ri ,'\n', bl , dn , br, sum)
    return sum

def check_left2(row, col, floor):
    if col == 0:
        return 0
    for c in range(col -1, -1, -1):
        if floor[row][c] == '#':
            return 1
        if floor[row][c] == 'L':
            return 0
    return 0

def check_right2(row, col, floor):
    edge = len(floor[row])
    if col == edge:
        return 0
    for c in range(col+1, edge):
        if floor[row][c] == '#':
            return 1
        if floor[row][c] == 'L':
            return 0
    return 0

def check_up2(row, col, floor):
    # print('up2')
    if row < 0:
        return 0
    for r in range(row  , 0, -1):
        # print('--r,c,',r, col, floor[r][col])
        if floor[r][col] == '#':
            return 1
        if floor[r][col] == 'L' and r != row:
            return 0
    return 0

def check_down2(row, col, floor):
    edge = len(floor)
    if row == len(floor) -1:
        return 0
    for r in range(row+1, edge):
        if floor[r][col] == '#':
            return 1
        if floor[r][col] == 'L':
            return 0
    return 0

def check_tl2(row, col, floor):
    # print('tl2')
    if row == 0 or col == 0: 
        return 0
    steps = intersect(row, col, 0, 0)

    for s in range(1, steps):
        r = row - s
        c = col - s
        # print('steps, s, r,c',steps, s,r, c)
        if r < 0 or c < 0: 
            return 0
        # print('steps, s, r,c',steps, s,r, c)
        if floor[r][c] == '#':
            return 1
        if floor[r][c] == 'L':
            return 0
    return 0

def check_tr2(row, col, floor):
    right_edge = len(floor[row])
    if row == 0 or col == right_edge -1: 
        return 0
    steps = intersect(row, col, right_edge, 0) + 1
    for s in range(1, steps):
        r = row - s
        c = col + s
        if r < 0 or c > right_edge - 1 : 
            return 0
        if floor[r][c] == '#':
            return 1
        if floor[r][c] == 'L':
            return 0
    return 0

def check_bl2(row, col, floor):
    # print('bl2')
    bottom = len(floor)-1
    if row == bottom or col == 0: 
        return 0
    steps = intersect(row, col, bottom, 0) + 1
    for s in range(1, steps):
        r = row + s
        c = col - s
        
        if r > bottom or c < 0:
            return 0
        if floor[r][c] == '#':
            return 1
        if floor[r][c] == 'L':
            return 0
    return 0

def check_br2(row, col, floor):
    # print('br2')

    bottom = len(floor)
    right_edge = len(floor[row])
    if row == bottom -1 or row == right_edge -1: 
        return 0
    steps = intersect(row, col, right_edge, bottom) 
    for s in range(1, steps):
        r = row + s 
        c = col + s
        # print('steps, s, r,c',steps, s,r, c)
        if r == bottom  or c == right_edge:
            # print('found edge at', r,c)
            # print('bottom, right', bottom, right_edge)
            return 0
        if floor[r][c] == '#':
            return 1
        if floor[r][c] == 'L':
            return 0
    return 0

def intersect(origin_row, origin_col, dest_row, dest_col):
    row_distance = abs(origin_row - dest_row)
    col_distance = abs(origin_col - dest_col)
    # print('intersect', origin_row, origin_col, dest_row, dest_col, row_distance, col_distance)
    if row_distance < col_distance:
        return col_distance
    else:
        return row_distance

if __name__ == "__main__":
    f = open('input.txt','r')
    print('seats:', model_seats(f))