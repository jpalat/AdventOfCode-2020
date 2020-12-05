f = open('input.txt')



def validate(rule, target, password):
    fp,sp = rule.split('-')
    first = int(fp)
    second = int(sp) 
    occurances = list(password)
    fo = occurances[first] == target
    so = occurances[second] == target

    return fo != so


valid_passwords = 0
for line in f:
   rule, password = line.split(':')
   freq, target = rule.split()
   if validate(freq, target, password):
       valid_passwords += 1
       

print("Valid Passwords: ", valid_passwords)

    
    