# Enter your code here. Read input from STDIN. Print output to STDOUT
#factorial function
def fact(num):
    if num == 0:
        return 1

    i = num - 1
    while i > 0:
        num *= i
        i -= 1
    return num

#probability of having 0 boys
zeroBoys = (fact(6)/(fact(0)*fact(6-0)))*(.522**0)*(.478**6)

#probability of having 1 boy
oneBoy = (fact(6)/(fact(1)*fact(6-1)))*(.522**1)*(.478**5)

#probability of having 2 boys
twoBoys = (fact(6)/(fact(2)*fact(6-2)))*(.522**2)*(.478**4)

percent = round(1 - (zeroBoys + oneBoy + twoBoys)-0.0005, 3)
print(percent)