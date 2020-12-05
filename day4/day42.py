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
        year = int(value)
        if year >1919 and year < 2003:
            return True
        else:
            return False
    if key == 'iyr':
        year = int(value)
        if year > 2009 and year < 2021:
            return True
        else:
            return False



if __name__ == "__main__":
    fileInput = open('input.txt','r')
    passports = batchparser(fileInput)
    count = 0
    for passport in passports:
        if passportValidator(passport):
            count += 1
    print("Valid Passports:", count)