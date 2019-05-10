# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
x = list(map(int, input().strip().split()))

x.sort()

def median(arr):
    median = 0
    arrLen = len(arr)
    if arrLen % 2 == 0:
        median = (arr[int(arrLen / 2) - 1] + arr[int(arrLen / 2)]) // 2
        return median
    else:
        median = arr[int(len(arr) / 2)]
        return median


half = n//2
if n % 2 == 0:
    print(median(x[:half]))
    print(median(x))
    print(median(x[half:]))
else:
    print(median(x[:half]))
    print(median(x))
    print(median(x[half+1:]))
