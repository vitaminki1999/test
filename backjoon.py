import sys
import math
import heapq
sys.setrecursionlimit(10**6)
input=sys.stdin.readline

n=int(input())
a=list(map(int,input().split()))

ans=0
temp=0

for i in a:
    temp+=i
    if i==0:
        temp=0
    ans+=temp
print(ans)
#헤헤