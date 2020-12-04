f = open('day-1-input')

bills = set(iter(f))
bill_list = []
for b in bills:
    bill_list.append(int(b.strip()))

slist = sorted(bill_list)
    
for first in slist:
    x = 2020 - first
    for second in slist:
        third = x - second
        if third in slist:
            sum = first + second + third
            product = first * second * third
            print(first, second, third, "sum:",sum, "product:", product)
            exit(1)
