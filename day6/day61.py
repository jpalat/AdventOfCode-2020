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

def getCommonAnswers(respondents):
    overall = []
    for x in respondents:
        answers = list(x)
        overall.append(set(answers))
    if len(overall) > 1:
        common = set.intersection(*overall)
    else:
        common = overall[0]

    return common


if __name__ == "__main__":
    f = open('input.txt','r')
    groups = getGroups(f)
    response_sum = 0
    intersection_sum = 0
    for g in groups:
        response_sum = len(uniqueGroupAnswers(g)) + response_sum
        intersection_sum = len(getCommonAnswers(g)) + intersection_sum
    
    print("Total Unique: ", response_sum)
    print("Total Common: ", intersection_sum)
