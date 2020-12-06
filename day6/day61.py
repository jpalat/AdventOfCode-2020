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

if __name__ == "__main__":
    f = open('input.txt','r')
    groups = getGroups(f)
    response_sum = 0
    for g in groups:
        response_sum = len(uniqueGroupAnswers(g)) + response_sum
    print("Total: ", response_sum)