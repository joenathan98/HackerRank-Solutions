n = int(input())
arr = list(map(int,input().strip().split()))
from collections import Counter


#finding the mean
mean = 0
for i in range(n):
    mean += arr[i]

print(round((float(mean/n)),1))

#findinf the median
arr.sort()
if(len(arr)%2 == 0):
    median = float((arr[(n//2)] + arr[n//2)-1])/2)
    print(median)
else:
    print(float(arr[n//2]))

#finding the mode 
data = Counter(arr)
get_mode = dict(data)
mode = [k for k, v in get_mode.items() if v == max(list(data.values()))]
if len(mode) == n:
    print(arr[0])
else:
    print(mode[0])
