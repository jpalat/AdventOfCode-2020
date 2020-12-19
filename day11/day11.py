def model_seats(input):
    floor = list(input)
    floor_plan = []
    size = len(floor[0])-1
    for l in floor:
        line = list(l.strip())
        floor_plan.append(line)
    mutate(floor_plan)
    print('model')
    print_floor(floor_plan)
    return 0

def print_floor(floor):
    for i in floor:
        print(i)

def mutate(floor_plan):
    delta = 0
    for row, c in enumerate(floor_plan):
        for column, seat in enumerate(c):
            print('row, column, seat:', row, column, seat)
            if seat == 'L':
                print('bingo!')
                floor_plan[row][column] = '#'
                delta += 1
            
    print('mutate')
    print_floor(floor_plan)

def check_left(row, col, floor):
    return -1

def check_right(row, col, floor):
    return -1

def check_up(row, col, floor):
    return -1

def check_down(row, col, floor):
    return -1