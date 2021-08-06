from collections import Counter
s = "aaabbbbccddeee"
c = dict(Counter(list(s)))
case = ''
for key, value in c.items():
    case+= f'{key}{value}'
print(case)    
