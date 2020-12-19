def model_seats(input):
    floor = list(input)
    floor_plan = []
    size = len(floor[0])-1
    for l in floor:
        line = list(l.strip())
        floor_plan.append(line)
    print('model')
    print_floor(floor_plan)
    return 0

def print_floor(floor):
    for i in floor:
        print(i)
