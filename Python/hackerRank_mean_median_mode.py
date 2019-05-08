n = int(input())
arr = list(map(int,input().strip().split()))
from collections import Counter


#finding the mean
mean = 0
for i in range(len(arr)):
    mean += arr[i]

print(round((float(mean/n)),1))

#findinf the median
arr.sort()
if(len(arr)%2 == 0):
    median = float((arr[(len(arr)//2)] + arr[(len(arr)//2)-1])/2)
    print(median)
else:
    print(float(arr[len(arr)//2]))

#finding the mode 
data = Counter(arr)
get_mode = dict(data)
mode = [k for k, v in get_mode.items() if v == max(list(data.values()))]
if len(mode) == n:
    print(arr[0])
else:
    print(mode[0])
print(len(mode))
