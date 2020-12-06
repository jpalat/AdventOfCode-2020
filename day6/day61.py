def getGroups(f):
    batch = []
    batches = []
    for line in f:
        if line == '\n':
            batches.append(batch)
        else:
            batch.append(line.strip())
    batches.append(batch)
    return batches

