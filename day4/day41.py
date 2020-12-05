def passportValidator():
    print('Hello')

def batchparser(input):
    source = list(input)
    passports = []
    passport = {}
    for index, line in enumerate(source):
        if line == '\n':
            print("reset")
            if passport != {}:
                passports.append(passport)
                passport = {}
        else:
            field_array = line.strip().split(' ')
            for f in field_array:
                key, value = f.split(':')
                passport[key] = value
    passports.append(passport)
    print(passports)
    return passports
            




if __name__ == "__main__":
    fileInput = open('input.txt','r')
