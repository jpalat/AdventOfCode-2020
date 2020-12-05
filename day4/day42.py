def passportValidator(passport):
    required_keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    optional_keys = ['cid']
    valid = True
    for key in required_keys:
        if key in passport:
            pass
        else:
            return False
    return True

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
            

def fieldValidator(key, value):
    if key == 'byr':
        return yearValidator(value, 1920, 2002)
    if key == 'iyr':
        return yearValidator(value, 2010, 2020)
    if key == 'eyr':
        return yearValidator(value, 2020, 2030)
    if key == 'hgt':
        return hgtValidator(value)
    if key == 'ecl':
        return eclValidator(value)
    if key == 'pid':
        return pidValidator(value)


def yearValidator(year_str, lower, upper):
    year = int(year_str)
    return inRange(year, lower, upper)

def inRange(value, lower, upper):
    if (value > lower and value <= upper):
        return True
    else:
        return False

def hgtValidator(fieldValue):
    unit = fieldValue[-2:]
    measure = int(fieldValue[:-2])
    if unit == 'cm':
        return inRange(measure, 150, 193)
    if unit == 'in':
        return inRange(measure, 59,76)
    else:
        return False

def eclValidator(value):
    valid_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    if value in valid_colors:
        return True
    return False

def pidValidator(value):
    if len(value) < 9 or len(value) > 9:
        return False
    for i in list(value):
        if i not in ['0','1','2','3','4','5','6','7','8','9']:
            return False
    return True
    

if __name__ == "__main__":
    fileInput = open('input.txt','r')
    passports = batchparser(fileInput)
    count = 0
    for passport in passports:
        if passportValidator(passport):
            count += 1
    print("Valid Passports:", count)