def primFactors(n):
    li = []
    i=2
    while i<n/2:
        if n%i==0:
            count = 0
            j=2
            while j!=i:
                if i%j == 0:
                    count+=1
                j+=1
            if count==0:
                li.append(i)
        i+=1

    return li

def primNumbers(n):
    i = 2
    li = []
    while i!=n:
        count = 0
        j=2
        while j!=i:
            if i%j == 0:
                count+=1
            j+=1
        if count==0:
            li.append(i)
        i+=1
    
    return li

def checkArmstrongNo(n): 
    #also called Narcissistic number
    sum = 0
    st = f'{n}'

    for char in st:
        sum += int(char)**len(st)

    if n==sum:
        return True

    return False

def checkStrongNo(n):
    sum =0
    st = f'{n}'

    for char in st:
        pro = 1
        j = 2
        while j != int(char) + 1:
            pro *= j
            j += 1
        sum += pro
    if n==sum:
        return True

    return False

def decimalToBinary(n):
    return bin(n).replace("0b","")
 
def binaryToDecimal(n):
    return int(n, 2)

def desimalToHex(n):
    return hex(n)

def hexToDecimal(n):
    return int(n, 6)

def decimalToOct(n):
    return oct(n)

def octToDecimal(n):
    return int(n, 8)

def fabonacci(n):
    li = [0,1,]
    if n>2:
        for i in range(2, n):
            li.append(li[i-2]+li[i-1])
    return li

if __name__=="__main__":
    n = 10
    print(fabonacci(n))
    # print(checkStrongNo(n))
    # print(primFactors(n))