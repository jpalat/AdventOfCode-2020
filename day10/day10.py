def chain(adapters):
    adapter_list = sorted(list(map(lambda x: int(x), adapters)))
    plug = 0
    device = max(adapter_list) + 3
    print(plug, adapter_list, device)
    adapter_list.append(device)
    last = 0
    joltage = {'1 jolt':0, '3 jolts':0}
    for i in adapter_list:
        if i - last == 1:
            joltage['1 jolt'] += 1
        if i - last == 3:
            joltage['3 jolts'] += 1
        last = i
    print (adapter_list)
    return joltage