import copy

def model_seats(input):
    floor = list(input)
    floor_plan = []
    size = len(floor[0])-1
    for l in floor:
        line = list(l.strip())
        floor_plan.append(line)
    print('Start')
    delta = 1
    while delta > 0:
        floor_plan, delta = mutate(floor_plan)
    return count_passengers(floor_plan)

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
        # print('ccc-> ', row ,c)
        for column, seat in enumerate(c):
            # print('row, column, seat:', row, column, seat)
            if seat == 'L' and count_neighbors(row, column, orig) < 1:
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
    print(row, col,'\n', tl , up , tr ,'\n', le , 'L', ri ,'\n', bl , dn , br, sum)
    return sum
def check_left2(row, col, floor):
    if col == 0:
        return 0
    for c in range(col -1, -1, -1):
        print('c',c, floor[row][c])
        if floor[row][c] == '#':
            return 1
        if floor[row][c] == 'L':
            return 0
    return 0
if __name__ == "__main__":
    f = open('input.txt','r')
    print('seats:', model_seats(f))