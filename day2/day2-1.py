f = open('input.txt')



def validate(rule, target, password):
    lower_bound,upper_bound = rule.split('-')
    occurances = list(password)
    count = 0
    for o in occurances:
        if o == target:
            count+=1
    if count >= int(lower_bound) and count <= int(upper_bound):
        return True
    else:
        return False


valid_passwords = 0
for line in f:

   rule, password = line.split(':')
   freq, target = rule.split()
   if validate(freq, target, password):
       valid_passwords += 1

print("Valid Passwords: ", valid_passwords)

    
    