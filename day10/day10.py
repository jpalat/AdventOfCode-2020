def chain(adapters):
    adapter_list = sorted(list(map(lambda x: int(x), adapters)))
    plug = 0
    device = max(adapter_list) + 3
    adapter_list.append(device)
    last = 0
    joltage = {'1 jolt':0, '3 jolts':0}
    for i in adapter_list:
        if i - last == 1:
            joltage['1 jolt'] += 1
        if i - last == 3:
            joltage['3 jolts'] += 1
        last = i
    return joltage

def arrangements(data):
def build_matrix(adapter_list):
    adjmatrix = [[0 for x in range(len(adapter_list))] for y in range(len(adapter_list))]
        
    for index, value in enumerate(adapter_list):
        
        for row_index, current in enumerate(adapter_list[slice(index)]):
            diff = abs(current - value)
            print(diff)
            if diff < 4 and diff > 0:
                print("index", index, "value", value)
                print("r_index", row_index, "value", current)
                adjmatrix[index][row_index] = 1
    print("\n adj", adjmatrix)

    for r in adjmatrix:
        print("\n",r)
    return adjmatrix

def build_graph(data_list): 
    graph = {}
    for index, value in enumerate(data_list):
        children = []
        for subindex, subvalue in enumerate(data_list):
            
            diff =  subvalue - value
            # print('diff', value, subvalue, diff)
            if diff < 4 and diff >0:
                children.append(subvalue)
            else:
                pass
        graph[value] = children
    # print('graph', graph)
    return graph
if __name__ == "__main__":
    f = open('input.txt','r')
    result = chain(f)
    print('\n',result, result['1 jolt'] * result['3 jolts'])