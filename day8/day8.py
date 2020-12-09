class BootLoader:

    def __init__(self, filepath):
        self.accumulator = 0
        f = open(filepath,'r')
        self.program = list(f)
        f.close()
        self.visited = []

    def parseRule(self, index):
        operator, operand_raw  = self.program[index].strip().split(" ")
        operand = int(operand_raw)
        return (operator, operand)

    def execute(self):
        index = 0
        halt = False
        while(halt == False):
            operator, operand = self.parseRule(index)
            self.visited.append(index)
            if operator == 'nop':
                index = index + 1
            else:
                if operator == 'acc':
                    self.accumulator += operand
                    index = index + 1
                else:
                    if operator == 'jmp':
                        index = index + operand
                    else:
                        print("Unknown opp -")
                        print(operator)
                        exit(0)
            if index == len(self.program):
                print('End of Program')
                return "True"        
            if index in self.visited:
                Halt = True
                print('exiting')
                return self.accumulator


    def setRule(self, index, operator, operand):
        newRule = operator + ' ' + str(operand) + "\n"
        self.program[index] = newRule

    def mutate(self):
        index = 0
        halt = False
        program = self.program
        for index, rule in enumerate(program):
            self.visited = []
            self.accumulator = 0
            operator, operand = self.parseRule(index)
            if operator == 'nop':
                self.setRule(index,'jmp', operand)
                res = self.execute()
                if isinstance(res, str):
                    return self.accumulator
                else:
                    self.setRule(index, operator, operand)
            if operator == 'jmp':
                self.setRule(index,'nop', operand)
                res = self.execute()
                if isinstance(res, str):
                    return self.accumulator
                else:
                    self.setRule(index, operator, operand)              





        
            
if __name__ == "__main__":
    b = BootLoader('input.txt')
    print('accumulator :', b.execute())

