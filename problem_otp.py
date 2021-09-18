def primeNumber(n):
    
    if n>0:
        count = 0
        j=2
        while j<=n:
            if n%j == 0:
                count+=1
            j+=1
        if count==1:
            return True
    elif n<0:
        count = 0
        j=-2
        while j>=n:
            if n%j == 0:
                count+=1
            j-=1
        if count==1:
            return True


    return False

def generateDude(num1,num2):
    li = []
    for i in range(num1,num2):
        if primeNumber(i):
            li.append(i)
    return abs(min(li)+max(li))



def main():
    num1, num2 = map(int, input().split(" "))
    if num1 < num2:
        otp = generateDude(num1,num2)
        print(otp)

if __name__ == "__main__":
    main()
