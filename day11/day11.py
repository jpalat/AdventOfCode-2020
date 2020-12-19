def model_seats(input):
    floor = list(input)
    floor_plan = []
    size = len(floor[0])-1
    for l in floor:
        line = list(l.strip())
        floor_plan.append(line)
    return 0