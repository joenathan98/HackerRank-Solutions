# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
x = list(map(int,input().strip().split()))
f = list(map(int,input().strip().split()))


def median(arr):
    median = 0
    arrLen = len(arr)
    if arrLen % 2 == 0:
        median = (arr[int(arrLen // 2)-1] + arr[int(arrLen // 2)]) / 2
        return median
    else:
        median = arr[int(arrLen) // 2]
        return median

a = []
for i in range(n):
    a.extend([x[i]]*f[i])

a.sort()
half = len(a)//2

if len(a) % 2 == 0: 
    q1 = median(a[:half])
    q3 = median(a[half:])
    print(float(q3-q1))
else:
    q1 = median(a[:half])
    q3 = median(a[half+1:])
    print(float(q3-q1))