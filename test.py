# N = input()
# R = int(input())

# digits = list(N)
# sum = 0
# for digit in digits:
#     sum +=int(digit)

# rTimes = R*sum

# digits = list(str(rTimes))
# sum = 0
# for digit in digits:
#     sum +=int(digit)

# print(sum)
# import math

# N = int(input())
# M = int(input())
# P = int(input())
# Q = int(input())

# result = math.factorial(N)/math.factorial(N-P)*math.factorial(P)*math.factorial(M)/math.factorial(M-Q)*math.factorial(Q)
# print(Q)

from collections import Counter

def StringChallenge(strParam):
    li = list(strParam)
    occ = dict(Counter(li))

    try:
        if occ['x']==occ['o']:
            return True
        else:
            return False
    except:
        return False

print(StringChallenge(input()))