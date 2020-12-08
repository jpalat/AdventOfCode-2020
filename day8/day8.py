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
        
            if index in self.visited:
                Halt = True
                print('exiting')
                return self.accumulator

            
            
