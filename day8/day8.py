class BootLoader:

    def __init__(self, filepath):
        self.accumulator = 0
        f = open(filepath,'r')
        self.program = list(f)
        f.close()

    def parseRule(self, index):
        operator, operand_raw  = self.program[index].strip().split(" ")
        operand = int(operand_raw)
        return (operator, operand)

