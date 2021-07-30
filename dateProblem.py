month = [31,28,31,30,31,30,31,31,30,31,30,31]
# first day of year is monday

day = int(input("enter date: "))
m = int(input("enter month no "))
sum = 0
sum+=day

switches= {
    0:'monday',
    1:'Tuesday',
    3:'Wednersday',
    4:'Friday',
    5:'Saturday',
    6:'Sunday',
}

print(switches[sum%7])