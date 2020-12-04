f = open('day-1-input')

bills = set(iter(f))
bill_list = []
for b in bills:
    bill_list.append(int(b.strip()))

slist = sorted(bill_list)
    
for s in range(len(slist)):
    x = 2020 - slist[s]
    # print(x)
    if x in slist:
        print(slist[s], x, slist[s]* x)
        break;
