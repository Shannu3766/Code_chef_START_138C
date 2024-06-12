# cook your dish here

#from collections import deque,Counter
#from math import ceil, floor

from sympy import primerange

def innum():
    return int(input())
def inmany():
    return map(int,input().split())
def inlist():
    return list(inmany())

nums = list(primerange(3,100500))
nums = [a*a for a in nums]

for T in range(innum()):
    
    N = innum() - 4
    
    possible = False
    i = 0
    j = len(nums)-1
    
    while(i<j):
        if nums[i] + nums[j] == N:
            possible = True
            break
        
        elif nums[i] + nums[j] > N:
            j -= 1
        
        elif nums[i] + nums[j] < N:
            i += 1
    
    print("Yes" if possible else "No")