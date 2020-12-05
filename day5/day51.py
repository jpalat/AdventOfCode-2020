import struct
import math

def seatDecoder(passid):
    print('passid:', passid)
    instructions = list(passid)
    row_instructions = instructions[:7]
    seat_instructions = instructions[-3:]
    row = parseRow(row_instructions)
    col = parseSeat(seat_instructions)
    seat = (row * 8) + col
    print(row_instructions, seat_instructions)
    return (row, col, seat)

def parseRow(instructions):
    lb = 0
    ub = 127
    for f in list(instructions):
        border = math.floor((ub-lb)/2) + lb
        if f == 'F':
            ub = border
        else:
            lb = border + 1
        print(f, lb, ub, border)
    return border

def parseSeat(instructions):
    lb = 0
    ub = 7
    for f in list(instructions):
        border = math.floor((ub-lb)/2) + lb
        if f == 'L':
            ub = border
        else:
            lb = border + 1
        print(f, lb, ub, border)
    return lb

        

