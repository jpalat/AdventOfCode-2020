def getGroups(f):
    batch = []
    batches = []
    for line in f:
        if line == '\n':
            batches.append(batch)
            batch = []
        else:
            batch.append(line.strip())
    batches.append(batch)
    return batches

"""
Check for the unique total of questions answerd
"""
def uniqueGroupAnswers(respondents):
    overall = set()
    for x in respondents:
        answers = list(x)
        resp = set(answers)
        overall = overall.union(resp)
    return overall
