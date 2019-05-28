# Enter your code here. Read input from STDIN. Print output to STDOUT
def fact(num):
    if num == 0:
        return 1

    i = num - 1
    while i > 0:
        num *= i
        i -= 1
    return num

zeroRejects = (fact(10)/(fact(0)*fact(10)))*(.12**0)*(.88**10)
oneReject = (fact(10)/(fact(1)*fact(9)))*(.12**1)*(.88**9)
twoRejects = (fact(10)/(fact(2)*fact(8)))*(.12**2)*(.88**8)

percent1 = round((zeroRejects + oneReject + twoRejects) - .0005, 3)
percent2 = round((zeroRejects + oneReject) - .0005, 3)
percent3 = round(1 - percent2, 3)
print(percent1)
print(percent3)
