def parseRule(rule):
    head, tail = splitParser(rule)
    display_head = head[0] + ' ' + head[1]
    response = {}
    if len(tail) == 0:
        return {display_head:{}}
    else:
        for r in tail:
            qty, mod, bag = r
            display_name = mod + " " + bag
            response[display_name] = int(qty)

    return {display_head: response}

def tokenParser(rule):
    tokens = rule.split(' ')
    print(tokens)

def splitParser(rule):
    head, tail = rule.split(' contain ')
    tail_result = tailParser(tail)
    head_result = headParser(head)
    return (head_result, tail_result)


def headParser(head):
    tokens = head.split(' ')
    mod, bag, _ = tokens
    return (mod, bag)



def tailParser(tail):
    container_list = tail.split(', ')
    results = []
    for c in container_list:
        tokens = c.split(' ')
        if len(tokens) > 3:
            qty, mod, bag, _ = tokens
            results.append((qty, mod, bag))
    return results
