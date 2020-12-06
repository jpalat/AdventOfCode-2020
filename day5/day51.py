import struct
import math

def seatDecoder(passid):
    print('passid:', passid)
    instructions = list(passid)
    row_instructions = instructions[:7]
    col_instructions = instructions[-3:]
    row = parseRow(row_instructions)
    col = parseCol(col_instructions)
    seat = (row * 8) + col
    # print(row_instructions, seat_instructions)
    return (row, col, seat)

def parseRow(instructions):
    row = 0
    for index, r in enumerate(reversed(instructions)):
        if r == 'B':
            row = (2**index) + row
    return row

def parseCol(instructions):
    column = 0
    for index,c in enumerate(reversed(instructions)):
        if c == 'R':
            column = (2**index) + column
    return column
            

if __name__ == "__main__":
    f = open('input.txt')
    l = list(f)
    l.sort()
    bigseat = 0
    for index, seat in enumerate(l):
        row, col, seat = seatDecoder(seat.strip())
        print (index, ': ',row, col, seat, bigseat)
        if seat > bigseat:
            bigseat = seat
        
    print("Highest Seat ID:", bigseat)
        

