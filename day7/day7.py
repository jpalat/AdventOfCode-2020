def parseRule(rule):
    results = splitParser(rule)
    response = {}
    if len(results) == 0:
        return {}
    else:
        for r in results:
            qty, mod, bag = r
            display_name = mod + " " + bag
            response[display_name] = int(qty)

    return response

def tokenParser(rule):
    tokens = rule.split(' ')
    print(tokens)

def splitParser(rule):
    head, tail = rule.split(' contain ')
    container_list = tail.split(', ')
    results = []
    for c in container_list:
        tokens = c.split(' ')
        if len(tokens) > 3:
            qty, mod, bag, _ = tokens
            results.append((qty, mod, bag))
    return results

            
        
